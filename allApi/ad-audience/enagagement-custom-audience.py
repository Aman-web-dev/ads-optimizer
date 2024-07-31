import urllib.parse
import urllib.request
import json
import os

def create_engagement_custom_audience(access_token, ad_account_id, page_id, audience_name, retention_seconds=31536000):
    """
    Creates an engagement custom audience based on people who engaged with your Facebook Page.

    Args:
        access_token (str): Facebook access token.
        ad_account_id (str): Facebook Ad Account ID.
        page_id (str): Facebook Page ID.
        audience_name (str): Name for the custom audience.
        retention_seconds (int): Retention period in seconds. Defaults to 1 year.

    Returns:
        None: This function doesn't return anything.
    """
    endpoint = f"/act_{ad_account_id}/customaudiences"
    base_url = "https://graph.facebook.com/v20.0"
    url = urllib.parse.urljoin(base_url, endpoint)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    audience_params = {
        "name": audience_name,
        "rule": {
            "inclusions": {
                "operator": "or",
                "rules": [
                    {
                        "event_sources": [
                            {
                                "id": page_id,
                                "type": "page"
                            }
                        ],
                        "retention_seconds": retention_seconds,
                        "filter": {
                            "operator": "and",
                            "filters": [
                                {
                                    "field": "event",
                                    "operator": "eq",
                                    "value": "page_engaged"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "prefill": 1
    }

    data = json.dumps(audience_params).encode("utf-8")

    try:
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            print(f"Request sent successfully: {response.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error making request: {e}")

# Example usage
access_token = "<YOUR_ACCESS_TOKEN>"
ad_account_id = "<YOUR_AD_ACCOUNT_ID>"
page_id = "<YOUR_PAGE_ID>"
audience_name = "My Test Engagement Custom Audience"
create_engagement_custom_audience(access_token, ad_account_id, page_id, audience_name)
