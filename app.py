from flask import Flask, render_template, request, jsonify
from rembg import remove
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    input_image = Image.open(file.stream)
    
    # AI Background Removal
    output = remove(input_image)
    
    # Base64 mein convert karna taake frontend pe display ho sake
    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return jsonify({"processed_image": img_str})

if __name__ == '__main__':
    app.run(debug=True)