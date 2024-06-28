from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image_path = request.form['image_path']
    
    # Get sensitive information from environment variables
    access_token = os.getenv('META_ACCESS_TOKEN')
    api_version = os.getenv('META_API_VERSION')
    ad_account_id = os.getenv('META_ACC_ID')
    page_id = os.getenv('META_PAGE_ID')
    image_hash = os.getenv('META_IMAGE_HASH')

    # Step 1: Upload the image
    image_upload_url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adimages"
    image_upload_files = {'filename': open(image_path, 'rb')}
    image_upload_data = {'access_token': access_token}

    image_response = requests.post(image_upload_url, files=image_upload_files, data=image_upload_data)

    if image_response.status_code != 200:
        return jsonify({'error': 'Image upload failed', 'details': image_response.json()}), image_response.status_code

    # Step 2: Create the ad creative
    ad_creative_url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adcreatives"
    ad_creative_data = {
        'name': 'Sample Creative',
        'object_story_spec': {
            'page_id': page_id,
            'link_data': {
                'image_hash': image_hash,
                'link': f'https://facebook.com/{page_id}',
                'message': 'try it out'
            }
        },
        'degrees_of_freedom_spec': {
            'creative_features_spec': {
                'standard_enhancements': {
                    'enroll_status': 'OPT_IN'
                }
            }
        },
        'access_token': access_token
    }

    ad_creative_response = requests.post(ad_creative_url, json=ad_creative_data)

    if ad_creative_response.status_code != 200:
        return jsonify({'error': 'Ad creative creation failed', 'details': ad_creative_response.json()}), ad_creative_response.status_code

    return jsonify({'success': 'Ad created successfully', 'ad_details': ad_creative_response.json()})


if __name__ == '__main__':
    app.run(debug=True)
