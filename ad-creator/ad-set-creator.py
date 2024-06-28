from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/create_ad_set', methods=['POST'])
def create_ad_set():
    
    data = request.get_json()
    
    name = data.get('name', 'A CPV Ad Set')
    campaign_id = data.get('campaign_id')
    daily_budget = data.get('daily_budget', 500)
    start_time = data.get('start_time', '2024-05-06T04:45:29+0000')
    end_time = data.get('end_time', '2024-06-06T04:45:29+0000')
    billing_event = data.get('billing_event', 'THRUPLAY')
    optimization_goal = data.get('optimization_goal', 'THRUPLAY')
    bid_amount = data.get('bid_amount', 100)
    targeting = data.get('targeting', {
        "device_platforms": ["mobile"],
        "geo_locations": {"countries": ["US"]},
        "publisher_platforms": ["facebook"]
    })
    status = data.get('status', 'PAUSED')
    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')
    api_version = os.getenv('META_API_VERSION')

    url = f'https://graph.facebook.com/{api_version}/act_{ad_account_id}/adsets'
    
    payload = {
        'name': name,
        'campaign_id': campaign_id,
        'daily_budget': daily_budget,
        'start_time': start_time,
        'end_time': end_time,
        'billing_event': billing_event,
        'optimization_goal': optimization_goal,
        'bid_amount': bid_amount,
        'targeting': targeting,
        'status': status,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
