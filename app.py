from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
from PIL import Image  # Exemplo para conversão de imagens
from pdf2image import convert_from_path  # Para converter PDFs

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
CONVERTED_FOLDER = "converted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            
            converted_filepath = convert_file(filepath)
            
            return send_file(converted_filepath, as_attachment=True)
    return render_template('index.html')


def convert_file(filepath):
    """Converte o arquivo para outro formato (PDF para PNG ou JPG)."""
    filename, ext = os.path.splitext(os.path.basename(filepath))
    
    if ext.lower() in ['.png', '.jpeg', '.jpg']:
        converted_filepath = os.path.join(CONVERTED_FOLDER, f"{filename}.jpg")
        img = Image.open(filepath)
        img = img.convert("RGB")  # Converte para evitar problemas
        img.save(converted_filepath, "JPEG")
        return converted_filepath
    
    elif ext.lower() == '.pdf':
        images = convert_from_path(filepath)
        converted_filepath = os.path.join(CONVERTED_FOLDER, f"{filename}.png")
        images[0].save(converted_filepath, "PNG")  # Salva apenas a primeira página
        return converted_filepath
    
    return filepath

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
