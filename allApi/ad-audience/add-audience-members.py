import os
import requests
import json

def add_users_to_custom_audience(audience_id, session, payload):
    url = f"https://graph.facebook.com/{os.getenv('META_API_VERSION')}/{audience_id}/users"
    data = {
        'session': session,
        'payload': payload,
        'access_token': os.getenv('META_ACCESS_TOKEN')
    }
    response = requests.post(url, json=data)
    return response.json()




# Example usage
# audience_id = '<AUDIENCE_ID>'
# session = {
#     "session_id": 9778993,
#     "batch_seq": 10,
#     "last_batch_flag": True,
#     "estimated_num_total": 99996
# }
# payload = {
#     "schema": "EMAIL_SHA256",
#     "data": [
#         "<HASHED_DATA>",
#         "<HASHED_DATA>",
#         "<HASHED_DATA>"
#     ]
# }





#payload example {
#   "schema": [
#     "FN",
#     "LN",
#     "EMAIL"
#   ],
#   "data": [
#     [
#       "1f3870be274f6c49b3e31a0c6728957f",  # Hashed first name
#       "8ad8757baa8564dc136c1e07507f4a98",  # Hashed last name
#       "1c383cd30b7c298ab50293adfecb7b18"   # Hashed email
#     ],
#     [
#       "98f13708210194c475687be6106a3b84",  # Hashed first name
#       "8f14e45fceea167a5a36dedd4bea2543",  # Hashed last name
#       "c4ca4238a0b923820dcc509a6f75849b"   # Hashed email
#     ]
#   ]
# }