import requests
import os 
from dotenv import load_dotenv

def create_ad_set(payload):
    
    load_dotenv()
    
    ad_account_id=os.environ('META_ACC_ID')
    api_version=os.environ("META_API_VERISON")
    
    url = f'https://graph.facebook.com/v{api_version}/act_{ad_account_id}/adsets'
    
    response = requests.post(url, data=payload)
    
    return response.json()



