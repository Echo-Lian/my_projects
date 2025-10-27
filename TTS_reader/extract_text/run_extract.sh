#!/bin/bash

# define arguments
work_dir="/Users/echolian/Library/CloudStorage/OneDrive-UniversityofHelsinki/GitHub/github_repo/my_projects/TTS_reader/extract_text"
application="$work_dir/pdf2text.py"
input_pdf="/Users/echolian/Downloads/epis.pdf"
output_txt="$work_dir/epis.txt"

# activate virtual environment
source ~/TTS_project/bin/activate

# run application
python "$application" --pdf_path $input_pdf --output $output_txt