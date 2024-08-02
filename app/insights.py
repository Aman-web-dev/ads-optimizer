from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)



def get_insights(object_type, object_id, level, metrics, date_preset):
    """Fetches insights for a given object type, ID, level, metrics, and date preset"""
    url = f'https://graph.facebook.com/v20.0/{object_id}/{level}'
    params = {
        'access_token': ACCESS_TOKEN,
        'level': level,
        'fields': ','.join(metrics),
        'date_preset': date_preset
    }
    response = requests.get(url, params=params)
    return response.json()

@app.route('/campaign_insights', methods=['GET'])
def get_campaign_insights():
    campaign_id = request.args.get('campaign_id')
    metrics = request.args.getlist('metrics')
    date_preset = request.args.get('date_preset')
    insights = get_insights('insights', campaign_id, 'campaign', metrics, date_preset)
    return jsonify(insights)

@app.route('/adset_insights', methods=['GET'])
def get_adset_insights():
    adset_id = request.args.get('adset_id')
    metrics = request.args.getlist('metrics')
    date_preset = request.args.get('date_preset')
    insights = get_insights('insights', adset_id, 'adset', metrics, date_preset)
    return jsonify(insights)

@app.route('/ad_insights', methods=['GET'])
def get_ad_insights():
    ad_id = request.args.get('ad_id')
    metrics = request.args.getlist('metrics')
    date_preset = request.args.get('date_preset')
    insights = get_insights('insights', ad_id, 'ad', metrics, date_preset)
    return jsonify(insights)

if __name__ == '__main__':
    app.run(debug=True)
