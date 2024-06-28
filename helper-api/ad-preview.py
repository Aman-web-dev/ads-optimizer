from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
app = Flask(__name__)

@app.route('/generate_previews', methods=['GET'])
def generate_previews():
    
    load_dotenv()
    # Extract parameters from the request
    creative = request.args.get('creative')
    ad_format = request.args.get('ad_format')
     # Replace with your actual ad account ID
    api_version = os.getenv('META_API_VERSION')
    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')

    # Construct the URL for the Facebook Graph API
    url = f'https://graph.facebook.com/{api_version}/act_{ad_account_id}/generatepreviews'

    # Prepare the data to be sent
    params = {
        'creative': creative,
        'ad_format': ad_format,
        'access_token': access_token
    }

    # Make the GET request to Facebook Graph API
    response = requests.get(url, params=params)

    # Check if request was successful
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to generate previews'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)