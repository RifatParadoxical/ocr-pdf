import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_scanned_pdf(pdf_path, output_txt_path):
    try:
        print(f"Starting OCR process for: {pdf_path}")
        print("Step 1: Converting PDF pages to images...")
        images = convert_from_path(pdf_path, dpi=300)
        print(f"Converted {len(images)} pages to images.")
        extracted_text = ""
        print("\nStep 2: Performing OCR on each page...")
        for i, image in enumerate(images):
            print(f"  Processing page {i}/{len(images)}...")
            page_text = pytesseract.image_to_string(image, lang='eng')
            extracted_text += f"\n--- Page {i} ---\n\n"
            extracted_text += page_text
            extracted_text += "\n\n"

        print("\nStep 3: Saving extracted text to file...")
        with open(output_txt_path, 'w', encoding='utf-8') as text_file:
            text_file.write(extracted_text.strip())
        print(f"Text extraction complete. Output saved to: {output_txt_path}")

        print(f"✓ Text successfully extracted and saved to: {output_txt_path}")
        print(f"✓ Total characters extracted: {len(extracted_text)}")
        return True

    except FileNotFoundError:
        print(f"✗ Error: PDF file not found at '{pdf_path}'")
        print("  Please check the file path and try again.")
        return False
        
    except Exception as e:
        print(f"✗ An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Ensure Tesseract OCR is installed and in your PATH")
        print("2. Ensure Poppler is installed (required by pdf2image)")
        print("3. Check that the PDF file is not corrupted")
        return False
    
if __name__ == "__main__":
    # input_pdf = "image_scan(1).pdf" 
    # output_txt = "hand_written_image_scan_pdf.txt"
    # extract_text_from_scanned_pdf(input_pdf, output_txt)

    input_pdf = "image_scan.pdf" 
    output_txt = "image_scan_pdf.txt"
    extract_text_from_scanned_pdf(input_pdf, output_txt)