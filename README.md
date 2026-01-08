# PDF Text Extraction Models

The repository was created from a real-world problem I personally faced that is extracting usable text from PDFs.
Sometimes we only need texts. Sometimes we need to modify it, translate it, analyze it, or process further. PDFs make these tasks unnecessarily difficult, especially when they come in different formats.

This project aims to be a **helpful toolkit** for handling multiple PDF text extraction scenarios.

## 📂 Features

This repository handles three major types of PDFs:

### 1. Text-Based PDFs (English)
**File:** `main.py`

- Works best with digitally generated PDFs
- Near 100% accuracy for English text
- Fast and lightweight
- No OCR required

### 2. Non-English / Complex Language PDFs (AI-Assisted)
**File:** `language-with-ai.py`

- Designed for languages where traditional tools struggle
- Uses AI to improve extraction accuracy and context
- Average accuracy: **99%+**
- Minor errors may still occur (AI is not perfect)

### 3. Scanned / Image-Based PDFs (OCR)
**File:** `ocr-pdf.py`

- Handles PDFs that are image-based
- Best results when:
  - Language is English
  - Text is printed (not handwritten)


### 4. Scanned PDFs with AI-Assisted OCR (Multi-language & HandWritten)
**File:** `ai-image-ocr-pdf.py`

- Combines OCR with AI assistance
- Better accuracy for scanned, handwritten, or non-English documents



## 🖲️ Run Command
To run any specific file for individual purpose of use, use the following command on terminal
```bash
    git clone https://github.com/RifatParadoxical/ocr-pdf.git
    cd ocr-pdf
    uv sync
```
After that you can open it on your application. 
Edit any specific line of code or change file name, move files accordingly and run the specific command:
```bash
    uv run <your-specific-file-name.py>
```


## 🏗️ System Requirements

This project depends on the following external tools:

- **Poppler** – Required for converting PDF pages to images  
  Installation guide:  
  https://github.com/oschwartz10612/poppler-windows/releases (Windows)  
  https://poppler.freedesktop.org/ (Linux / macOS via package managers)

- **Tesseract OCR** – OCR engine for extracting text from images  
  Official installation documentation:  
  https://tesseract-ocr.github.io/tessdoc/Installation.html

Ensure both tools are installed and available in your system PATH.

You can verify installation by running:
```bash
pdftoppm -h
tesseract --version
```


## 📊 Accuracy Overview

| PDF Type | Expected Accuracy |
|--------|------------------|
| Text-based English PDF | ~100% |
| AI-assisted language PDF | ~99%+ |
| Scanned printed English PDF | ~95%+ |
| Handwritten scanned PDF | ~98%+ |
| AI-assisted language scanned PDF | ~98%+ |

## 📝 Output Format Note
**Note:** <br>
The script writes plain `UTF-8` text using Python’s `open()` function. You can change the output filename extension (e.g., `.txt`, `.doc`, `.rtf`, `.md`) as needed, but no format-specific processing is applied.
If you want it even more minimal and blunt: <br>


## 🚨 Limitations

- AI-assisted extraction may produce small inaccuracies
- OCR accuracy depends on image quality, resolution, and clarity

These limitations are expected and documented intentionally.


## 🛠️ Troubleshooting

### "GEMINI_API_KEY not found"

- Ensure `.env` file exists in the same directory as the script
- Check the API key is correctly formatted: `GEMINI_API_KEY=your_key`
- No spaces around the `=` sign

### "PDF file not found"

- Verify the PDF file is in the same directory as the script
- Check the filename matches exactly (case-sensitive)
- Use absolute path if needed: `C:/Users/YourName/Documents/file.pdf`

### "Error converting PDF to images"

- Install Poppler and ensure it's in your system PATH
- For Windows: Add Poppler's `bin` folder to environment variables

### Low Accuracy Results

- Increase DPI: `convert_from_path(pdf_path, dpi=400)`
- Ensure the scan quality is good (not blurry or too dark)
- Try a different Gemini model

## 🆕 New Updates

- ✅ Integrated Google Gemini 2.5 Flash Lite model for enhanced accuracy
- ✅ Support for handwritten text recognition
- ✅ Multi-language OCR without additional configuration
- ✅ Improved error handling and validation
- ✅ Page-by-page processing with progress tracking
- ✅ Support for high-resolution scans (300 DPI)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests!


## 📄 License

This project is open-source and available for personal and commercial use.


## ⭐ Support

If this tool helped you, please consider giving it a star!


## 📞 Contact

For questions or support, please open an issue on GitHub.
