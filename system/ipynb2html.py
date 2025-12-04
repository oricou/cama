#! /usr/bin/env python3

import os
import nbconvert
from nbconvert import HTMLExporter
import nbformat
import sys
import shutil

def convert_notebooks_to_html(input_dir, output_dir):
    # Create HTML Exporter
    html_exporter = HTMLExporter()

    # Walk through the directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".ipynb"):
                # Construct the full file paths
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_file_dir = os.path.join(output_dir, relative_path)
                output_file_path = os.path.join(output_file_dir, file.replace('.ipynb', '.html'))
                
                # Create output directory if it doesn't exist
                os.makedirs(output_file_dir, exist_ok=True)

                # Read the notebook content
                with open(input_file_path, 'r', encoding='utf-8') as f:
                    notebook_content = nbformat.read(f, as_version=4)

                # Convert to HTML
                (body, resources) = html_exporter.from_notebook_node(notebook_content)

                # Write the HTML output
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(body)

                print(f"Converted {input_file_path} to {output_file_path}")

input_directory = sys.argv[1]
output_directory = sys.argv[2]
try:
    shutil.rmtree(output_directory)
except:
    pass
convert_notebooks_to_html(input_directory, output_directory)

