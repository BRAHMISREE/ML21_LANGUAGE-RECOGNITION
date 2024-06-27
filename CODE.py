from PIL import Image
import pytesseract
from langdetect import detect, detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException


DetectorFactory.seed = 0


def detect_language_from_image(image_path):
    try:
        
        image = Image.open(image_path)
        
        
        extracted_text = pytesseract.image_to_string(image, lang='osd+eng')
        
        if not extracted_text.strip():
            return "No text found in image."
        
        
        detected_language = detect(extracted_text)
        detected_languages_with_prob = detect_langs(extracted_text)
        
        return {
            "extracted_text": extracted_text,
            "detected_language": detected_language,
            "detected_languages_with_probabilities": detected_languages_with_prob 
        }
    except LangDetectException as e:
        return f"Language detection error: {str(e)}" 
    except Exception as e:
        return f"An error occurred: {str(e)}" 


image_path = r"path to your image"  
result = detect_language_from_image(image_path)


if isinstance(result, str):
    print("Error:", result)  
else:
    print("Extracted Text:", result.get("extracted_text"))
    print("Detected Language:", result.get("detected_language"))
    print("Detected Languages with Probabilities:", result.get("detected_languages_with_probabilities"))
    
    
    if result.get("detected_languages_with_probabilities")[0].prob > 0.9:
        detected_lang_code = result.get("detected_languages_with_probabilities")[0].lang
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=input("Enter the language code: "))
        print("Text with detected language OCR:", text)