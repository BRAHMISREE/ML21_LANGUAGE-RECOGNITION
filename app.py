from flask import Flask, render_template, request, send_from_directory
from PIL import Image, ImageFilter
import pytesseract
from langdetect import detect, detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from translatepy import Translator
from werkzeug.utils import secure_filename
import os


os.makedirs("uploads", exist_ok=True)
os.makedirs("downloads", exist_ok=True)

# --- Config ---
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)
DetectorFactory.seed = 0
translator = Translator()

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_language():
    if 'image' not in request.files:
        return render_template('index.html', result={"error": "No image uploaded."})

    image_file = request.files['image']
    if image_file.filename == '':
        return render_template('index.html', result={"error": "No file selected."})

    try:
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(filepath)

        # --- Preprocess Image ---
        image = Image.open(filepath).convert('L')              # Grayscale
        image = image.filter(ImageFilter.SHARPEN)              # Sharpen
        image = image.point(lambda x: 0 if x < 140 else 255)   # Binary threshold

        # --- OCR using Tesseract ---
        extracted_text = pytesseract.image_to_string(
            image,
            lang='eng+hin+tel+tam+kan+mal+ben+guj+pan'
        )

        if not extracted_text.strip():
            return render_template('index.html', result={"error": "No text found in image."})

        # --- Language Detection ---
        try:
            detected_language = detect(extracted_text)
            detected_languages_with_probabilities = detect_langs(extracted_text)
        except LangDetectException:
            return render_template('index.html', result={"error": "Language detection failed."})

        # --- Translation ---
        try:
            translated_text = translator.translate(extracted_text, "en").result
        except:
            translated_text = "Translation failed."

        # --- Save for Download ---
        text_filename = filename.rsplit('.', 1)[0] + '.txt'
        text_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], text_filename)
        with open(text_filepath, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        return render_template('index.html', result={
            "extracted_text": extracted_text,
            "detected_language": detected_language,
            "detected_languages_with_probabilities": detected_languages_with_probabilities,
            "translated_text": translated_text,
            "filename": text_filename,
            "download_ready": True,
            "image_url": f"/uploads/{filename}"  # 👈 Preview image after submission
        })

    except Exception as e:
        return render_template('index.html', result={"error": str(e)})

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
# --- Main ---
if __name__ == '__main__':
    app.run(debug=True)
