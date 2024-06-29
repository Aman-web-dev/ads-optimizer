

# Budgets

- daily_budget : The average amount you're willing to spend on an ad set or campaign each day. With Ads Manager, you’ll get roughly your daily budget’s worth of the result you optimized for. There may, however, be certain days when better opportunities are available. On those days, up to 25% more than your daily budget may be spent. For example, if your daily budget is $10, up to $12.50 may be spent.


- lifetime budget : The amount you're willing to spend over the entire run of an ad set or campaign. You won't be charged more than your lifetime budget for your ad set's results unless you change your delivery settings. If your ad set is running for five days and has a $250 lifetime budget, $50 may be spent on each of the first two days. On the third day, if lots of results are available, $75 may be spent. Then, if there aren't as many opportunities available, $25 may be spent on the fourth day and $50 on the fifth day.

params = {
    "name": "My First Adset",
    "daily_budget": 2000,
    "start_time": "2024-06-29T12:32:27-0700",
    "end_time": "2024-07-06T12:32:27-0700",
    "campaign_id": "<AD_CAMPAIGN_ID>",
    "bid_amount": 100,
    "billing_event": "LINK_CLICKS",
    "optimization_goal": "LINK_CLICKS",
    "targeting": {
        "facebook_positions": [
            "feed"
        ],
        "geo_locations": {
            "countries": [
                "US"
            ]
        }
    },
    "status": "PAUSED",
    "access_token": "<ACCESS_TOKEN>"
}

url= act_<AD_ACCOUNT_ID>
adset = create_adset_with_bidding(url,**params)
print(adset)





To set a lifetime budget of 200 dollars for a campaign setup to run for 10 days:



