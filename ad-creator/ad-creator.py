from flask import Flask, request, jsonify
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

def create_ad(ad_name, ad_set_id, creative_id):
    # Load environment variables from .env file
    load_dotenv()

    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')

    # Initialize Facebook API
    FacebookAdsApi.init(access_token=access_token)

    fields = []
    params = {
        'name': ad_name,
        'adset_id': ad_set_id,
        'creative': {'creative_id': creative_id},
        'status': 'PAUSED',
    }

    try:
        ad = AdAccount(ad_account_id).create_ad(
            fields=fields,
            params=params,
        )
        ad_id = ad.get_id()
        return {'status': 'success', 'ad_id': ad_id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_ad_previews(ad_id):
    fields = []
    params = {
        'ad_format': 'DESKTOP_FEED_STANDARD',
    }

    try:
        previews = Ad(ad_id).get_previews(
            fields=fields,
            params=params,
        )
        return {'status': 'success', 'previews': previews}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.route('/create_ad', methods=['POST'])
def api_create_ad():
    data = request.json
    ad_name = data.get('ad_name')
    ad_set_id = data.get('ad_set_id')
    creative_id = data.get('creative_id')

    result = create_ad(ad_name, ad_set_id, creative_id)
    return jsonify(result)

@app.route('/get_ad_previews', methods=['POST'])
def api_get_ad_previews():
    data = request.json
    ad_id = data.get('ad_id')

    result = get_ad_previews(ad_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
