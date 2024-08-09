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


@app.route('/level/<string:id>/insights', methods=['GET'])
def get_insights(level_id):
    json_body = request.json
    access_token = json_body.get('access_token')
    params = json_body.get('params')

    if not level_id:
        return jsonify({'error': 'valid level ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'{FACEBOOK_URL}/{level_id}/insights'
        params['access_token'] = access_token
        response = requests.get(url, params=params)
        response.raise_for_status()
        insights = response.json()

        return jsonify({'insights': insights.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/level/<string:id>/insights', methods=['POST'])
def get_insights(level_id):
    json_body = request.json
    access_token = json_body.get('access_token')
    params = json_body.get('params')

    if not level_id:
        return jsonify({'error': 'valid level ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'{FACEBOOK_URL}/{level_id}/insights'
        params['access_token'] = access_token
        response = requests.post(url, data=params)
        response.raise_for_status()
        insights = response.json()

        return jsonify({'insights': insights.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
    
