import os
import zipfile
import uuid
from flask import Flask, request, send_file, jsonify, render_template
from pdf2image import convert_from_path

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "converted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert_pdf_to_png():
    if 'files' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    files = request.files.getlist('files')
    output_zip = os.path.join(OUTPUT_FOLDER, f"converted_{uuid.uuid4().hex}.zip")
    
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            if file.filename == "":
                continue
            
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            images = convert_from_path(file_path)
            
            for i, image in enumerate(images):
                image_filename = f"{os.path.splitext(file.filename)[0]}_page_{i + 1}.png"
                image_path = os.path.join(OUTPUT_FOLDER, image_filename)
                image.save(image_path, "PNG")
                zipf.write(image_path, image_filename)
                os.remove(image_path)
            
            os.remove(file_path)
    
    return send_file(output_zip, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
