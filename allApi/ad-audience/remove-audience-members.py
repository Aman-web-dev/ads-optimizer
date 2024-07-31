import os
import requests

def delete_users_from_custom_audience(audience_id, payload):
    url = f"https://graph.facebook.com/{os.getenv('META_API_VERSION')}/{audience_id}/users"
    data = {
        'payload': payload,
        'access_token': os.getenv('META_ACCESS_TOKEN')
    }
    response = requests.delete(url, data=data)
    return response.json()