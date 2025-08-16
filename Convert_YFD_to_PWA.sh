#!/bin/bash

# Convert YFD to PWA (Improved Version)
# Script to prepare markdown files for ProWriting Aid import
# Normalizes chapter headings and creates proper document structure

set -euo pipefail  # Exit on error, undefined vars, pipe failures

echo "Converting YFD files for ProWriting Aid import..."
echo "================================================"

# Create output directory if it doesn't exist
mkdir -p "./docx_pwa"

# Counter for processed files
count=0

# Array to store sorted filenames for combined document
declare -a sorted_files

# Function to normalize chapter headings for ProWriting Aid compatibility
normalize_chapter_heading() {
    local file="$1"
    # Convert to H1 headings (# Chapter) for ProWriting Aid compatibility
    # ProWriting Aid expects Heading1 style, not Heading2
    # Add empty line after each chapter heading to match document.docx structure
    # ## Chapter 1. Title -> # Chapter 1: Title
    # # Chapter 2: Title -> # Chapter 2: Title  
    # ## Chapter 3 Title -> # Chapter 3: Title
    sed -e 's/^## Chapter/# Chapter/g' \
        -e 's/^# Chapter \([0-9][0-9]*\)\. /# Chapter \1: /g' \
        -e 's/^# Chapter \([0-9][0-9]*\): /# Chapter \1: /g' \
        -e 's/^# Chapter \([0-9][0-9]*\) \([^:]*\)$/# Chapter \1: \2/g' \
        -e 's/^# Chapter \([0-9][0-9]*\): \(.*\)$/# Chapter \1: \2\n/' \
        "$file"
}

# Function to check if pandoc is installed
check_dependencies() {
    if ! command -v pandoc &> /dev/null; then
        echo "Error: pandoc is not installed or not in PATH"
        echo "Install pandoc: brew install pandoc (macOS) or apt-get install pandoc (Ubuntu)"
        exit 1
    fi
}

# Check dependencies
check_dependencies

# Process each markdown file in the markdown_yfd directory
for file in ./markdown_yfd/*.md; do
    if [ -f "$file" ]; then
        # Get the filename without the path and extension
        filename=$(basename "$file" .md)
        
        # Normalize chapter headings and convert to docx
        normalize_chapter_heading "$file" | pandoc -f markdown -t docx -o "./docx_pwa/${filename}.docx"
        
        echo "Converted: $filename.md -> $filename.docx"
        ((count++))
        
        # Add to sorted files array for combined document
        sorted_files+=("$file")
    fi
done

echo "================================================"
echo "Creating combined document..."

# Sort files numerically (Chapter_1, Chapter_2, ..., Chapter_10, etc.)
IFS=$'\n' sorted_files=($(printf '%s\n' "${sorted_files[@]}" | sort -V))

# Create temporary file for combined content
combined_temp=$(mktemp)

# Process files in numerical order and combine them
file_count=0
total_files=${#sorted_files[@]}

for file in "${sorted_files[@]}"; do
    ((file_count++))
    echo "Processing chapter $file_count of $total_files..."
    
    # Normalize chapter headings for combined file
    normalize_chapter_heading "$file" >> "$combined_temp"
    
    # Add clean separation between chapters (NO page breaks)
    # This creates proper document structure that ProWriting Aid can parse
    if [ $file_count -lt $total_files ]; then
        echo "" >> "$combined_temp"
        echo "" >> "$combined_temp"  # Double line break for clear separation
        echo "" >> "$combined_temp"  # Extra line for better chapter detection
    fi
done

# Check if python-docx is available
if ! python3 -c "import docx" 2>/dev/null; then
    echo "⚠️  python-docx not found. Installing..."
    python3 -m pip install python-docx --user --quiet
    
    # Check again
    if ! python3 -c "import docx" 2>/dev/null; then
        echo "❌ Failed to install python-docx. Falling back to pandoc..."
        # Fallback to pandoc
        pandoc "$combined_temp" \
            -f markdown \
            -t docx \
            --reference-doc="./docx_pwa/document.docx" \
            -o "./docx_pwa/all_chapters.docx"
    else
        echo "✅ python-docx installed successfully"
        # Use python-docx for precise control
        python3 markdown_to_docx.py "$combined_temp" "./docx_pwa/all_chapters.docx"
    fi
else
    echo "✅ Using python-docx for ProWriting Aid compatible conversion"
    # Use python-docx for precise control
    python3 markdown_to_docx.py "$combined_temp" "./docx_pwa/all_chapters.docx"
fi

# Clean up temporary file
rm "$combined_temp"

echo "Created: all_chapters.docx (ProWriting Aid optimized)"

echo "================================================"
echo "Conversion complete!"
echo "Processed $count individual files"
echo "Individual chapters are in: ./docx_pwa/"
echo "Combined document: ./docx_pwa/all_chapters.docx"
echo ""
echo "✅ ProWriting Aid Optimizations:"
echo "  - NO page breaks (allows proper chapter detection)"
echo "  - Exact structure match with working document.docx"
echo "  - Normalized H1 chapter headings (# Chapter N: Title)"
echo "  - ONLY Heading1 + Normal styles (python-docx precision)"
echo "  - Empty paragraph after each chapter heading"
echo "  - Natural document flow for parser compatibility"
echo ""
echo "📝 Note: Original files remain unchanged in ./markdown_yfd/"
echo "🎯 This document structure is optimized for ProWriting Aid chapter splitting"
