from flask import Flask, request, jsonify
import requests
import pymongo
import os
import json
from utils.utils import encode_payload

app = Flask(__name__)
MONGO_URI = os.environ["MONGO_DB_URI"]
client = pymongo.MongoClient(MONGO_URI)

db = client["Ads"] 



@app.route('/campaign', methods=['POST'])
def create_campaign():
  
    json_body = request.json
    
    params= json_body['params']
      
    access_token = json_body['access_token']
    ad_account_id = json_body['ad_account_id']
    api_version = json_body['api_version']
    
    payload=params
    payload['access_token']=access_token
    
    collection = db["campaigns"] 

    print(payload)
    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/campaigns"

    response = requests.post(url, data=payload)
    
    if(response.status_code==200):
        campaignId=response.json()
        print(campaignId)
        saving_data=params
        saving_data["campaignId"]=campaignId['id']
        result = collection.insert_one(saving_data)
        print(result)
        
    return response.json()




@app.route('/create_adset', methods=['POST'])
def create_adset():
    
    json_body = request.json
    ad_account_id = json_body['ad_account_id']
    
    params= json_body['params']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["ad-sets"] 

    if not all([params,ad_account_id, access_token, api_version]):
        return "Missing required fields", 400
    
    payload= params
    payload['access_token']=access_token
    
    payload=encode_payload(payload=payload)
    
    print(payload)
    print(ad_account_id)

    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adsets"

    response = requests.post(url, data=payload)
    
    if response.status_code==200:
        adset_id=response.json()
        adset_details=payload
        adset_details['adset_id']=adset_id['id']
        result = collection.insert_one(adset_details)
        
    return jsonify(response.json())


    
    
    
@app.route('/create_adcreative', methods=['POST'])
def create_adcreative():
    
    json_body = request.json
    
    
    ad_account_id = json_body['ad_account_id']
    name = json_body['name']
    object_story_spec = json_body['object_story_spec']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["creatives"] 

    if not all([ad_account_id, name, object_story_spec,access_token, api_version]):
        return "Missing required fields", 400

    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adcreatives"
    payload = {
        'name': name,
        'object_story_spec':json.dumps(object_story_spec) ,
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    
    creative_id=response.json()
    result = collection.insert_one(creative_id)

    
    return jsonify(response.json())

    
    
    
@app.route('/create_ad', methods=['POST'])
def create_ad():
    json_body = request.json
    
    
    ad_account_id = json_body['ad_account_id']
    params = json_body['params']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    payload=params
    payload['access_token']=access_token
    collection = db["ads"] 
    
    
    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/ads"

    # Sending the POST request to the Facebook API
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        ad_id = response.json()
        # Storing the response in the MongoDB collection
        data= payload
        data['ad_id']=ad_id['id']
        result = collection.insert_one(data)
        return jsonify(ad_id)
    else:
        return jsonify(response.json()), response.status_code


    
    
if __name__ == '__main__':
    app.run(debug=True)    
    