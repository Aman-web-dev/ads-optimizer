from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)





def update_object(object_type, object_id, data,access_token):
    """Updates a Facebook object based on its type, ID, and new data"""
    url = f'https://graph.facebook.com/v20.0/{object_id}'
    params = {'access_token': access_token}
    headers = {'Content-Type': 'application/json'}
    print(params,headers,access_token,data)
    response = requests.post(url, params=params, headers=headers, json=data)
     # Check for successful response (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
    # Log or handle errors based on the response
        print(f"Error updating {object_type}: {response.json()}")
    return None  # Or raise an exception





@app.route('/bulk_update_objects', methods=['POST'])
def bulk_update_objects():
    data = request.get_json()
    objects = data.get('objects')
    update = data.get('update')  # Singular update data for all objects
    access_token = data.get('access_token')

    # Validate input parameters
    if not objects:
        return jsonify({'error': 'Objects data is required'}), 400
    if not update:
        return jsonify({'error': 'Update data is required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    valid_object_types = ['campaign', 'adset', 'ad', 'creative']

    try:
        for obj in objects:
            object_type = obj.pop('id', None)  # Check for 'id' key for backward compatibility
            if not object_type:
                return jsonify({'error': 'Object ID is required'}), 400
            if object_type not in valid_object_types:
                return jsonify({'error': f'Invalid object type: {object_type}'}), 400

            # Update object based on its type and ID
            update_object(object_type, obj['id'], update, access_token)

        return jsonify({'message': 'Objects updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500









@app.route('/bulk_update_campaigns', methods=['POST'])
def bulk_update_campaigns():
    data = request.get_json()
    campaigns = data.get('campaigns')
    update= data.get('updates')
    access_token=data.get('access_token')
    if not campaigns:
        return jsonify({'error': 'Campaigns data is required'}), 400

    try:
        for campaign in campaigns:
            campaign_id = campaign.pop('id')
            res=update_object('campaign', campaign_id,update,access_token)
        return jsonify({'message': 'Campaigns updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500










# Similar endpoints for ad sets, ads, and creatives

@app.route('/bulk_update_adsets', methods=['POST'])
def bulk_update_adsets():
    data = request.get_json()
    adsets = data.get('adsets')
    update= data.get('updates')
    access_token=data.get('access_token')
    if not adsets:
        return jsonify({'error': 'Campaigns data is required'}), 400

    try:
        for adset in adsets:
            adset_id = adset.pop('id')
            res=update_object('adset', adset_id,update,access_token)
        return jsonify({'message': 'Campaigns updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500













@app.route('/bulk_update_ads', methods=['POST'])
def bulk_update_ads():
    data = request.get_json()
    ads = data.get('ads')
    update= data.get('updates')
    access_token=data.get('access_token')
    if not ads:
        return jsonify({'error': 'Campaigns data is required'}), 400

    try:
        for ad in ads:
            ad_id = ad.pop('id')
            res=update_object('ad', ad_id,update,access_token)
        return jsonify({'message': 'Campaigns updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500












@app.route('/bulk_update_creatives', methods=['POST'])
def bulk_update_creatives():
    data = request.get_json()
    creatives = data.get('creatives')
    update= data.get('updates')
    access_token=data.get('access_token')
    if not creatives:
        return jsonify({'error': 'Campaigns data is required'}), 400

    try:
        for creative in creatives:
            creative_id = creative.pop('id')
            res=update_object('campaign', creative_id,update,access_token)
        return jsonify({'message': 'Campaigns updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
