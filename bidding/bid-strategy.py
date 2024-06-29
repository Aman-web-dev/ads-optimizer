import requests
import os

def update_bid_strategy(ad_set_id, **params):
    access_token = os.environ["META_ACCESS_TOKEN"]
    api_version = os.environ["META_API_VERSION"]
    url = f"https://graph.facebook.com/{api_version}/{ad_set_id}"
    
    params_dict = {
        "access_token": access_token
    }
    params_dict.update(params)
    
    response = requests.post(url, data=params_dict)
    return response.json()


def get_facebook_adset_bid_strategy(ad_set_id):
    access_token = os.environ["META_ACCESS_TOKEN"]
    api_version = os.environ["META_API_VERSION"]
    url = f"https://graph.facebook.com/{api_version}/{ad_set_id}"
    
    params = {
        "fields": "bid_strategy",
        "access_token": access_token
    }
    
    response = requests.get(url, params=params)
    return response.json()