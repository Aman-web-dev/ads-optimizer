import requests

def fetch_facebook_ads(search_terms, ad_type, ad_reached_countries, access_token, api_version):
    url = f"https://graph.facebook.com/{api_version}/ads_archive"
    params = {
        'search_terms': search_terms,
        'ad_type': ad_type,
        'ad_reached_countries': ad_reached_countries,
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

# Example usage
search_terms = 'california'
ad_type = 'POLITICAL_AND_ISSUE_ADS'
ad_reached_countries = ['US']
access_token = 'EAAOE6F6rmLQBO2uXXJYsjkBpnJtxCNFSZBRc33WAB7ZCHJXF9rZAOs5zwo00IERoryoPRuleSKZC7QGJo5OZCZC7rMKvG5ZAJGTnSZB4c8KEPhCSH1zPBkyin9Pp7UMFCy527R2JjrTuwnmwsqk7ZAJhs8k6GZC8psDlIg2WDC7ZCZBdlzZA3RMVROcOf6nZAsuxed2exWTgrk2jZBP'
api_version = 'v20.0'

ads_data = fetch_facebook_ads(search_terms, ad_type, ad_reached_countries, access_token, api_version)
print(ads_data)
