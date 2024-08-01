import requests
from flask import current_app
import json

def encode_payload(payload):
    for key, value in payload.items():
        if isinstance(value, (dict, list)):
            payload[key] = json.dumps(value)
    return payload

