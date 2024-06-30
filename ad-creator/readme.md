# Create Campaign



## Campaign with basic settings

payload = {
    'name': 'My First Campaign',
    'objective': 'LINK_CLICKS',
    'status': 'ACTIVE',
    'special_ad_categories': []
}


create_campaign(payload)



## Campaign with custom audience

payload = {
    'name': 'My Custom Audience Campaign',
    'objective': 'CONVERSIONS',
    'status': 'ACTIVE',
    'special_ad_categories': [],
    'audience': {
        'id': '1234567890',
        'type': 'CUSTOM_AUDIENCE'
    }
}

create_campaign(payload)


## Campaign with lookalike audience

payload = {
    'name': 'My Lookalike Audience Campaign',
    'objective': 'CONVERSIONS',
    'status': 'ACTIVE',
    'special_ad_categories': [],
    'audience': {
        'id': '1234567890',
        'type': 'LOOKALIKE_AUDIENCE',
        'source_audience_id': '1234567890'
    }
}

create_campaign(payload)


## Campaign with budget and schedule

payload = {
    'name': 'My Budgeted Campaign',
    'objective': 'LINK_CLICKS',
    'status': 'ACTIVE',
    'special_ad_categories': [],
    'budget': {
        'amount': 100,
        'currency': 'USD',
        'start_time': '2023-03-01T00:00:00+0000',
        'end_time': '2023-03-31T00:00:00+0000'
    }
}

create_campaign(payload)

## Campaign with targeting options

payload = {
    'name': 'My Targeted Campaign',
    'objective': 'CONVERSIONS',
    'status': 'ACTIVE',
    'special_ad_categories': [],
    'targeting': {
        'geo_locations': {
            'countries': ['US', 'CA']
        },
        'languages': ['en_US', 'fr_CA'],
        'platforms': ['facebook', 'instagram']
    }
}


create_campaign(payload)


# Create Ad Set


## Sample Payload 1: Basic Ad Set

payload = {
    'name': 'My First Ad Set',
    'campaign_id': '1234567890',
    'daily_budget': 500,
    'start_time': '2024-05-06T04:45:29+0000',
    'end_time': '2024-06-06T04:45:29+0000',
    'billing_event': 'THRUPLAY',
    'optimization_goal': 'THRUPLAY',
    'bid_amount': 100,
    'targeting': {
        "device_platforms": ["mobile"],
        "geo_locations": {"countries": ["US"]},
        "publisher_platforms": ["facebook"]
    },
    'status': 'PAUSED'
}

## Sample Payload 2: Ad Set with Custom Audience

payload = {
    'name': 'My Custom Audience Ad Set',
    'campaign_id': '1234567890',
    'daily_budget': 500,
    'start_time': '2024-05-06T04:45:29+0000',
    'end_time': '2024-06-06T04:45:29+0000',
    'billing_event': 'THRUPLAY',
    'optimization_goal': 'THRUPLAY',
    'bid_amount': 100,
    'targeting': {
        "device_platforms": ["mobile"],
        "geo_locations": {"countries": ["US"]},
        "publisher_platforms": ["facebook"],
        "custom_audiences": [
            {
                "audience_id": "1234567890",
                "audience_type": "CUSTOM_AUDIENCE"
            }
        ]
    },
    'status': 'PAUSED'
}

## Sample Payload 3: Ad Set with Lookalike Audience

payload = {
    'name': 'My Lookalike Audience Ad Set',
    'campaign_id': '1234567890',
    'daily_budget': 500,
    'start_time': '2024-05-06T04:45:29+0000',
    'end_time': '2024-06-06T04:45:29+0000',
    'billing_event': 'THRUPLAY',
    'optimization_goal': 'THRUPLAY',
    'bid_amount': 100,
    'targeting': {
        "device_platforms": ["mobile"],
        "geo_locations": {"countries": ["US"]},
        "publisher_platforms": ["facebook"],
        "lookalike_audiences": [
            {
                "audience_id": "1234567890",
                "audience_type": "LOOKALIKE_AUDIENCE",
                "source_audience_id": "1234567890"
            }
        ]
    },
    'status': 'PAUSED'
}





# Create Adcreative


## Sample Payload 1: Basic Ad Creative
payload = {
    'name': 'Sample Creative',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'link_data': {
            'link': 'https://www.example.com',
            'message': 'Check out this link!'
        }
    },
    'access_token': 'ACCESS_TOKEN'
}

## Sample Payload 2: Ad Creative with Image
payload = {
    'name': 'Sample Creative with Image',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'image_data': {
            'image_url': 'https://www.example.com/image.jpg',
            'image_width': 800,
            'image_height': 600
        }
    },
    'access_token': 'ACCESS_TOKEN'
}

## Sample Payload 3: Ad Creative with Video
payload = {
    'name': 'Sample Creative with Video',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'video_data': {
            'video_id': 'VIDEO_ID',
            'video_url': 'https://www.example.com/video.mp4'
        }
    },
    'access_token': 'ACCESS_TOKEN'
}

## Sample Payload 4: Ad Creative with Carousel
payload = {
    'name': 'Sample Creative with Carousel',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'carousel_data': {
            'carousel_items': [
                {
                    'image_url': 'https://www.example.com/image1.jpg',
                    'title': 'Item 1',
                    'description': 'This is item 1'
                },
                {
                    'image_url': 'https://www.example.com/image2.jpg',
                    'title': 'Item 2',
                    'description': 'This is item 2'
                }
            ]
        }
    },
    'access_token': 'ACCESS_TOKEN'
}



# Create ad




payload1 = {
    'name': 'Ad Creative 1',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'link_data': {
            'call_to_action': {
                'type': 'INSTALL_MOBILE_APP',
                'value': {
                    'link': 'https://itunes.apple.com/us/app/apple-store/id1234567890'
                }
            },
            'image_hash': 'image_hash_1',
            'link': 'https://itunes.apple.com/us/app/apple-store/id1234567890',
            'message': 'Try it out'
        }
    }
}

payload2 = {
    'name': 'Ad Creative 2',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'link_data': {
            'call_to_action': {
                'type': 'INSTALL_MOBILE_APP',
                'value': {
                    'link': 'https://play.google.com/store/apps/details?id=com.example.app'
                }
            },
            'image_hash': 'image_hash_2',
            'link': 'https://play.google.com/store/apps/details?id=com.example.app',
            'message': 'Try it out'
        }
    }
}

payload3 = {
    'name': 'Ad Creative 3',
    'object_story_spec': {
        'page_id': 'PAGE_ID',
        'video_data': {
            'call_to_action': {
                'type': 'INSTALL_MOBILE_APP',
                'value': {
                    'link': 'https://itunes.apple.com/us/app/apple-store/id1234567890'
                }
            },
            'image_url': 'https://example.com/thumbnail.jpg',
            'video_id': 'video_id_1'
        }
    }
}