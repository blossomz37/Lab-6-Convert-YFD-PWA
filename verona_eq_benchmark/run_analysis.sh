#!/bin/bash

# Verona EQ Benchmark Setup and Runner
# Quick setup script for the Emotional Intelligence evaluation framework

echo "🧠 Verona Resurrected EQ Benchmark"
echo "=================================="

# Check if we're in the right directory
if [ ! -d "../markdown_yfd" ]; then
    echo "❌ Error: markdown_yfd directory not found!"
    echo "   Please run this script from the verona_eq_benchmark/ directory"
    exit 1
fi

if [ ! -f "verona_eq_benchmark.py" ]; then
    echo "❌ Error: verona_eq_benchmark.py not found!"
    echo "   Please ensure you're in the correct directory"
    exit 1
fi

echo "📂 Directory structure verified ✓"
echo "📚 Novel files found ✓"
echo ""

# Check Python availability
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Error: Python not found!"
        echo "   Please install Python 3.7 or later"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "🐍 Python available: $PYTHON_CMD ✓"
echo ""

# Menu options
echo "Select analysis to run:"
echo "1) Full EQ Benchmark Evaluation"
echo "2) Comparative Analysis with LLMs" 
echo "3) Both (Recommended)"
echo "4) Quick Framework Test"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Running Full EQ Benchmark Evaluation..."
        $PYTHON_CMD verona_eq_benchmark.py
        ;;
    2)
        echo ""
        echo "📊 Running Comparative Analysis..."
        $PYTHON_CMD comparative_analysis.py
        ;;
    3)
        echo ""
        echo "🎯 Running Complete Analysis Suite..."
        echo ""
        echo "Step 1/2: Full EQ Benchmark Evaluation"
        $PYTHON_CMD verona_eq_benchmark.py
        echo ""
        echo "Step 2/2: Comparative Analysis"
        $PYTHON_CMD comparative_analysis.py
        ;;
    4)
        echo ""
        echo "🔧 Running Framework Test..."
        $PYTHON_CMD novel_analysis_framework.py
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "✅ Analysis complete!"
echo ""
echo "📁 Generated files:"
ls -la *.json *.md 2>/dev/null | head -10

echo ""
echo "📖 For detailed results, see:"
echo "   • VERONA_EQ_ANALYSIS_REPORT.md - Comprehensive analysis report"
echo "   • verona_eq_benchmark_results.json - Detailed evaluation data"
echo "   • verona_comparative_analysis.json - LLM comparison results"
echo ""
echo "🎉 Thank you for using the Verona EQ Benchmark framework!"
