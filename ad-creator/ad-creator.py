from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/create_ad', methods=['POST'])
def create_ad():
    data = request.get_json()
    
    api_version = os.getenv('META_API_VERSION')
    
    name = data.get('name', 'My Ad')
    adset_id = data.get('adset_id')
    creative = data.get('creative', {
        'creative_id': '<CREATIVE_ID>'
    })
    status = data.get('status', 'PAUSED')
    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')

    url = f'https://graph.facebook.com/{api_version}/act_{ad_account_id}/ads'
    
    payload = {
        'name': name,
        'adset_id': adset_id,
        'creative': creative,
        'status': status,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)