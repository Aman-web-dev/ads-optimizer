from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
import pymongo
import os
import json



client = pymongo.MongoClient(os.environ["MONGO_DB_URI"])

db = client["Ads"] 


@app.route('/create_campaign', methods=['POST'])
def create_campaign():
  
    json_body = request.json
    
    print(json_body)
    ad_account_id = json_body['ad_account_id']
    name = json_body['name']
    objective = json_body['objective']
    status = json_body['status']
    special_ad_categories = json_body['special_ad_categories']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["campaigns"] 

    payload = {
        'name': name,
        'objective': objective,
        'status': status,
        'special_ad_categories': special_ad_categories,
        'access_token': access_token  # Include access token in the payload
    }
    
    print(payload)
    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/campaigns"

    response = requests.post(url, data=payload)
    
    campaignId=response.json()
    
    print(campaignId)
    
    result = collection.insert_one(campaignId)
    
    print(result)
    return response.json()




@app.route('/create_adset', methods=['POST'])
def create_adset():
    
    json_body = request.json
    ad_account_id = json_body['ad_account_id']
    name = json_body['name']
    optimization_goal = json_body['optimization_goal']
    billing_event = json_body['billing_event']
    bid_amount = json_body['bid_amount']
    daily_budget = json_body['daily_budget']
    campaign_id = json_body['campaign_id']
    targeting = json_body['targeting']
    start_time = json_body['start_time']
    status = json_body['status']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["ad-sets"] 

    if not all([ad_account_id, name, optimization_goal, billing_event, bid_amount, daily_budget, campaign_id, targeting, start_time, status, access_token, api_version]):
        return "Missing required fields", 400

    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adsets"
    payload = {
        'name': name,
        'optimization_goal': optimization_goal,
        'billing_event': billing_event,
        'bid_amount': bid_amount,
        'daily_budget': daily_budget,
        'campaign_id': campaign_id,
        'targeting': json.dumps(targeting),
        'start_time': start_time,
        'status': status,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    
    adset_id=response.json()
    result = collection.insert_one()
    
    return jsonify(response.json())


    
    
    
@app.route('/create_adcreative', methods=['POST'])
def create_adcreative():
    
    json_body = request.json
    
    
    ad_account_id = json_body['ad_account_id']
    name = json_body['name']
    object_story_spec = json_body['object_story_spec']
    degrees_of_freedom_spec = json_body['degrees_of_freedom_spec']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["creatives"] 

    if not all([ad_account_id, name, object_story_spec, degrees_of_freedom_spec, access_token, api_version]):
        return "Missing required fields", 400

    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adcreatives"
    payload = {
        'name': name,
        'object_story_spec': object_story_spec,
        'degrees_of_freedom_spec': json.dumps(degrees_of_freedom_spec),
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    
    creative_id=response.json()
    result = collection.insert_one(creative_id)

    
    return jsonify(response.json())

    
    
    
@app.route('/create_ad', methods=['POST'])
def create_ad():
    json_body = request.json
    
    # Extracting the necessary fields from the request body
    ad_account_id = json_body['ad_account_id']
    name = json_body['name']
    adset_id = json_body['adset_id']
    creative_id = json_body['creative_id']
    status = json_body['status']
    access_token = json_body['access_token']
    api_version = json_body['api_version']
    
    collection = db["ads"] 
    
    # Payload for the Facebook API request
    payload = {
        'name': name,
        'adset_id': adset_id,
        'creative': {
            'creative_id': creative_id
        },
        'status': status,
        'access_token': access_token  # Include access token in the payload
    }
    
    url = f"https://graph.facebook.com/v{api_version}/act_{ad_account_id}/ads"

    # Sending the POST request to the Facebook API
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        ad_id = response.json()
        # Storing the response in the MongoDB collection
        collection = db['ads']
        result = collection.insert_one(ad_id)
        return jsonify(ad_id)
    else:
        return jsonify(response.json()), response.status_code


    
    
if __name__ == '__main__':
    app.run(debug=True)    
    