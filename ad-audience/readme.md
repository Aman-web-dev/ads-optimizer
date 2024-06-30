# Custom Audience


## using custom audience ID 
Endpoint: GET /{CUSTOM_AUDIENCE_ID}

custom_audience_id = "1234567890"
custom_audience_data = get_custom_audience(custom_audience_id)
print(custom_audience_data)




## using custom ad_account_id

Endpoint: GET /act_{AD_ACCOUNT_ID}/customaudiences

ad_account_id = "1234567890"
custom_audiences = get_custom_audiences(ad_account_id)
if custom_audiences:
    print(custom_audiences)
else:
    print("Error retrieving custom audiences")





Endpoint: GET /act_{AD_ACCOUNT_ID}/saved_audiences    

ad_account_id = "1234567890"
saved_audiences = get_saved_audiences(ad_account_id)
if saved_audiences:
    print(saved_audiences)
else:
    print("Error retrieving saved audiences")









## Saved Audiences
Endpoint: GET /{SAVED_AUDIENCE_ID}



saved_audience_id = "1234567890"
saved_audience = get_saved_audience(saved_audience_id)
if saved_audience:
    print(saved_audience)
else:
    print("Error retrieving saved audience")






    