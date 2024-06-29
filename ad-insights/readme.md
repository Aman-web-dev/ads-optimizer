





# Example  of simple get insights usage:

To get the statistics of a campaign's last 7 day performance:



 <!-- # Replace with actual URL part: act_<AD_ACCOUNT_ID>, <CAMPAIGN_ID>, <ADSET_ID>, or <AD_ID>  -->
url = "act_<AD_ACCOUNT_ID>" 
params={
date_preset ="last_7d"
}
insights = get_facebook_insights(url,params)
print(insights)





# Levels
Aggregate results at a defined object level. This automatically deduplicates data.

params = {
    "level": "ad",
    "fields": "impressions,ad_id",
    "access_token": "ACCESS_TOKEN"
}

insights = get_facebook_insights("CAMPAIGN_ID", **params)
print(insights)






 
# Sorting
Sort results by providing the sort parameter with {fieldname}_descending or {fieldname}_ascending:




<!-- # Replace with actual URL part: act_<AD_ACCOUNT_ID>, <CAMPAIGN_ID>, <ADSET_ID>, or <AD_ID>  -->
url = "act_<AD_ACCOUNT_ID>"
params = {
    "sort": "reach_descending",
    "level": "ad",
    "fields": "reach"
}

insights = get_facebook_insights(url, **params)
print(insights)










# Ads Labels
    Stats for all labels whose names are identical. Aggregated into a single value at an ad object level. See the Ads Labels Reference for more information.

params = {
    "fields": "id,name,insights{unique_clicks,cpm,total_actions}",
    "level": "ad",
    "filtering": "[{\"field\":\"ad.adlabels\",\"operator\":\"ANY\", \"value\":[\"Label Name\"]}]",
    "time_range": {"since": "2015-03-01", "until": "2015-03-31"},
    "access_token": "ACCESS_TOKEN"
}

insights = get_facebook_insights("AD_OBJECT_ID", **params)
print(insights)















# Deleted and Archived Objects
To get the stats of all ARCHIVED ads in an ad account listed one by one:


params = {
    "level": "ad",
    "filtering": '[{"field":"ad.effective_status","operator":"IN","value":["ARCHIVED"]}]',
    "access_token": "<ACCESS_TOKEN>"
}

insights = get_facebook_insights("act_<AD_ACCOUNT_ID>", **params)
print(insights)






# Deleted Objects Insights
You can query insights on deleted objects if you have their IDs or by using the ad.effective_status filter.

params = {
    "fields": "ad_id,impressions",
    "date_preset": "lifetime",
    "level": "ad",
    "filtering": '[{"field":"ad.effective_status","operator":"IN","value":["DELETED"]}]',
    "access_token": "token",
    "appsecret_proof": "proof"
}

insights = get_facebook_insights("act_ID", **params)
print(insights)










# Insights API Breakdowns


You can group the Insights API results into different sets using breakdowns.

The Insights API can return several metrics that are estimated, in development, or both. Insights breakdown values are estimated. For more information, see Insights API, Estimated and Deprecated Metrics.


params = {
    "breakdowns": "age,gender",
    "fields": "impressions",
    "access_token": "<ACCESS_TOKEN>"
}

insights = get_facebook_insights("<AD_CAMPAIGN_ID>", **params)
print(insights)




