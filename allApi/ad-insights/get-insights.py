import requests
import os

def get_facebook_insights( url, **params):
    
    
    access_token= os.environ("META_ACCESS_TOKEN")
    api_version=os.environ("META_API_VERISON")
    
    url = f"https://graph.facebook.com/{api_version}/{url}/insights"
    params_dict = {
        "access_token": access_token
    }
    params_dict.update(params)
    response = requests.get(url, params=params_dict)
    return response.json()