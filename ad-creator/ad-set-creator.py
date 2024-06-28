from flask import Flask, request, jsonify
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

def create_ad_set(campaign_id, ad_set_name, daily_budget, bid_amount):
    # Load environment variables from .env file
    load_dotenv()
    
    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')
    page_id = os.getenv('META_PAGE_ID')
    
    # Initialize Facebook API
    FacebookAdsApi.init(access_token=access_token)

    fields = []
    params = {
        'name': ad_set_name,
        'optimization_goal': 'PAGE_LIKES',
        'billing_event': 'IMPRESSIONS',
        'bid_amount': bid_amount,
        'promoted_object': {'page_id': page_id},
        'daily_budget': daily_budget,
        'campaign_id': campaign_id,
        'targeting': {'geo_locations': {'countries': ['US']}},
        'status': 'PAUSED',
    }

    try:
        ad_set = AdAccount(ad_account_id).create_ad_set(
            fields=fields,
            params=params,
        )
        ad_set_id = ad_set.get_id()
        return {'status': 'success', 'ad_set_id': ad_set_id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.route('/create_ad_set', methods=['POST'])
def api_create_ad_set():
    data = request.json
    campaign_id = data.get('campaign_id')
    ad_set_name = data.get('ad_set_name')
    daily_budget = data.get('daily_budget')
    bid_amount = data.get('bid_amount')
    
    result = create_ad_set(campaign_id, ad_set_name, daily_budget, bid_amount)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)