params = {
    "name": "My First Adset",
    "lifetime_budget": 20000,
    "start_time": "2024-06-29T12:32:27-0700",
    "end_time": "2024-07-09T12:32:27-0700",
    "campaign_id": "<AD_CAMPAIGN_ID>",
    "bid_amount": 100,
    "billing_event": "LINK_CLICKS",
    "optimization_goal": "LINK_CLICKS",
    "targeting": {
        "facebook_positions": [
            "feed"
        ],
        "geo_locations": {
            "countries": [
                "US"
            ]
        },
        "publisher_platforms": [
            "facebook",
            "audience_network"
        ]
    },
    "status": "PAUSED",
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding(<AD_ACCOUNT_ID>,**params)
print(adset)


# Bid Strategy


## To read bid_strategy from an ad set:

params = {
    "fields": "bid_strategy",
    "access_token": "<ACCESS_TOKEN>"
}

adset = get_facebook_adset_bid_strategy("<VERSION>", "<AD_SET_ID>", **params)
print(adset)




## To update an ad set's bid strategy to LOWEST_COST_WITH_BID_CAP with a bid cap of $3 USD:


params = {
    "bid_strategy": "LOWEST_COST_WITH_BID_CAP",
    "bid_amount": 300,
    "access_token": "<ACCESS_TOKEN>"
}

adset = update_bid_strategy("<AD_SET_ID>", **params)
print(adset)


# Cost Cap
Cost cap is a cost-based bid feature that enables advertisers to express and optimize against the actual cost (CPA/CPI) of conversions. This feature allows advertisers to get the most results possible while we strive to meet their desired cost, allowing them to maximize cost efficiency, reducing complexities of managing bids, and helping advertisers scale more profitably and confidently. Note: Adherence to cost cap limits is not guaranteed.



## For example, to use a cost cap at the ad campaign level:

params = {
    "name": "L3 With Lifetime Budget",
    "objective": "LINK_CLICKS",
    "lifetime_budget": 100000,
    "bid_strategy": "COST_CAP",
    "access_token": "ACCESS_TOKEN"
}

campaign = create_facebook_campaign("<VERSION>", "<AD_ACCOUNT_ID>", **params)
print(campaign)



## To set a cost cap at the ad set level

params = {
    "name": "My Ad Set",
    "optimization_goal": "CONVERSIONS",
    "billing_event": "IMPRESSIONS",
    "bid_strategy": "COST_CAP",
    "bid_amount": 200,
    "daily_budget": 1000,
    "campaign_id": "<CAMPAIGN_ID>",
    "targeting": {"geo_locations": {"countries": ["US"]}},
    "status": "PAUSED",
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding("act_<AD_ACCOUNT_ID>", **params)
print(adset)






# Minimum Return on Advertiser Spend (Min ROAS) Bidding
This is a specific bidding option for value optimization. As such, you must already be eligible for value optimization, which has several prerequisites:


## Create new minimum bidding ad set
The API call below creates a min ROAS bidding ad set, with campaign objective = “website conversion” and ROAS floor = 1.0 (or 100%).



params = {
    "name": "minRoasBiddingDemo",
    "daily_budget": 2000,
    "optimization_goal": "VALUE",
    "promoted_object": {"pixel_id": "<PIXEL_ID>", "custom_event_type": "PURCHASE"},
    "targeting": {"geo_locations": {"countries": ["US"]}},
    "campaign_id": "<CAMPAIGN_ID>",
    "status": "PAUSED",
    "start_time": "2018-12-10T12:45:26-0700",
    "bid_strategy": "LOWEST_COST_WITH_MIN_ROAS",
    "bid_constraints": {"roas_average_floor": 10000},
    "billing_event": "IMPRESSIONS",
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding("act_<AD_ACCOUNT_ID>", **params)
print(adset)






# Billing Events

billing_event defines events you want to pay for such as impressions, clicks, or various actions. Billing depends on the size of your audience and your budget.



For example, to optimize for POST_ENGAGEMENT and pay per IMPRESSIONS:


params = {
    "name": "My First Adset",
    "lifetime_budget": 20000,
    "start_time": "2024-06-29T12:48:39-0700",
    "end_time": "2024-07-09T12:48:39-0700",
    "campaign_id": "<AD_CAMPAIGN_ID>",
    "bid_amount": 500,
    "billing_event": "IMPRESSIONS",
    "optimization_goal": "POST_ENGAGEMENT",
    "targeting": {
        "facebook_positions": ["feed"],
        "geo_locations": {
            "countries": ["US"],
            "regions": [{"key": "4081"}],
            "cities": [{"key": 777934, "radius": 10, "distance_unit": "mile"}]
        },
        "genders": [1],
        "age_max": 24,
        "age_min": 20,
        "behaviors": [{"id": 6002714895372, "name": "All travelers"}],
        "life_events": [{"id": 6002714398172, "name": "Newlywed (1 year)"}],
        "publisher_platforms": ["facebook"],
        "device_platforms": ["desktop"]
    },
    "status": "PAUSED",
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding("act_<AD_ACCOUNT_ID>", **params)
print(adset)













# Pacing and Scheduling

Determines how your ads budget is spent over time. It provides uniform competition at Facebook's ads auction across all advertisers each day and automatically allocates budgets to different ads. Pacing functions the same way for ads created with the API as it does with Facebook tools, see Ads Help Center, Delivery and Pacing.



## Accelerated delivery removes all pacing adjustments from your bid. We enter your ad into all eligible auctions at its full maximum bid. You can achieve maximum delivery with a specified cost and budget. This results in delivery that is not smooth throughout the day; your ad set's budget may be exhausted before the end of the day. To create an ad set with accelerated delivery:

params = {
    "name": "Ad Set without pacing",
    "optimization_goal": "REACH",
    "billing_event": "IMPRESSIONS",
    "pacing_type": ["no_pacing"],
    "bid_amount": 2,
    "daily_budget": 1000,
    "campaign_id": "<CAMPAIGN_ID>",
    "targeting": {"geo_locations": {"countries": ["US"]}},
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding( "act_<AD_ACCOUNT_ID>", **params)
print(adset)



## Ad Scheduling


Specify days in a week and hours in a day when your ad set runs in adset_schedule. Your schedule applies to all ad groups under the ad set. See Ad Scheduling, Blog. adset_schedule is an array of JSON objects.


params = {
    "name": "Ad Set with scheduling",
    "optimization_goal": "REACH",
    "billing_event": "IMPRESSIONS",
    "pacing_type": ["day_parting"],
    "lifetime_budget": 100000,
    "end_time": "2018-02-06T04:45:17+0000",
    "adset_schedule": [
        {
            "start_minute": 540,
            "end_minute": 720,
            "days": [1, 2, 3, 4, 5]
        }
    ],
    "bid_amount": 2,
    "campaign_id": "<CAMPAIGN_ID>",
    "targeting": {"geo_locations": {"countries": ["US"]}},
    "access_token": "<ACCESS_TOKEN>"
}

adset = create_adset_with_bidding("act_<AD_ACCOUNT_ID>", **params)
print(adset)