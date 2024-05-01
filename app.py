from flask import Flask, request, send_file, jsonify
from PIL import Image
from rembg import remove
import os
import uuid

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
  # Check if an image is uploaded
  if 'image' not in request.files:
    return jsonify({'error': 'No image uploaded'}), 400

  # Get the uploaded image
  file = request.files['image']

  # Validate file extension (optional)
  # allowed_extensions = ['jpeg', 'jpg', 'png']
  # if file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
  #   return jsonify({'error': 'Unsupported file format'}), 400

  # Generate a secure filename
  filename = f'{uuid.uuid4()}.jpg'

  try:
    # Load the image
    img = Image.open(file)
    # Process the image
    processed_img = remove(img)

    # Save the processed image
    processed_img.save(os.path.join('uploads', filename), 'JPEG')

    # Return success response with the processed image filename
    return jsonify({'success': True, 'filename': filename}), 200
  except Exception as e:
    print(f'Error processing image: {e}')
    return jsonify({'error': 'Failed to process image'}), 500

if __name__ == '__main__':
  # Create uploads folder if it doesn't exist
  os.makedirs('uploads', exist_ok=True)
  app.run(debug=True)
