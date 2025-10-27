import fitz  # PyMuPDF
import argparse
import sys
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text.strip()

def main():
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF using PyMuPDF (fitz)."
    )
    parser.add_argument("--pdf_path", help="Path to the input PDF file.")
    parser.add_argument(
        "-o", "--output", help="Path to output text file. If omitted, prints to stdout."
    )
    args = parser.parse_args()

    try:
        text = extract_text_from_pdf(args.pdf_path)
    except Exception as e:
        print(f"Error extracting text from '{args.pdf_path}': {e}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Error writing to '{args.output}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(text)

if __name__ == "__main__":
    main()
    
