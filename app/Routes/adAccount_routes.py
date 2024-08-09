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




@app.route('/create_adaccount', methods=['POST'])
def create_adaccount():
    # Extract form data from the request
    name = request.form.get('name')
    currency = request.form.get('currency')
    timezone_id = request.form.get('timezone_id')
    end_advertiser = request.form.get('end_advertiser')
    media_agency = request.form.get('media_agency')
    partner = request.form.get('partner')
    access_token = request.form.get('access_token')
    
    
    
    # Prepare the URL and payload
    url = "https://graph.facebook.com/<API_VERSION>/<BUSINESS_ID>/adaccount"
    payload = {
        'name': name,
        'currency': currency,
        'timezone_id': timezone_id,
        'end_advertiser': end_advertiser,
        'media_agency': media_agency,
        'partner': partner,
        'access_token': access_token
    }
    
    # Make the request to the Facebook API
    response = requests.post(url, data=payload)
    
    # Return the response from Facebook API
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)