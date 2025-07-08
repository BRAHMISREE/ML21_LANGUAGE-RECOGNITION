
# 🌍 Language Recognition Web App

A Flask-based application that extracts text from uploaded images, detects the language, translates it to English, and provides a downloadable output — all in a beautiful UI.

---

## 🚀 Features

- 📤 Upload any image (screenshot, scanned doc, photo, etc.)
- 🔍 Text extraction using **Tesseract OCR**
- 🌐 Language detection with **Langdetect**
- 🔁 Translation to English via **TranslatePy**
- 💾 Download extracted raw text
---

## 🛠 Tech Stack

| Component       | Tech Used                           |
|-----------------|--------------------------------------|
| Backend         | Python, Flask                        |
| OCR             | pytesseract + Tesseract-OCR Engine   |
| Language Detect | langdetect                           |
| Translation     | translatepy                          |
| Frontend        | HTML, TailwindCSS, Lottie            |

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/language-recognition-app.git
cd language-recognition-app
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

#### Windows:

Download and install from:
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Make sure to add it to PATH.

#### macOS:

```bash
brew install tesseract
```

#### Ubuntu/Linux:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

---

### 4. Run the App

```bash
python app.py
```

Go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🗂 Project Structure

```
language-recognition-app/
├── app.py                  # Flask app
├── templates/
│   └── index.html          # Frontend UI
├── uploads/                # Uploaded images
├── downloads/              # Downloadable text files
├── static/ (optional)      # Add your static assets if needed
├── requirements.txt        # Python package list
└── README.md               # You're reading it :)
```

---

## 📜 Sample `requirements.txt`

```txt
Flask
pytesseract
Pillow
langdetect
translatepy
```

---

## ⚠ Notes

* OCR supports multiple languages: `eng+hin+tel+tam+kan+mal+ben+guj+pan` by default.
* Language detection may still detect other languages even if not listed in OCR.
* Translation supports many global languages but depends on TranslatePy's backend status.
* Avoid uploading large images to speed up processing.

---

## 👨‍💻 Author

Built with ❤️ by **IITI Soc'24**

---

## 📄 License

MIT License. Free to use, remix, and deploy.

```

---

Let me know if you want a `.gitignore`, deployment guide, or badge-style README tweaks too! 💻✅
```
