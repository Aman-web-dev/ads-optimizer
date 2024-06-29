import json

def create_audience_rule(event_source, retention_days, filters, aggregation=None):
    """
    Create an audience rule for Facebook Marketing API.
    
    :param event_source: Dict containing 'type' and 'id' for the event source
    :param retention_days: Number of days to retain the audience
    :param filters: List of filter dicts, each containing 'field', 'operator', and 'value'
    :param aggregation: Optional dict for aggregation, containing 'type', 'operator', and 'value'
    :return: JSON string of the audience rule
    """
    rule = {
        "inclusions": {
            "operator": "and",
            "rules": [
                {
                    "event_sources": [event_source],
                    "retention_seconds": retention_days * 86400,  # Convert days to seconds
                    "filter": {
                        "operator": "and",
                        "filters": filters
                    }
                }
            ]
        }
    }
    
    if aggregation:
        rule["inclusions"]["rules"][0]["aggregation"] = aggregation
    
    return json.dumps(rule, indent=2)


# URL-based rule (matching URLs containing "shoes"):

# payload1 = create_audience_rule(
#     event_source={"type": "pixel", "id": "123456789"},
#     retention_days=30,
#     filters=[
#         {
#             "field": "url",
#             "operator": "i_contains",
#             "value": "shoes"
#         }
#     ]
# )
# print("Payload 1 (URL-based):")
# print(payload1)



# Event-based rule (matching ViewContent events with price >= 100):

# payload2 = create_audience_rule(
#     event_source={"type": "pixel", "id": "123456789"},
#     retention_days=30,
#     filters=[
#         {
#             "field": "event",
#             "operator": "eq",
#             "value": "ViewContent"
#         },
#         {
#             "field": "price",
#             "operator": "gte",
#             "value": "100"
#         }
#     ]
# )
# print("\nPayload 2 (Event-based):")
# print(payload2)



# Complex rule with multiple filters and aggregation:

# payload3 = create_audience_rule(
#     event_source={"type": "pixel", "id": "123456789"},
#     retention_days=60,
#     filters=[
#         {
#             "field": "event",
#             "operator": "eq",
#             "value": "Purchase"
#         },
#         {
#             "field": "value",
#             "operator": "gte",
#             "value": "50"
#         },
#         {
#             "field": "currency",
#             "operator": "eq",
#             "value": "USD"
#         }
#     ],
#     aggregation={
#         "type": "count",
#         "operator": ">",
#         "value": 2
#     }
# )
# print("\nPayload 3 (Complex rule with aggregation):")
# print(payload3)


# Mobile app custom audience:

# payload4 = create_audience_rule(
#     event_source={"type": "app", "id": "com.example.app"},
#     retention_days=90,
#     filters=[
#         {
#             "field": "event",
#             "operator": "eq",
#             "value": "fb_mobile_purchase"
#         },
#         {
#             "field": "_valueToSum",
#             "operator": "gte",
#             "value": "100"
#         }
#     ],
#     aggregation={
#         "type": "sum",
#         "operator": ">",
#         "value": 500
#     }
# )
# print("\nPayload 4 (Mobile app custom audience):")
# print(payload4)