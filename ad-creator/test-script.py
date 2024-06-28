import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_create_campaign():
    url = f'{BASE_URL}/create_campaign'
    payload = {
        'campaign_name': 'My Campaign',
        'buying_type': 'AUCTION',
        'objective': 'OUTCOME_APP_PROMOTION',
        'status': 'PAUSED',
        'special_ad_categories':[]
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print('Create Campaign Response:', response.json())

def test_create_ad_creative():
    url = f'{BASE_URL}/create_ad_creative'
    payload = {
        'ad_name': 'My Creative',
        # 'object_id': 'your_page_id',  # Replace with actual page id
        'title': 'My Page Like Ad',
        'body': 'Like My Page',
        'image_url': 'https://images.unsplash.com/photo-1498462440456-0dba182e775b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BsYXNofGVufDB8fDB8fHww'
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print('Create Ad Creative Response:', response.json())

def test_create_ad():
    url = f'{BASE_URL}/create_ad'
    payload = {
        'ad_name': 'My Ad',
        'ad_set_id': 'your_ad_set_id',  # Replace with actual ad set id
        'creative_id': 'your_creative_id'  # Replace with actual creative id
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print('Create Ad Response:', response.json())

def test_get_ad_previews():
    url = f'{BASE_URL}/get_ad_previews'
    payload = {
        'ad_id': 'your_ad_id'  # Replace with actual ad id
    }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print('Get Ad Previews Response:', response.json())

if __name__ == '__main__':
    # test_create_campaign()
    test_create_ad_creative()
    # test_create_ad()
    # test_get_ad_previews()
