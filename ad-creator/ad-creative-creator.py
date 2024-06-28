from flask import Flask, request, jsonify
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

def create_ad_creative(ad_name, title, body, image_url):
    # Load environment variables from .env file
    load_dotenv()

    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')
    page_id = os.getenv('META_PAGE_ID')
    
    # Initialize Facebook API
    FacebookAdsApi.init(access_token=access_token)

    fields = []
    params = {
        'name': ad_name,
        'object_id': page_id,
        'title': title,
        'body': body,
        'image_url': image_url,
    }

    try:
        creative = AdAccount(ad_account_id).create_ad_creative(
            fields=fields,
            params=params,
        )
        creative_id = creative.get_id()
        return {'status': 'success', 'creative_id': creative_id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.route('/create_ad_creative', methods=['POST'])
def api_create_ad_creative():
    data = request.json
    ad_name = data.get('ad_name')
    title = data.get('title')
    body = data.get('body')
    image_url = data.get('image_url')
    
    result = create_ad_creative(ad_name, title, body, image_url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
