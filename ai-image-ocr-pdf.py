from pdf2image import convert_from_path
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

def extract_text_from_scanned_pdf(pdf_path, output_txt_path):
    try:
        print("configuring gemini api key...")
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
    except Exception as e:
        print(f"✗ An error occurred while configuring Gemini API: {str(e)}")
        return False
    try:
        print(f"Starting OCR process for: {pdf_path}")
        print("Step 1: Converting PDF pages to images...")
        images = convert_from_path(pdf_path, dpi=300)
        print(f"Converted {len(images)} pages to images.")
        extracted_text = ""
        print("\nStep 2: Performing OCR on each page...")
        for i, image in enumerate(images, start=1):
            print(f"  Processing page {i}/{len(images)}...")
            prompt = f"""OCR the image and extract the text accurately. 
                        Ensure proper spelling, grammar, and formatting.
                        Return only the extracted text from the image."""
            r = model.generate_content([prompt, image])
            page_text = r.text
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
        print("1. Ensure Gemini API key is correct and has access")
        print("2. Check that the PDF file is not corrupted")
        return False
    

if __name__ == "__main__":
        extract_text_from_scanned_pdf("handwritten_image_scan.pdf","hand_written_image_scan_pdf.txt")