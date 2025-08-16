# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Document Conversion (Primary Task)
```bash
# Make script executable (first time only)
chmod +x Convert_YFD_to_PWA.sh

# Convert markdown chapters to ProWriting Aid DOCX format
./Convert_YFD_to_PWA.sh
```

### EQ Benchmark Analysis
```bash
# Run from verona_eq_benchmark/ directory
cd verona_eq_benchmark/

# Full analysis suite
python3 verona_eq_benchmark.py
python3 comparative_analysis.py

# Or use the runner script for menu-driven execution
chmod +x run_analysis.sh && ./run_analysis.sh
```

## Repository Architecture

This is a manuscript conversion and analysis project with two distinct components:

### 1. Document Conversion Pipeline
- **Purpose**: Convert a 20-chapter markdown manuscript to ProWriting Aid-compatible DOCX format
- **Source**: `/markdown_yfd/` contains original Chapter_1.md through Chapter_20.md files
- **Output**: `/docx_pwa/` receives converted DOCX files (individual and combined)
- **Script**: `Convert_YFD_to_PWA.sh` handles heading normalization, pandoc conversion, and document merging

### 2. EQ Benchmark Framework
- **Location**: `/verona_eq_benchmark/` directory
- **Purpose**: Analyzes emotional intelligence in the manuscript using adapted EQBench3 methodology
- **Components**:
  - `novel_analysis_framework.py`: Extracts emotionally complex passages
  - `verona_eq_benchmark.py`: Main evaluation system with 5-dimensional scoring
  - `comparative_analysis.py`: Compares results against LLM benchmarks
  - Configuration and results stored as JSON files

## Key Implementation Details

### Markdown Processing
- Chapter headings are normalized to `# Chapter N: Title` (H1 format for ProWriting Aid)
- python-docx creates precise structure: Heading1 + Normal styles only
- Empty paragraphs added after chapter headings for proper parsing
- Files are sorted numerically (handling Chapter_1 through Chapter_20 correctly)
- Zero page breaks ensure clean document flow for chapter detection

### Dependencies
- **Python 3.7+**: Required for python-docx conversion engine and EQ analysis
- **python-docx**: Automatically installed by conversion script if needed
- **pandoc**: Fallback option for DOCX conversion (check with `command -v pandoc`)

### File Paths
- All scripts use relative paths from their respective directories
- The EQ benchmark scripts expect `../markdown_yfd/` to access manuscript files
- Output directories are created automatically if they don't exist

## Working with the Manuscript

The manuscript "Verona Resurrected" is a Gothic horror reimagining of Romeo and Juliet with 20 chapters. When modifying conversion scripts or analysis tools:

1. Preserve the original markdown files in `/markdown_yfd/`
2. Maintain chapter naming convention: `Chapter_N.md`
3. Ensure heading format consistency for ProWriting Aid compatibility
4. The EQ benchmark framework reads directly from markdown source files

## Error Handling Notes

- Pandoc warnings about file extensions are expected and harmless
- The conversion script uses `set -euo pipefail` for strict error handling
- Python scripts should handle missing files gracefully
- Check for pandoc installation before running conversion