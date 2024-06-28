from flask import Flask, request, jsonify
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

def create_campaign(campaign_name, buying_type, objective, status ,special_ad_categories):
    # Load environment variables from .env file
    load_dotenv()

    access_token = os.getenv('META_ACCESS_TOKEN')
    ad_account_id = os.getenv('META_ACC_ID')

    # Initialize Facebook API
    FacebookAdsApi.init(access_token=access_token)

    fields = []
    params = {
        'name': campaign_name,
        'buying_type': buying_type,
        'objective': objective,
        'status': status,
        'special_ad_categories':special_ad_categories
    }

    try:
        campaign = AdAccount(ad_account_id).create_campaign(
            fields=fields,
            params=params,
        )
        campaign_id = campaign.get_id()
        return {'status': 'success', 'campaign_id': campaign_id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.route('/create_campaign', methods=['POST'])
def api_create_campaign():
    data = request.json
    campaign_name = data.get('campaign_name')
    buying_type = data.get('buying_type')
    objective = data.get('objective')
    status = data.get('status')
    special_ad_categories=data.get('special_ad_categories')

    result = create_campaign(campaign_name, buying_type, objective, status,special_ad_categories)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
