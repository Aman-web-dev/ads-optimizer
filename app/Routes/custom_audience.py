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



@app.route('/customaudiences', methods=['POST'])
def create_audience():
    try:
        json_body = request.json
        if not json_body:
            return jsonify({'error': 'Request body is required'}), 400

        ad_account_id = json_body.get('ad_account_id')
        params = json_body.get('params')
        access_token = json_body.get('access_token')

        if not ad_account_id or not params or not access_token:
            return jsonify({'error': 'Missing required params'}), 400


        payload = encode_payload({**params, 'access_token': access_token})

        url = f"{FACEBOOK_URL}/act_{ad_account_id}/customaudiences"
        response = requests.post(url, data=payload)

        response.raise_for_status()  # Ensure that HTTP errors are raised

        audience_data = response.json()
        audience_id = audience_data.get('id')
        if not audience_id:
            return jsonify({'error': 'Failed to create custom audience'}), 500


        return jsonify({'message': 'Custom audience created successfully'}), 201

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/customaudiences', methods=['GET'])
def get_custom_audiences():
    try:
        # Extract JSON body and parameters
        json_body = request.json
        ad_account_id = json_body.get("ad_account_id")
        access_token = json_body.get("access_token")
        params = json_body.get('params', {})

        if not ad_account_id:
            return jsonify({'error': 'Missing required parameter: ad_account_id'}), 400
        if not access_token:
            return jsonify({'error': 'Missing required parameter: access_token'}), 400

        # Include the access token in the parameters
        params['access_token'] = access_token

        # Construct the URL
        url = f"{FACEBOOK_URL}/act_{ad_account_id}/customaudiences"

        # Make the request to the Facebook API
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Return the response from Facebook API
        return jsonify(response.json())

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), response.status_code
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error occurred: {req_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'An error occurred: {err}'}), 500
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)