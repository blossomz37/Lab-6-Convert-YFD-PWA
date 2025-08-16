# Lab 6: Convert YFD to PWA

This repository contains the Lab 6 markdown conversion project for preparing "Your First Draft" manuscript files for import into ProWriting Aid.

## Overview

This project includes:
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
└── docx_pwa/                   # ProWriting Aid ready files (DOCX format)
    ├── Chapter_1.docx
    ├── Chapter_2.docx
    ├── ... (Chapters 1-20)
    └── all_chapters.docx       # Combined manuscript file
```

## Convert YFD to PWA Script

### Purpose

The `Convert_YFD_to_PWA.sh` script prepares your markdown files for import into ProWriting Aid by:

1. **Standardizing chapter headings**: Converts periods to colons and ensures consistent H2 (`##`) format
2. **Converting to DOCX format**: Uses pandoc to convert markdown to Word-compatible DOCX format
3. **Creating combined document**: Generates both individual chapter files and a single merged document with proper page breaks
4. **Preserving originals**: Creates converted copies while leaving original files unchanged

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

- Scans the `./markdown_yfd/` directory for all `.md` files
- Standardizes chapter heading format to `## Chapter N:` (converts periods to colons)
- Uses pandoc to convert markdown to DOCX format with proper OpenXML page breaks
- Creates individual files in `./docx_pwa/` directory
- Combines all chapters into `all_chapters.docx` with native DOCX page breaks after each chapter (except the last)
- Provides progress feedback and summary

### Example Conversion

**Original format**:
```markdown
## Chapter 1. Dark Alchemy
```

**Standardized format**:
```markdown
## Chapter 1: Dark Alchemy
```
*Note: The script automatically converts periods to colons for consistency and adds proper DOCX page breaks after each chapter*

## File Formats

### Markdown Files (`/markdown_yfd/`)
- Original manuscript files for "Verona Resurrected" (20 chapters)
- Chapter headings use H2 format (`## Chapter N.` or `## Chapter N:`)
- Complete manuscript content preserved
- Source files for the conversion process

### ProWriting Aid Ready (`/docx_pwa/`)
- Converted files optimized for ProWriting Aid import
- Individual chapter files: `Chapter_1.docx` through `Chapter_20.docx`
- Combined manuscript: `all_chapters.docx` (all 20 chapters with native DOCX page breaks)
- Standardized H2 chapter headings with consistent colon format (`## Chapter N: Title`)
- Native page breaks after each chapter (except the last) for proper manuscript formatting
- Microsoft Word compatible DOCX format

## ProWriting Aid Import Instructions

1. Run the conversion script: `./Convert_YFD_to_PWA.sh`
2. In ProWriting Aid, select "Import Document"
3. Choose files from the `docx_pwa/` directory:
   - Import individual chapters for detailed analysis
   - Import `all_chapters.docx` for full manuscript review
4. ProWriting Aid will recognize the H2 chapter headings for proper document structure

## Requirements

- **Bash shell** (included on macOS/Linux)
- **Pandoc** (for DOCX conversion)
  ```bash
  # Install on macOS with Homebrew
  brew install pandoc
  ```

## Notes

- Original files in `/markdown_yfd/` are never modified
- The script creates both individual chapter files and a combined document with native DOCX page breaks
- The script can be run multiple times safely (overwrites previous output)
- Chapter titles are automatically standardized from periods to colons (e.g., "Chapter 1. Title" → "Chapter 1: Title")
- All paths use relative references for cross-platform compatibility
- Suitable for version control and GitHub sharing
- Pandoc warnings about temporary file extensions are normal and harmless
- Chapter numbering is handled automatically and sorted correctly (1, 2, ..., 10, 11, etc.)

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

This lab project uses a 20-chapter gothic romance manuscript "Verona Resurrected" as sample content for demonstrating markdown-to-DOCX conversion workflows for writing tools like ProWriting Aid.

## License

This project contains manuscript content and conversion utilities. Please respect copyright and intellectual property rights.
