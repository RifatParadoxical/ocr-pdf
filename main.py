from pypdf import PdfReader

def main():
    reader = PdfReader('IELTS.pdf', strict=False)
    extracted_text = ''
    pages = reader.pages
    for page in pages:
        text = page.extract_text()
        if text:  
            extracted_text += text + '\n'
            
    with open('IELTS.txt', 'w', encoding='utf-8') as f:
        f.write(extracted_text)


if __name__ == "__main__":
    main()
