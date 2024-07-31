import requests
import os

def create_adset_with_bidding( **params):
    access_token= os.environ("META_ACCESS_TOKEN")
    api_version=os.environ("META_API_VERISON")
    url = f"https://graph.facebook.com/{api_version}/{url}/adsets"
    params_dict = {
        "access_token": access_token
    }
    params_dict.update(params)
    response = requests.post(url, params=params_dict)
    return response.json()