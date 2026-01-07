# PDF Text Extraction Models

The repository was created from a real-world problem I personally faced that is extracting usable text from PDFs.
Sometimes we only need texts. Sometimes we need to modify it, translate it, analyze it, or process further. PDFs make these tasks unnecessarily difficult, especially when they come in different formats.

This project aims to be a **helpful toolkit** for handling multiple PDF text extraction scenarios.

## Features

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

For direct image OCR, see:
- **File:** `ocr-image.py`

## Run Command
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


## Accuracy Overview

| PDF Type | Expected Accuracy |
|--------|------------------|
| Text-based English PDF | ~100% |
| AI-assisted language PDF | ~99%+ |
| Scanned printed English PDF | ~95%+ |
| Handwritten scanned PDF | Low / Not reliable |


## Limitations

- AI-assisted extraction may produce small inaccuracies
- Handwritten text is difficult and not a primary focus
- OCR accuracy depends on image quality, resolution, and clarity

These limitations are expected and documented intentionally.

---

## Future Improvements

Planned enhancements include:

- Better handling of low-quality scans
- Expanded multilingual support
- Cleaner output formatting
- broading formats including pdf to docs, image_scan pdf to text pdf etc

## Support the Project

If you find this repository useful:

- ⭐ Star the repository
- 💖 Sponsor the project

Your support helps keep development active and sustainable.

## License

This project is open-source and available under the MIT License.
