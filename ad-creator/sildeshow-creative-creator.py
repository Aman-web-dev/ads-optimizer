from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Load environment variables
META_ACCESS_TOKEN = os.getenv('META_ACCESS_TOKEN')
META_ACC_ID = os.getenv('META_ACC_ID')
META_API_VERSION = os.getenv('META_API_VERSION')

@app.route('/create_slideshow_video', methods=['POST'])
def create_slideshow_video():
    # Extract parameters from request
    image_urls = request.form.getlist('image_urls[]')
    duration_ms = request.form.get('duration_ms', type=int)
    transition_ms = request.form.get('transition_ms', type=int)

    # Construct slideshow_spec
    slideshow_spec = {
        "images_urls": image_urls,
        "duration_ms": duration_ms,
        "transition_ms": transition_ms
    }

    # Prepare payload for POST request to Facebook Graph API
    payload = {
        'slideshow_spec': slideshow_spec,
        'access_token': META_ACCESS_TOKEN
    }

    # Construct URL for Facebook API endpoint
    url = f'https://graph-video.facebook.com/{META_API_VERSION}/act_{META_ACC_ID}/advideos'

    # Send POST request to Facebook API
    response = requests.post(url, data=payload)

    # Check if request was successful
    if response.status_code == 200:
        return jsonify({'message': 'Slideshow video created successfully'})
    else:
        return jsonify({'error': 'Failed to create slideshow video'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
