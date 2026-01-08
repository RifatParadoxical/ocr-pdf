from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    try:
        reader = PdfReader('electricity.pdf', strict=False)
        extracted_text = ''
        pages = reader.pages
        for page in pages:
            text = page.extract_text()
            if text:  
                extracted_text += text + '\n'
    except Exception as e:
        print("An error occurred while reading the PDF:", e)

    try:
        prompt = f"""The following Bengali(or whatever language it is) text was extracted from a PDF and may contain:
                    - broken characters
                    - incorrect punctuation
                    - spacing issues
                    - encoding artifacts

                    Your task:
                    1. Reconstruct proper Bengali(or whatever language it is) words where possible
                    2. Fix spelling and grammar
                    3. Remove encoding artifacts
                    4. Preserve original meaning
                    5. Do NOT add new content

                    Return only the corrected Bengali(or whatever language it is) text. \n\n {extracted_text} """

        r = model.generate_content(prompt)
        dot_txt = r.text
    except Exception as e:
        print("An error occurred while generating content:", e)

    try:
        with open('electricity.txt', 'w', encoding='utf-8') as f:
            f.write(dot_txt)
    except Exception as e:
        print("An error occurred while writing to the text file:", e)
if __name__ == "__main__":
    main()
