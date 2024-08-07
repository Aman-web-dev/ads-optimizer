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


@app.route('/ad', methods=['POST'])
def create_ad():
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

        url = f"{FACEBOOK_URL}/act_{ad_account_id}/ads"
        response = requests.post(url, data=payload)

        response.raise_for_status()  # Ensure that HTTP errors are raised

        ad_data = response.json()
        ad_id = ad_data.get('id')
        if not ad_id:
            return jsonify({'error': 'Failed to create ad set, no ID returned'}), 500

        ad_details = {**params, 'ad_id': ad_id, 'access_token': access_token}
        collection.insert_one(ad_details)

        return jsonify({'message': 'Ad set created successfully', 'ad_id': ad_id}), 201

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ad/<string:id>', methods=['POST'])
def update_ad(id):
    try:
        json_body = request.json
        if not json_body:
            return jsonify({'error': 'Request body is required'}), 400

        params = json_body.get('params')
        access_token = json_body.get('access_token')

        if not params:
            return jsonify({'error': 'Update Params data is required'}), 400
        if not access_token:
            return jsonify({'error': 'Access token is required'}), 400

        url = f'{FACEBOOK_URL}/{id}'
        payload = {**params, 'access_token': access_token}

        response = requests.post(url, data=payload)
        response.raise_for_status()  # Ensure that HTTP errors are raised

        return jsonify({'message': 'ad updated successfully'}), 200

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ads', methods=['GET'])
def get_all_ads():
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

        url = f'{FACEBOOK_URL}/act_{account_id}/ads'
        params = {'access_token': access_token}

        if fields:
            params['fields'] = fields

        response = requests.get(url, params=params)
        response.raise_for_status()
        ads = response.json()

        return jsonify({'ads': ads.get('data', [])}), 200

    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'HTTP request error occurred: {req_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/ad/<string:id>', methods=['GET'])
def get_ad(id):
    try:
        json_body = request.json
        if not json_body:
            return jsonify({'error': 'Request body is required'}), 400

        access_token = json_body.get("access_token")
        fields = json_body.get('fields', None)  # Handle optional fields parameter

        if not access_token:
            return jsonify({'error': 'Access token is required'}), 400

        url = f'{FACEBOOK_URL}/{id}'
        params = {'access_token': access_token}

        if fields:
            params['fields'] = fields

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json(), 200
        else:
            return jsonify({'error': response.json().get('error', 'Unknown error occurred')}), response.status_code

    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'HTTP request error occurred: {req_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
    

@app.route('/ad/<string:id>', methods=['DELETE'])
def bulk_delete_ads(id):
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request body is required'}), 400

        access_token = data.get('access_token')

        if not id:
            return jsonify({'error': 'Ad set ID is required'}), 400
        if not access_token:
            return jsonify({'error': 'Access token is required'}), 400

        url = f'{FACEBOOK_URL}/{id}'
        params = {'access_token': access_token}
        response = requests.delete(url, params=params)

        if response.status_code == 200:
            return jsonify({'message': 'Ad deleted successfully'}), 200
        else:
            return jsonify({'error': response.json().get('error', 'Unknown error occurred')}), response.status_code

    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'HTTP request error occurred: {req_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
if __name__ == '__main__':
 app.run(debug=True)