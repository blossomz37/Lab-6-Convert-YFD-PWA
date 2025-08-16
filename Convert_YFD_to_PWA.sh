#!/bin/bash

# Convert YFD to PWA
# Script to prepare markdown files for ProWriting Aid import
# Converts from markdown_yfd to docx_pwa format with H2 headings

echo "Converting YFD files for ProWriting Aid import..."
echo "================================================"

# Create output directory if it doesn't exist
mkdir -p "./docx_pwa"

# Counter for processed files
count=0

# Array to store sorted filenames for combined document
declare -a sorted_files

# Process each markdown file in the markdown_yfd directory
for file in ./markdown_yfd/*.md; do
    if [ -f "$file" ]; then
        # Get the filename without the path and extension
        filename=$(basename "$file" .md)
        
        # Convert H1 chapter headings to H2 and standardize format with colons
        # Handle both # Chapter and ## Chapter formats, convert periods to colons
        sed -e 's/^# Chapter/## Chapter/g' -e 's/^## Chapter \([0-9]*\)\./## Chapter \1:/g' "$file" | pandoc -f markdown -t docx -o "./docx_pwa/${filename}.docx"
        
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
    # Convert H1 to H2 and standardize format with colons for combined file
    sed -e 's/^# Chapter/## Chapter/g' -e 's/^## Chapter \([0-9]*\)\./## Chapter \1:/g' "$file" >> "$combined_temp"
    # Add page break after each chapter (except the last one)
    if [ $file_count -lt $total_files ]; then
        echo "" >> "$combined_temp"
        echo '```{=openxml}' >> "$combined_temp"
        echo '<w:p><w:r><w:br w:type="page"/></w:r></w:p>' >> "$combined_temp"
        echo '```' >> "$combined_temp"
        echo "" >> "$combined_temp"
    fi
done

# Convert combined content to docx
pandoc "$combined_temp" -f markdown -t docx -o "./docx_pwa/all_chapters.docx"

# Clean up temporary file
rm "$combined_temp"

echo "Created: all_chapters.docx (combined document)"

echo "================================================"
echo "Conversion complete!"
echo "Processed $count individual files"
echo "Individual chapters are in: ./docx_pwa/"
echo "Combined document: ./docx_pwa/all_chapters.docx"
echo ""
echo "Note: All chapter headings have been converted from H1 (#) to H2 (##)"
echo "Original files remain unchanged in ./markdown_yfd/"
