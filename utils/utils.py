import requests
from flask import current_app, jsonify
import json

def encode_payload(payload):
    for key, value in payload.items():
        if isinstance(value, (dict, list)):
            payload[key] = json.dumps(value)
    return payload

def handle_error(e, message='An error occurred'):
    if isinstance(e, requests.exceptions.HTTPError):
        return jsonify({'error': f'HTTP error occurred: {e}'}), 500
    else:
        return jsonify({'error': message, 'details': str(e)}), 500