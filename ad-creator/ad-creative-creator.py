import requests
import os

def create_ad_creative(payload):
    ad_account_id=os.environ()
    
    
    url = f'https://graph.facebook.com/v20.0/act_{ad_account_id}/adcreatives'
  
    response = requests.post(url, json=payload)
    return response.json()