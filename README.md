# optical-character-recognition (Image to Text Extraction using Tesseract OCR & OpenCV)

## 📌 Overview
Extracts text from images using **Tesseract OCR**, enhanced with **OpenCV** for image preprocessing. The pipeline improves text recognition accuracy by applying various image processing techniques before performing OCR.

Tesseract OCR (LSTM-based Model)

Tesseract v4+ (which this project uses) relies on a Long Short-Term Memory (LSTM) network, a specialized Recurrent Neural Network (RNN).

---

✅ Extract text from images automatically  
✅ Preprocess images for better OCR accuracy  
✅ Noise reduction and contrast enhancement   
✅ Customizable OCR settings (`--psm` & `--oem`)  

---

## 🛠️ Technologies Used
| Library     | Purpose |
|-------------|---------|
| **Python**  | Main programming language |
| **OpenCV (`cv2`)**  | Image processing and enhancement |
| **Pytesseract (`pytesseract`)**  | Python wrapper for Tesseract OCR |
| **Pillow (`PIL`)**  | Image handling and conversion |

---

## 🔧 Installation Guide

### 1️⃣ Prerequisites
- **Python 3.7+**
- **Tesseract OCR** (Download & Install from [here](https://github.com/tesseract-ocr/tesseract))  
  - After installation, add Tesseract to your system **PATH** (Windows)  
  - Run `tesseract --version` in the terminal to verify installation

### 2️⃣ Install Required Libraries
Run the following command:
```bash
pip install opencv-python pytesseract pillow
