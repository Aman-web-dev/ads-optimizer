
# sample payload


# first Rule
{
  "name": "Rule 1",
  "evaluation_spec": {
    "type": "AND",
    "rules": [
      {
        "type": "EXPRESSION",
        "expression": "targeting_location.country == 'US'"
      },
      {
        "type": "EXPRESSION",
        "expression": "targeting_age_min <= 25"
      }
    ]
  },
  "execution_spec": {
    "type": "UPDATE",
    "update_spec": {
      "bid_amount": {
        "amount": 0.5
      }
    }
  }
}



# 2  complex rule 


{
  "name": "Rule 2",
  "evaluation_spec": {
    "type": "OR",
    "rules": [
      {
        "type": "EXPRESSION",
        "expression": "targeting_device.type == 'desktop'"
      },
      {
        "type": "EXPRESSION",
        "expression": "targeting_device.type == 'mobile'"
      },
      {
        "type": "EXPRESSION",
        "expression": "targeting_device.type == 'tablet'"
      }
    ]
  },
  "execution_spec": {
    "type": "UPDATE",
    "update_spec": {
      "daily_budget": {
        "amount": 100
      }
    }
  }
}


# Sample 3: Rule with Multiple Actions

{
  "name": "Rule 3",
  "evaluation_spec": {
    "type": "AND",
    "rules": [
      {
        "type": "EXPRESSION",
        "expression": "targeting_location.country == 'CA'"
      },
      {
        "type": "EXPRESSION",
        "expression": "targeting_age_min <= 30"
      }
    ]
  },
  "execution_spec": {
    "type": "UPDATE",
    "update_specs": [
      {
        "bid_amount": {
          "amount": 0.5
        }
      },
      {
        "daily_budget": {
          "amount": 50
        }
      }
    ]
  }
}










# Metadata Related Trigger Rules


# Metadata Creation Rule


payload = {
    "name": "Metadata Creation Example 1",
    "evaluation_spec": {
        "evaluation_type": "TRIGGER",
        "trigger": {
            "type": "METADATA_CREATION"
        },
        "filters": [
            {
                "field": "entity_type",
                "value": "AD",
                "operator": "EQUAL"
            },
            {
                "field": "campaign.objective",
                "value": ["APP_INSTALLS"],
                "operator": "IN"
            }
        ]
    },
    "execution_spec": {
        "execution_type": "PING_ENDPOINT"
    }
}





# Metadata Update Rule



payload = {
    "name": "Metadata Update Example 1",
    "evaluation_spec": {
        "evaluation_type": "TRIGGER",
        "trigger": {
            "type": "METADATA_UPDATE",
            "field": "daily_budget"
        },
        "filters": [
            {
                "field": "entity_type",
                "value": "ADSET",
                "operator": "EQUAL"
            }
        ]
    },
    "execution_spec": {
        "execution_type": "NOTIFICATION"
    }
}




# Insights Related Trigger Rules


 #   -Stats Milestone Rule



    payload = {
        "name": "Rule 1",
        "evaluation_spec": {
            "evaluation_type": "TRIGGER",
            "trigger": {
                "type": "STATS_MILESTONE",
                "field": "post_comment",
                "value": 1,
                "operator": "EQUAL"
            },
            "filters": [
                {
                    "field": "entity_type",
                    "value": "CAMPAIGN",
                    "operator": "EQUAL"
                },
                {
                    "field": "time_preset",
                    "value": "LIFETIME",
                    "operator": "EQUAL"
                }
            ]
        },
        "execution_spec": {
            "execution_type": "PING_ENDPOINT"
        }
    }





#  Stats Change Rule

payload = {
    "name": "Rule 1",
    "evaluation_spec": {
        "evaluation_type": "TRIGGER",
        "trigger": {
            "type": "STATS_CHANGE",
            "field": "cost_per_purchase_fb",
            "value": 1000,
            "operator": "GREATER_THAN"
        },
        "filters": [
            {
                "field": "entity_type",
                "value": "AD",
                "operator": "EQUAL"
            },
            {
                "field": "time_preset",
                "value": "LAST_3_DAYS",
                "operator": "EQUAL"
            },
            {
                "field": "reach",
                "value": 5000,
                "operator": "GREATER_THAN"
            }
        ]
    },
    "execution_spec": {
        "execution_type": "PAUSE"
    }
}





# Schedule Based Rules



payload = {
    "name": "Rule 1",
    "evaluation_spec": {
        # your evaluation spec here
    },
    "execution_spec": {
        # your execution spec here
    },
    "schedule_spec": {
        "schedule_type": "DAILY"
    }
}




## Schedule Spec


payload = {
    "name": "Rule 1",
    "schedule_spec": {
        # your schedule spec here
    },
    "evaluation_spec": {
        "evaluation_type": "SCHEDULE",
        "filters": [
            {
                "field": "time_preset",
                "value": "LAST_7_DAYS",
                "operator": "EQUAL"
            },
            {
                "field": "effective_status",
                "value": ["ACTIVE"],
                "operator": "IN"
            },
            {
                "field": "id",
                "value": [101, 102, 103],
                "operator": "IN"
            },
            {
                "field": "impressions",
                "value": 10000,
                "operator": "GREATER_THAN"
            }
        ]
    },
    "execution_spec": {
        # your execution spec here
    }
}


# Advanced Scheduling



payload = {
    "name": "Test Advanced Scheduling Rule",
    "schedule_spec": {
        "schedule_type": "CUSTOM",
        "schedule": [
            {
                "start_minute": 600
            }
        ]
    },
    "evaluation_spec": {
        # your evaluation spec here
    },
    "execution_spec": {
        # your execution spec here
    }
}

## Here's an example of a rule that runs every 30 minutes only on weekends. By omitting start_minute, we infer the rule to run as SEMI_HOURLY for the specified days.


payload = {
    "name": "Test Advanced Scheduling Rule",
    "schedule_spec": {
        "schedule_type": "CUSTOM",
        "schedule": [
            {
                "days": [0, 6]
            }
        ]
    },
    "evaluation_spec": {
        # your evaluation spec here
    },
    "execution_spec": {
        # your execution spec here
    }
}


## Here's an example of a rule that only runs on Wednesdays at 2 AM. By omitting end_minute, we infer that the rule only runs at one specific time instead of a range of times.


payload = {
    "name": "Test Advanced Scheduling Rule",
    "schedule_spec": {
        "schedule_type": "CUSTOM",
        "schedule": [
            {
                "start_minute": 120,
                "days": [3]
            }
        ]
    },
    "evaluation_spec": {
        # your evaluation spec here
    },
    "execution_spec": {
        # your execution spec here
    }
}


## Each individual schedule is calculated independently as an OR with the other schedules. Here's an example of a rule that runs all day on the weekdays, but only from 12-1PM on the weekends. By having an end_minute here, we now look at the range of time from the start_minute to end_minute.



payload = {
    "name": "Test Advanced Scheduling Rule",
    "schedule_spec": {
        "schedule_type": "CUSTOM",
        "schedule": [
            {
                "days": [1, 2, 3, 4, 5]
            },
            {
                "start_minute": 720,
                "end_minute": 780,
                "days": [0, 6]
            }
        ]
    },
    "evaluation_spec": {
        # your evaluation spec here
    },
    "execution_spec": {
        # your execution spec here
    }
}

