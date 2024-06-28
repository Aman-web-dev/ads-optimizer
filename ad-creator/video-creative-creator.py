from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Load environment variables
META_ACCESS_TOKEN = os.getenv('META_ACCESS_TOKEN')
META_ACC_ID = os.getenv('META_ACC_ID')
META_APP_SECRET = os.getenv('META_APP_SECRET')
META_PAGE_ID = os.getenv('META_PAGE_ID')
META_APP_ID = os.getenv('META_APP_ID')
META_API_VERSION = os.getenv('META_API_VERSION')

@app.route('/create_ad_creative', methods=['POST'])
def create_ad_creative():
    # Extract parameters from request
    name = request.form.get('name')
    thumbnail_url = request.form.get('thumbnail_url')
    video_id = request.form.get('video_id')

    # Construct object_story_spec
    object_story_spec = {
        "page_id": META_PAGE_ID,
        "video_data": {
            "image_url": thumbnail_url,
            "video_id": video_id
        }
    }

    # Prepare payload for POST request to Facebook Graph API
    payload = {
        'name': name,
        'object_story_spec': object_story_spec,
        'access_token': META_ACCESS_TOKEN
    }

    # Construct URL for Facebook API endpoint
    url = f'https://graph.facebook.com/{META_API_VERSION}/act_{META_ACC_ID}/adcreatives'

    # Send POST request to Facebook API
    response = requests.post(url, data=payload)

    # Check if request was successful
    if response.status_code == 200:
        return jsonify({'message': 'Ad creative created successfully'})
    else:
        return jsonify({'error': 'Failed to create ad creative'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
