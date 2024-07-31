from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def create_ad(payload):
    api_version = os.getenv('META_API_VERSION')
    ad_account_id = os.getenv('META_ACC_ID')
    
    url = f'https://graph.facebook.com/{api_version}/act_{ad_account_id}/ads'
    
    response = requests.post(url, data=payload)
    
    return response.json()

