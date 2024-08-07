from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)



def get_campaigns(account_id,access_token):
    """Fetches all campaigns for a given account ID"""
    url = f'https://graph.facebook.com/v20.0/act_{account_id}/campaigns'
    params = {'access_token': access_token, 'fields': 'id,name,objective,status'}
    response = requests.get(url, params=params)
    print(response.json())
    return response.json()


def get_adsets(campaign_id,access_token):
    """Fetches all ad sets for a given campaign ID"""
    url = f'https://graph.facebook.com/v20.0/{campaign_id}/adsets'
    params = {'access_token': access_token, 'fields': 'id,name,status'}
    response = requests.get(url, params=params)
    return response.json()

def get_ads(adset_id,access_token):
    """Fetches all ads for a given ad set ID"""
    url = f'https://graph.facebook.com/v20.0/{adset_id}/ads'
    params = {'access_token': access_token, 'fields': 'id,name,status'}
    response = requests.get(url, params=params)
    return response.json()


# @app.route('/campaigns', methods=['GET'])
# def get_all_campaign_data():
#     json_body = request.json
#     access_token = json_body['access_token']
#     account_id = json_body['account_id']

#     if not account_id:
#         return jsonify({'error': 'Account ID is required'}), 400

#     try:
#         campaigns = get_campaigns(account_id, access_token)
#         adsets = []
#         ads = []

#         for campaign in campaigns['data']:
#             adset_data = get_adsets(campaign['id'], access_token)
#             adsets.extend(adset_data['data'])
#             for adset in adset_data['data']:
#                 ad_data = get_ads(adset['id'], access_token)
#                 ads.extend(ad_data['data'])

#         return jsonify({'campaigns': campaigns['data'], 'adsets': adsets, 'ads': ads})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


    
    

@app.route('/adsets', methods=['GET'])
def get_all_campaign_data():
    json_body = request.json
    access_token = json_body.get('access_token')
    account_id = json_body.get('account_id')
    fields= json_body.get('fields')

    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'https://graph.facebook.com/v20.0/act_{account_id}/adsets'
        params = {'access_token': access_token, 'fields':fields}
        response = requests.get(url, params=params)
        response.raise_for_status()
        adsets = response.json()

        return jsonify({'campaigns': adsets.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500    
    

@app.route('/adset/<string:id>', methods=['GET'])
def get_adset():
    json_body = request.json
    adset_id = json_body['adset_id']
    access_token = json_body["access_token"]
    fields = json_body.get('fields', None)  # Handle optional fields parameter

    if not adset_id:
        return jsonify({'error': 'Ad Set ID is required'}), 400

    try:
        url = f'https://graph.facebook.com/v20.0/{adset_id}'
        params = {'access_token': access_token}

        if fields:  # Include fields parameter if provided
            params['fields'] = fields

        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
    

    

@app.route('/ads', methods=['GET'])
def get_all_campaign_data():
    json_body = request.json
    access_token = json_body.get('access_token')
    account_id = json_body.get('account_id')
    fields= json_body.get('fields')

    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'https://graph.facebook.com/v20.0/act_{account_id}/campaigns'
        params = {'access_token': access_token, 'fields':fields}
        response = requests.get(url, params=params)
        response.raise_for_status()
        campaigns = response.json()

        return jsonify({'campaigns': campaigns.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  
    

@app.route('/ad/<string:id>', methods=['GET'])
def get_ad():
    json_body= request.json 
    ad_id = json_body['ad_id']
    access_token = json_body['access_token']
    fields = json_body.get('fields', None)  # Handle optional fields parameter
    
    
    if not ad_id:
        return jsonify({'error': 'Ad ID is required'}), 400

    try:
        url = f'https://graph.facebook.com/v20.0/{ad_id}'
        params = {'access_token': access_token}

        if fields:  # Include fields parameter if provided
            params['fields'] = fields

        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/adcreatives', methods=['GET'])
def get_all_campaign_data():
    json_body = request.json
    access_token = json_body.get('access_token')
    account_id = json_body.get('account_id')
    fields= json_body.get('fields')

    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    try:
        url = f'https://graph.facebook.com/v20.0/act_{account_id}/adcreatives'
        params = {'access_token': access_token, 'fields':fields}
        response = requests.get(url, params=params)
        response.raise_for_status()
        creatives = response.json()

        return jsonify({'creatives': creatives.get('data', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500      