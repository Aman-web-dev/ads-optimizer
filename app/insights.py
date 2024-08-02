from flask import Flask, request, jsonify
import requests
import json
from .reading import get_campaigns,get_adsets,get_ads
app = Flask(__name__)



def get_insights(object_type, object_id, level, metrics, date_preset,access_token):
    """Fetches insights for a given object type, ID, level, metrics, and date preset"""
    url = f'https://graph.facebook.com/v20.0/{object_id}/insights'
    params = {
        'access_token': access_token,
        'level': level,
        'fields': ','.join(metrics),
        'date_preset': date_preset
    }
    response = requests.get(url, params=params)
    return response.json()



@app.route('/get_insights', methods=['GET'])
def get_insights_endpoint():
    json_body = request.json
    object_type = json_body['object_type']
    object_id = json_body['object_id']
    level = json_body['level'] # Default level to object_type
    metrics = json_body['metrics']
    date_preset = json_body['date_preset']
    access_token= json_body['access_token']

    # Validate input parameters
    if not object_type:
        return jsonify({'error': 'Object type is required'}), 400
    if not object_id:
        return jsonify({'error': 'Object ID is required'}), 400
    if not metrics:
        return jsonify({'error': 'Metrics are required'}), 400
    if not date_preset:
        return jsonify({'error': 'Date preset is required'}), 400

    # Valid levels based on object type
    valid_levels = {
        'campaign': ['campaign'],
        'adset': ['adset', 'campaign'],
        'ad': ['ad', 'adset', 'campaign']
    }

    if level not in valid_levels.get(object_type, []):
        return jsonify({'error': f'Invalid level for {object_type}: {level}'}), 400

    try:
        insights = get_insights(object_type, object_id, level, metrics, date_preset,access_token)
        print(insights)
        return jsonify(insights)
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/bulk_insights', methods=['POST'])
def bulk_insights():
    data = request.get_json()
    object_type = data.get('object_type')
    object_ids = data.get('object_ids')
    metrics = data.args.getlist('metrics')  # Use args for consistency with combined endpoint
    date_preset = data.args.get('date_preset')

    # Validate input parameters (similar to combined endpoint)

    insights = {}
    for object_id in object_ids:
        level = object_type  # Use object_type as the default level for all objects
        insights[object_id] = get_insights(object_type, object_id, level, metrics, date_preset)

    return jsonify(insights)


    
    
@app.route('/get_all_campaign_data_with_insights', methods=['GET'])
def get_all_campaign_data_with_insights():
    json_body = request.json
    access_token = json_body['access_token']
    account_id = json_body['ad_account_id']
    metrics = json_body['metrics']  # Metrics for insights
    date_preset = json_body['date_preset'] # Date preset for insights

    # Validate input parameters
    if not account_id:
        return jsonify({'error': 'Account ID is required'}), 400
    if not metrics:
        return jsonify({'error': 'Metrics are required for insights'}), 400
    if not date_preset:
        return jsonify({'error': 'Date preset is required for insights'}), 400

    try:
        campaigns = get_campaigns(account_id, access_token)
        all_data = {'campaigns': campaigns['data']}

        # Fetch and store insights for each level within a loop
        for campaign in all_data['campaigns']:
            campaign_id = campaign['id']
            all_data[f'adsets_{campaign_id}'] = get_adsets(campaign_id, access_token)
            all_data[f'ads_{campaign_id}'] = get_ads(campaign_id, access_token)

            # Get insights for each level (campaign, adset, ad)
            for level in ['campaign', 'adset', 'ad']:
                object_id = campaign_id if level == 'campaign' else campaign['id']  # Use campaign ID for campaign level
                insights = get_insights(level, object_id, level, metrics, date_preset,access_token)
                all_data[f'{level}_insights_{object_id}'] = insights

        return jsonify(all_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    app.run(debug=True)
    