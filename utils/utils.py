import requests
from flask import current_app

def create_facebook_campaign(ad_account_id, access_token, payload):
    url = f"https://graph.facebook.com/v{current_app.config['FB_API_VERSION']}/act_{ad_account_id}/campaigns"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()

