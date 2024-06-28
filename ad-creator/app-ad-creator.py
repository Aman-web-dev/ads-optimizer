from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Load environment variables
META_ACCESS_TOKEN = os.getenv('META_ACCESS_TOKEN')
META_ACC_ID = os.getenv('META_ACC_ID')
META_API_VERSION = os.getenv('META_API_VERSION')
META_PAGE_ID = os.getenv('META_PAGE_ID')

@app.route('/create_ad_creative', methods=['POST'])
def create_ad_creative():
    # Extract common parameters from request
    name = request.form.get('name')
    ad_type = request.form.get('ad_type')  # 'single', 'carousel', or 'video'
    message = request.form.get('message', 'Try it out')
    app_store_url = request.form.get('app_store_url')

    # Construct object_story_spec based on ad_type
    if ad_type == 'single':
        image_hash = request.form.get('image_hash')
        object_story_spec = {
            "page_id": META_PAGE_ID,
            "link_data": {
                "call_to_action": {
                    "type": "INSTALL_MOBILE_APP",
                    "value": {
                        "link": app_store_url
                    }
                },
                "image_hash": image_hash,
                "link": app_store_url,
                "message": message
            }
        }
    elif ad_type == 'carousel':
        image_hash = request.form.get('image_hash')
        deep_link = request.form.get('deep_link')
        child_attachments = []
        for i in range(4):
            child_attachments.append({
                "link": app_store_url,
                "image_hash": image_hash,
                "call_to_action": {
                    "type": "USE_MOBILE_APP",
                    "value": {
                        "app_link": deep_link
                    }
                }
            })
        object_story_spec = {
            "page_id": META_PAGE_ID,
            "link_data": {
                "message": message,
                "link": app_store_url,
                "caption": "WWW.ITUNES.COM",
                "name": "The link name",
                "description": "The link description",
                "child_attachments": child_attachments,
                "multi_share_optimized": True
            }
        }
    elif ad_type == 'video':
        video_id = request.form.get('video_id')
        thumbnail_url = request.form.get('thumbnail_url')
        object_story_spec = {
            "page_id": META_PAGE_ID,
            "video_data": {
                "call_to_action": {
                    "type": "INSTALL_MOBILE_APP",
                    "value": {
                        "link": app_store_url
                    }
                },
                "image_url": thumbnail_url,
                "video_id": video_id
            }
        }
    else:
        return jsonify({'error': 'Invalid ad_type'}), 400

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