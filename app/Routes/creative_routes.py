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


@app.route('/creative', methods=['POST'])
def create_creative():
  
    json_body = request.json
    
    params= json_body['params']
      
    access_token = json_body['access_token']
    ad_account_id = json_body['ad_account_id']
   
    
    payload=params
    payload['access_token']=access_token
    
    collection = db["creatives"] 

    print(payload)
    url = f"{FACEBOOK_URL}/act_{ad_account_id}/creatives"

    response = requests.post(url, data=payload)
    
    if(response.status_code==200):
        creativeId=response.json()
        print(creativeId)
        saving_data=params
        saving_data["creativeId"]=creativeId['id']
        result = collection.insert_one(saving_data)
        print(result)
        
    return response.json()


@app.route('/creative/<string:id>', methods=['POST'])
def update_creative(id):
    json_body = request.json
    params = json_body['params']
    access_token = json_body['access_token']

    if not params:
        return jsonify({'error': 'Update Params data is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    url = f'{FACEBOOK_URL}/{id}'


    payload=params
    payload['access_token']=access_token

    try:
        response = requests.post(url,data=payload)
        response.raise_for_status()  # Ensure that HTTP errors are raised
        return jsonify({'message': 'creative updated successfully'})
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/creatives', methods=['GET'])
def get_all_creatives():
    json_body = request.json
    access_token = json_body.get('access_token')
    account_id = json_body.get('account_id')
    fields= json_body.get('fields')

    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'{FACEBOOK_URL}/act_{account_id}/creatives'
        params = {'access_token': access_token, 'fields':fields}
        response = requests.get(url, params=params)
        response.raise_for_status()
        creatives = response.json()

        return jsonify({'creatives': creatives.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500





@app.route('/creative/<string:id>', methods=['GET'])
def get_creative(id):
    # Use request.args to get query parameters
    fields = request.args.get('fields')
    access_token = request.args.get('access_token')
    
    # Check if required parameters are provided
    if not id:
        return jsonify({'error': 'creative ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400
    if not fields:
        return jsonify({'error': 'Fields are required'}), 400

    try:
        url = f'{FACEBOOK_URL}/{id}'
        params = {'access_token': access_token, 'fields': fields}
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    

    
    
@app.route('/creative/<string:id>', methods=['DELETE'])
def delete_creative(id):
    data = request.json
    access_token = data.get('access_token')

    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    url = f'{FACEBOOK_URL}/{id}'
    params = {'access_token': access_token}

    try:
        response = requests.delete(url, params=params)
        response.raise_for_status()
        return jsonify({'message': 'creative deleted successfully'})
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)