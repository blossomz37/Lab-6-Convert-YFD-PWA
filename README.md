# Lab 6: Convert YFD to PWA

This repository contains the Lab 6 markdown conversion project for preparing "Your First Draft" manuscript files for import into ProWriting Aid.

## 🚀 Quick Start

### Web Interface (Recommended)
**Launch as webpage:** Visit the [YFD to PWA Converter](https://blossomz37.github.io/Lab-6-Convert-YFD-PWA/) web application

- **🌐 Browser Conversion:** Upload and convert files directly in your browser (completely private)
- **⚡ GitHub Actions:** Use automated workflows for batch processing

### Command Line Interface
```bash
chmod +x Convert_YFD_to_PWA.sh
./Convert_YFD_to_PWA.sh
```

## Overview

This project includes:
- **🌐 Web Application:** Browser-based conversion interface at [blossomz37.github.io/Lab-6-Convert-YFD-PWA](https://blossomz37.github.io/Lab-6-Convert-YFD-PWA/)
- **⚡ GitHub Actions:** Automated conversion workflows
- Original markdown files for a 20-chapter manuscript ("Verona Resurrected")
- Automated conversion script for ProWriting Aid compatibility
- DOCX output files ready for ProWriting Aid import
- Both individual chapter files and a combined document

## Directory Structure

```
lab_6_markdown_conversion_project/
├── README.md                    # This file
├── Convert_YFD_to_PWA.sh       # Conversion script for ProWriting Aid
├── markdown_yfd/               # Original markdown files (source)
│   ├── Chapter_1.md            # "Dark Alchemy"
│   ├── Chapter_2.md
│   └── ... (Chapters 1-20)    # Complete 20-chapter manuscript
├── docx_pwa/                   # ProWriting Aid ready files (DOCX format)
│   ├── Chapter_1.docx
│   ├── Chapter_2.docx
│   ├── ... (Chapters 1-20)
│   └── all_chapters.docx       # Combined manuscript file
```

## Requirements

- **Python 3.7+**: Required for the python-docx conversion engine
- **python-docx**: Automatically installed by the script if needed
- **pandoc** (fallback): Universal document converter
  - macOS: `brew install pandoc`
  - Ubuntu/Debian: `sudo apt-get install pandoc`
  - Windows: Download from [pandoc.org](https://pandoc.org/installing.html)

## Usage Methods

### 🌐 Web Interface (Easiest)

Visit **[blossomz37.github.io/Lab-6-Convert-YFD-PWA](https://blossomz37.github.io/Lab-6-Convert-YFD-PWA/)** for the user-friendly web application:

1. **Browser Conversion:** Upload your `.md` files directly in the browser
   - Completely private - no files leave your device
   - Drag & drop interface for easy file handling
   - Instant conversion with downloadable results

2. **GitHub Actions:** Use automated workflows for batch processing
   - Fork this repository to your account
   - Replace files in `markdown_yfd/` with your manuscript
   - Automatic conversion via GitHub's cloud infrastructure

### 📱 Command Line Interface

For advanced users or local processing:

### Purpose

The `Convert_YFD_to_PWA.sh` script prepares your markdown files for import into ProWriting Aid by:

1. **Standardizing chapter headings**: Converts periods to colons and ensures consistent H1 (`#`) format
2. **Converting to DOCX format**: Uses python-docx for precise ProWriting Aid compatibility
3. **Creating combined document**: Generates both individual chapter files and a single merged document
4. **ProWriting Aid optimization**: Ensures exact structure compatibility for chapter detection
5. **Preserving originals**: Creates converted copies while leaving original files unchanged

### Usage

1. **Make the script executable** (one-time setup):
   ```bash
   chmod +x Convert_YFD_to_PWA.sh
   ```

2. **Run the conversion**:
   ```bash
   ./Convert_YFD_to_PWA.sh
   ```

3. **Alternative: Combine both commands with "&&"**:
   ```bash
   chmod +x Convert_YFD_to_PWA.sh && ./Convert_YFD_to_PWA.sh
   ```

4. **Output**: Converted files will be created in the `./docx_pwa/` directory
   - Individual chapter files: `Chapter_1.docx`, `Chapter_2.docx`, etc.
   - Combined manuscript: `all_chapters.docx` (all chapters in one document)

### What the Script Does

- **Dependency Check**: Automatically installs python-docx if needed (falls back to pandoc)
- **File Processing**: Scans the `./markdown_yfd/` directory for all `.md` files
- **Heading Standardization**: Converts chapter headings to `# Chapter N:` format (H1 for ProWriting Aid)
- **Precise Conversion**: Uses python-docx to create DOCX with exact ProWriting Aid structure
- **Individual Files**: Creates separate DOCX files for each chapter
- **Combined Document**: Merges all chapters into `all_chapters.docx` with proper structure
- **ProWriting Aid Optimization**: 
  - Only uses `Heading1` + `Normal` styles
  - Adds empty paragraphs after chapter headings
  - Zero page breaks for clean document flow
- **Progress Feedback**: Provides detailed conversion status and verification

### Example Conversion

**Original format**:
```markdown
## Chapter 1. Dark Alchemy
```

**Standardized format**:
```markdown
# Chapter 1: Dark Alchemy
```
*Note: The script automatically converts periods to colons and H2 to H1 format for ProWriting Aid compatibility*

## File Formats

### Markdown Files (`/markdown_yfd/`)
- Original manuscript files for "Verona Resurrected" (20 chapters)
- Chapter headings use H2 format (`## Chapter N.` or `## Chapter N:`)
- Complete manuscript content preserved
- Source files for the conversion process

### ProWriting Aid Ready (`/docx_pwa/`)
- **Optimized files** for ProWriting Aid chapter detection
- **Individual chapters**: `Chapter_1.docx` through `Chapter_20.docx`
- **Combined manuscript**: `all_chapters.docx` (all 20 chapters optimized)
- **Perfect structure**: `Heading1` + `Normal` styles only
- **Chapter format**: H1 headings with colon format (`# Chapter N: Title`)
- **Empty paragraphs**: Added after each chapter heading for proper parsing
- **Zero page breaks**: Clean document flow for optimal detection
- **Microsoft Word compatible** DOCX format

## ProWriting Aid Import Instructions

1. Run the conversion script: `./Convert_YFD_to_PWA.sh`
2. In ProWriting Aid, select "Import Document"
3. Choose files from the `docx_pwa/` directory:
   - Import individual chapters for detailed analysis
   - Import `all_chapters.docx` for full manuscript review
4. **✅ Success**: ProWriting Aid will now properly detect and split all 20 chapters

## Technical Requirements

- **Python 3.7+** (for python-docx conversion engine)
- **Bash shell** (included on macOS/Linux)
- **python-docx** (automatically installed by script)
- **Pandoc** (fallback option)
  ```bash
  # Install on macOS with Homebrew
  brew install pandoc
  ```

## Notes

- Original files in `/markdown_yfd/` are never modified
- **python-docx engine**: Creates perfect ProWriting Aid structure (Heading1 + Normal only)
- **Chapter detection**: Optimized with empty paragraphs and proper heading hierarchy
- **Multiple runs safe**: Script can be run multiple times (overwrites previous output)
- **Auto-standardization**: Converts periods to colons (e.g., "Chapter 1. Title" → "Chapter 1: Title")
- **Cross-platform**: All paths use relative references for compatibility
- **Version control ready**: Suitable for GitHub sharing and collaboration
- **Smart numbering**: Handles chapters 1-20 correctly in proper sequence
- **Fallback support**: Uses pandoc if python-docx installation fails

## Troubleshooting

### Script Permission Issues
```bash
chmod +x Convert_YFD_to_PWA.sh
```

### Missing Output Directory
The script automatically creates the `docx_pwa` directory if it doesn't exist.

### No Files Found
Ensure you're running the script from the project root directory where the `markdown_yfd/` folder is located.

### Pandoc Warnings
You may see warnings like "Could not deduce format from file extension" - these are harmless as pandoc correctly defaults to markdown format.

## Contributing

When adding new chapters to the "Verona Resurrected" manuscript:
1. Place original markdown files in the `markdown_yfd/` directory
2. Follow the naming convention: `Chapter_N.md` (where N is the chapter number)
3. Use H2 headings for chapter titles: `## Chapter N: Title`
4. Run the conversion script to update ProWriting Aid versions
5. Commit both original and converted versions

## About the Manuscript

"Verona Resurrected" is a Gothic horror reimagining of Romeo and Juliet, exploring themes of love, death, resurrection, and moral ambiguity through 20 chapters of dark fantasy narrative.

## License

This project contains manuscript content and conversion utilities. Please respect copyright and intellectual property rights.

## Repository Information

- **Repository**: [Lab-6-Convert-YFD-PWA](https://github.com/blossomz37/Lab-6-Convert-YFD-PWA)
- **Owner**: blossomz37
- **Branch**: main
- **Language**: Shell, Python, Markdown
