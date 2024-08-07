from flask import Flask, request, jsonify
import requests
import pymongo
import os
import json
from utils.utils import encode_payload

app = Flask(__name__)
MONGO_URI = os.environ["MONGO_DB_URI"]
client = pymongo.MongoClient(MONGO_URI)


FACEBOOK_URL=os.environ["FACEBOOK_API_URL"]
db = client["Ads"] 


@app.route('/advideo', methods=['POST'])
def create_advideo():
    try:
        json_body = request.json
        if not json_body:
            return jsonify({'error': 'Request body is required'}), 400

        ad_account_id = json_body.get('ad_account_id')
        params = json_body.get('params')
        access_token = json_body.get('access_token')

        if not ad_account_id or not params or not access_token:
            return jsonify({'error': 'Missing required fields'}), 400

        collection = db["ad-sets"]

        payload = encode_payload({**params, 'access_token': access_token})

        url = f"{FACEBOOK_URL}/act_{ad_account_id}/advideos"
        response = requests.post(url, data=payload)

        response.raise_for_status()  # Ensure that HTTP errors are raised

        advideo_data = response.json()
        advideo_id = advideo_data.get('id')
        if not advideo_id:
            return jsonify({'error': 'Failed to create ad set, no ID returned'}), 500

        advideo_details = {**params, 'advideo_id': advideo_id, 'access_token': access_token}
        collection.insert_one(advideo_details)

        return jsonify({'message': 'Ad set created successfully', 'advideo_id': advideo_id}), 201

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/advideos', methods=['GET'])
def get_all_advideos():
    try:
        json_body = request.json
        if not json_body:
            return jsonify({'error': 'Request body is required'}), 400

        access_token = json_body.get('access_token')
        account_id = json_body.get('account_id')
        fields = json_body.get('fields', None)  # Handle optional fields parameter

        if not account_id:
            return jsonify({'error': 'Account ID is required'}), 400
        if not access_token:
            return jsonify({'error': 'Access token is required'}), 400

        url = f'{FACEBOOK_URL}/act_{account_id}/advideos'
        params = {'access_token': access_token}

        if fields:
            params['fields'] = fields

        response = requests.get(url, params=params)
        response.raise_for_status()
        advideos = response.json()

        return jsonify({'advideos': advideos.get('data', [])}), 200

    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'HTTP request error occurred: {req_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500



    
    
  
    
    
if __name__ == '__main__':
 app.run(debug=True)