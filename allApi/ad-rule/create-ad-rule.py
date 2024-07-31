import requests

def create_ad_rule(name, evaluation_spec, execution_spec, access_token, version, ad_account_id):
    url = f"https://graph.facebook.com/{version}/{ad_account_id}/adrules_library"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "name": name,
        "evaluation_spec": evaluation_spec,
        "execution_spec": execution_spec
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


