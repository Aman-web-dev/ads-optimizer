from flask import Flask, request, jsonify
import requests
import os 
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/create_campaign', methods=['POST'])
def create_campaign():
    
    # Load environment variables from .env file
    load_dotenv()
    
    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')
    api_version = os.getenv('META_API_VERSION')
    
    data = request.get_json()
    
    name = data.get('name', 'Video Views campaign')
    objective = data.get('objective', 'OUTCOME_ENGAGEMENT')
    status = data.get('status', 'PAUSED')
    special_ad_categories = data.get('special_ad_categories', [])
    
    url = f'https://graph.facebook.com/v{api_version}/act_{ad_account_id}/campaign'
    
    payload = {
        'name': name,
        'objective': objective,
        'status': status,
        'special_ad_categories': special_ad_categories,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
