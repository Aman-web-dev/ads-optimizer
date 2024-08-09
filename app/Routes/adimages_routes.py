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


@app.route('/adimages', methods=['POST'])
def create_adimage():
    # Extract JSON body and parameters
    json_body = request.json
    ad_account_id = json_body.get("ad_account_id")
    access_token = json_body.get('access_token')
    params=json_body.get('params')
    

    # Prepare data and optional parameters
    params = params
    params['access_token']=access_token

    if not ad_account_id:
        return jsonify({'error': 'Missing required parameter: ad_account_id'}), 400
    
    # Construct the API endpoint URL
    url = f'{FACEBOOK_URL}/{ad_account_id}/adimages'
    
    # Make the API call
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.post(url, headers=headers, data=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500

    # Return the created AdImage details
    return jsonify(response.json())


@app.route('/adimages', methods=['DELETE'])
def delete_ad_image():
    try:
        # Extract JSON body and parameters
        json_body = request.json
        ad_account_id = json_body.get("ad_account_id")
        access_token = json_body.get("access_token")
        params=json_body.get('params')
    

        if not ad_account_id:
            return jsonify({'error': 'Missing required parameter: ad_account_id'}), 400
        if not access_token:
            return jsonify({'error': 'Missing required parameter: access_token'}), 400
        if not params:
            return jsonify({'error': 'Missing required parameter: hash'}), 400

        # Construct the URL
        url = f"{FACEBOOK_URL}/act_{ad_account_id}/adimages"
        
        # Prepare the parameters for the DELETE request
        params=params
        params['access_token']=access_token
        
        # Make the DELETE request to the Facebook API
        response = requests.delete(url, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Return the success status
        return jsonify(response.json())

    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), response.status_code
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error occurred: {req_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'An error occurred: {err}'}), 500

@app.route('/adimages', methods=['GET'])
def get_ad_images():
    try:
        # Extract JSON body and parameters
        json_body = request.json
        params = json_body.get('params', {})
        ad_account_id = json_body.get("ad_account_id")
        access_token = json_body.get('access_token')

        if not ad_account_id:
            return jsonify({'error': 'Missing required parameter: ad_account_id'}), 400
        if not access_token:
            return jsonify({'error': 'Missing required parameter: access_token'}), 400

        params['access_token'] = access_token
        
        # Construct the URL 
        url = f"{FACEBOOK_URL}/act_{ad_account_id}/adimages"
        
        # Make the request to the Facebook API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes

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