from flask import Flask, request, send_file
from PIL import Image
from rembg import remove
import io

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    # retrieve the Image from the Request
    # Expecting the image in a form-data field named 'image'
    file = request.files['image']
    # Load the image into a PIL object
    img = Image.open(file)
    # Process the Image
    processed_img = remove(img)

    # Save the image to a BytesIO object and send it as a response
    img_io = io.BytesIO()
    processed_img.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

