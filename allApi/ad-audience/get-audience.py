import os
import requests

def get_custom_audience(CUSTOM_AUDIENCE_ID):
    """
    Get a custom audience from the Facebook Graph API

    Args:
        CUSTOM_AUDIENCE_ID (str): The ID of the custom audience

    Returns:
        dict: The custom audience data in JSON format
    """
    api_version = os.getenv('META_API_VERSION')
    url = f"https://graph.facebook.com/{api_version}/{CUSTOM_AUDIENCE_ID}"
    headers = {
        "Authorization": f"Bearer {os.getenv('META_ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()



def get_custom_audiences(ad_account_id):
    api_endpoint = f"https://graph.facebook.com/v13.0/act_{ad_account_id}/customaudiences"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    response = requests.get(api_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None






def get_saved_audiences(ad_account_id):
    api_endpoint = f"https://graph.facebook.com/v13.0/act_{ad_account_id}/saved_audiences"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    response = requests.get(api_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
    
    
    
    
    
def get_saved_audience(saved_audience_id):
    api_endpoint = f"https://graph.facebook.com/v13.0/{saved_audience_id}"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    response = requests.get(api_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None   