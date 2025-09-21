#!/usr/bin/env python3
"""
Sales Analysis Report Exporter
Exports the Jupyter notebook analysis to various formats in the reports folder.
"""

import os
import sys
import subprocess
from datetime import datetime

def export_reports():
    """Export the sales analysis notebook to multiple formats."""
    
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    notebook_dir = os.path.join(script_dir, 'notebooks')
    reports_dir = os.path.join(script_dir, 'reports')
    
    # Create reports directory if it doesn't exist
    os.makedirs(reports_dir, exist_ok=True)
    
    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    notebook_file = 'sales_analysis_report.ipynb'
    
    print("="*60)
    print("SALES ANALYSIS REPORT EXPORTER")
    print("="*60)
    print(f"Timestamp: {timestamp}")
    print(f"Reports directory: {reports_dir}")
    print()
    
    # Check if notebook exists
    notebook_path = os.path.join(notebook_dir, notebook_file)
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return False
    
    success_count = 0
    
    # Export to HTML
    try:
        html_file = f'sales_analysis_report_{timestamp}.html'
        html_path = os.path.join(reports_dir, html_file)
        
        cmd = [
            'jupyter', 'nbconvert',
            '--to', 'html',
            '--output', html_path,
            notebook_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ HTML report exported: {html_file}")
            success_count += 1
        else:
            print(f"❌ HTML export failed: {result.stderr}")
    except Exception as e:
        print(f"❌ HTML export error: {e}")
    
    # Export to PDF (optional, requires additional dependencies)
    try:
        pdf_file = f'sales_analysis_report_{timestamp}.pdf'
        pdf_path = os.path.join(reports_dir, pdf_file)
        
        cmd = [
            'jupyter', 'nbconvert',
            '--to', 'pdf',
            '--output', pdf_path,
            notebook_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ PDF report exported: {pdf_file}")
            success_count += 1
        else:
            print(f"⚠️  PDF export failed (dependencies may be missing)")
            print("   Install with: pip install nbconvert[webpdf] or apt-get install pandoc texlive")
    except Exception as e:
        print(f"⚠️  PDF export not available: {e}")
    
    # Export notebook as Python script
    try:
        py_file = f'sales_analysis_script_{timestamp}.py'
        py_path = os.path.join(reports_dir, py_file)
        
        cmd = [
            'jupyter', 'nbconvert',
            '--to', 'python',
            '--output', py_path,
            notebook_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Python script exported: {py_file}")
            success_count += 1
        else:
            print(f"❌ Python script export failed: {result.stderr}")
    except Exception as e:
        print(f"❌ Python script export error: {e}")
    
    # Create a simple README for the reports
    readme_path = os.path.join(reports_dir, 'README.md')
    with open(readme_path, 'w') as f:
        f.write("# Sales Analysis Reports\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Available Reports\n\n")
        f.write("- **HTML Report**: Interactive version with all visualizations\n")
        f.write("- **PDF Report**: Print-friendly version (if available)\n")
        f.write("- **Python Script**: Executable code version\n")
        f.write("- **Executive Summary**: Key insights in text format\n")
        f.write("- **Processed Data**: Enhanced dataset with customer clusters\n\n")
        f.write("## Usage\n\n")
        f.write("1. Open HTML report in web browser for interactive experience\n")
        f.write("2. Use PDF for presentations or printing\n")
        f.write("3. Run Python script to reproduce analysis\n")
        f.write("4. Share executive summary for quick insights\n")
    
    print(f"✅ README created: README.md")
    success_count += 1
    
    print()
    print("="*60)
    print(f"EXPORT SUMMARY: {success_count} files created successfully")
    print(f"Reports location: {os.path.abspath(reports_dir)}")
    print("="*60)
    
    return success_count > 0

if __name__ == "__main__":
    success = export_reports()
    sys.exit(0 if success else 1)
