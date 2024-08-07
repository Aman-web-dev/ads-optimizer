from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)





def delete_object(access_token,object_id):
    """Deletes a Facebook object based on its type and ID"""
    url = f'https://graph.facebook.com/v20.0/{object_id}'
    params = {'access_token': access_token}
    response = requests.delete(url, params=params)
    return response.json()





@app.route('/bulk_delete_objects', methods=['POST'])
def bulk_delete_objects():
    data = request.json
    object_type = data.get('object_type')
    object_ids = data.get('object_ids')
    access_token = data.get('access_token')

    # Validate input parameters
    if not object_type:
        return jsonify({'error': 'Object type is required'}), 400
    if not object_ids:
        return jsonify({'error': 'Object IDs are required'}), 400
    if not access_token:
        return jsonify({'error': 'Access token is required'}), 400

    valid_object_types = ['campaign', 'adset', 'ad', 'creative']  # Define allowed object types
    if object_type not in valid_object_types:
        return jsonify({'error': f'Invalid object type: {object_type}'}), 400

    try:
        for object_id in object_ids:
            delete_object(access_token, object_id)
        return jsonify({'message': f'{object_type.title()}s deleted successfully'})  # Use title case for success message
    except Exception as e:
        return jsonify({'error': str(e)}), 500





@app.route('/delete_campaign', methods=['POST'])
def bulk_delete_campaigns():
    data = request.json
    campaign_id = data['campaign_id']
    access_token=data['access_token']
    if not campaign_id:
        return jsonify({'error': 'Campaign IDs are required'}), 400

    try:
        delete_object(access_token,campaign_id)
        return jsonify({'message': 'Campaign deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    

    @app.route('/delete_adset', methods=['POST'])
    def bulk_delete_adsets():
        data = request.json
        adset_id= data['adset_id']
        access_token=data['access_token']
        if not adset_id:
            return jsonify({'error': 'Ad set IDs are required'}), 400

        try:
            
            delete_object(access_token,adset_id)
            return jsonify({'message': 'Ad set deleted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    

@app.route('/delete_ad', methods=['POST'])
def bulk_delete_ads():
    data = request.json
    ad_id = data['ad_id']
    access_token=data['access_token']
    if not ad_id:
        return jsonify({'error': 'Ad IDs are required'}), 400

    try:
        
        delete_object(access_token,ad_id)
        return jsonify({'message': 'Ads deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
    
    
    
    
    
    

@app.route('/bulk_delete_creatives', methods=['POST'])
def bulk_delete_creatives():
    data = request.json
    creative_ids = data['creative_ids']
    access_token=data['access_token']
    if not creative_ids:
        return jsonify({'error': 'Creative IDs are required'}), 400

    try:
        for creative_id in creative_ids:
            delete_object(access_token,creative_id)
        return jsonify({'message': 'Creatives deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Reuse the bulk_delete_campaigns function from the previous response

if __name__ == '__main__':
    app.run(debug=True)
