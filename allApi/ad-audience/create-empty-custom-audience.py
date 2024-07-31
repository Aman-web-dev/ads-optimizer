import os
import requests

def create_empty_custom_audience(name, subtype, description, customer_file_source):
    url = f"https://graph.facebook.com/{os.getenv('META_API_VERSION')}/act_{os.getenv('META_ACC_ID')}/customaudiences"
    payload = {
        'name': name,
        'subtype': subtype,
        'description': description,
        'customer_file_source': customer_file_source,
        'access_token': os.getenv('META_ACCESS_TOKEN')
    }
    response = requests.post(url, data=payload)
    return response.json()





