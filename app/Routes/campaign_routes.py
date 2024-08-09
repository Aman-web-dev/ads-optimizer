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


def handle_error(e, message='An error occurred'):
    if isinstance(e, requests.exceptions.HTTPError):
        return jsonify({'error': f'HTTP error occurred: {e}'}), 500
    else:
        return jsonify({'error': message, 'details': str(e)}), 500

def validate_params(json_body, required_params):
    for param in required_params:
        if not json_body.get(param):
            return False, jsonify({'error': f'{param} is required'}), 400
    return True, None

@app.route('/campaign', methods=['POST'])
def create_campaign():
  
    json_body = request.json
    
    params= json_body['params'] 
    access_token = json_body['access_token']
    ad_account_id = json_body["ad_account_id"]
   
    
    payload=params
    payload['access_token']=access_token
    
    collection = db["campaigns"] 

    print(payload)
    url = f"{FACEBOOK_URL}/act_{ad_account_id}/campaigns"

    response = requests.post(url, data=payload)
    
    if(response.status_code==200):
        campaignId=response.json()
        print(campaignId)
        saving_data=params
        saving_data["campaignId"]=campaignId['id']
        result = collection.insert_one(saving_data)
        print(result)
        
    return response.json()

#checked
@app.route('/campaign/<string:campaign_id>', methods=['POST'])
def update_campaign(campaign_id):
    request_data = request.json
    params = request_data.get('params')
    access_token = request_data.get('access_token')
    

    if not params:
        return jsonify({'error': 'Update Params data is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    url = f'{FACEBOOK_URL}/{campaign_id}'

    # Include the access token in the update parameters 
    params['access_token'] = access_token

    print(params)  # Print the payload for debugging

    try:
        # Send the payload as JSON
        response = requests.post(url, json=params)
        response.raise_for_status()  # Ensure that HTTP errors are raised
        return jsonify({'message': 'Campaign updated successfully'})
    except requests.exceptions.HTTPError as http_err:
        error_response = response.json() if response.content else {}
        print(f'HTTP error occurred: {http_err}')
        print(f'Error response content: {error_response}')
        return jsonify({'error': f'HTTP error occurred: {http_err}', 'details': error_response}), 500
    except Exception as e:
        print(f'Unexpected error occurred: {e}')
        return jsonify({'error': str(e)}), 500


@app.route('/campaigns', methods=['GET'])
def get_all_campaigns():
    try:
        json_body = request.json

        # Validate required parameters
        required_params = ['access_token', 'ad_account_id']
        is_valid, error_response = validate_params(json_body, required_params)
        if not is_valid:
            return error_response

        access_token = json_body['access_token']
        account_id = json_body['ad_account_id']
        params = json_body.get('params', {})

        # Add the access token to the params
        params['access_token'] = access_token

        url = f'{FACEBOOK_URL}/act_{account_id}/campaigns'

        # Send the GET request with params
        response = requests.get(url, params=params)
        response.raise_for_status()

        campaigns = response.json()
        return jsonify({'campaigns': campaigns.get('data', [])})

    except requests.exceptions.HTTPError as http_err:
        return handle_error(http_err, 'Failed to get campaigns')
    except Exception as e:
        return handle_error(e)








# checked
@app.route('/campaign/<string:id>', methods=['GET'])
def get_campaign(id):
    # Use request.args to get query parameters
    json_body = request.json
    params = json_body['params']
    access_token = json_body['access_token']
    
    # Check if required parameters are provided
    if not id:
        return jsonify({'error': 'Campaign ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400
    if not params:
        return jsonify({'error': 'params are required'}), 400

    try:
        url = f'{FACEBOOK_URL}/{id}'
        params['access_token']=access_token
        print(params)
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    

    # checked
@app.route('/campaign/<string:id>', methods=['DELETE'])
def delete_campaign(id):
    data = request.json
    access_token = data.get('access_token')

    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    url = f'{FACEBOOK_URL}/{id}'
    params = {'access_token': access_token}

    try:
        response = requests.delete(url, params=params)
        response.raise_for_status()
        return jsonify({'message': 'Campaign deleted successfully'})
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500






@app.route('/campaigns', methods=['DELETE'])
def delete_campaigns():
    json_body = request.json
    access_token = json_body.get('access_token')
    account_id = json_body.get("ad_account_id")
    params=json_body.get("params")

    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'{FACEBOOK_URL}/act_{account_id}/campaigns'
        params = {'access_token': access_token, 'params':params}
        response = requests.delete(url, params=params)
        response.raise_for_status()
        campaigns = response.json()

        return jsonify({'campaigns': campaigns.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)