import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adaccount import AdAccount

from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.objects import AdSet, TargetingSpecsField
from facebookads import FacebookSession
from facebookads import FacebookAdsApi

session = FacebookSession(
    259842962,
    'd3811777417e066669fb968fa9206985',
    'EAASGV9QgOGQBAEwj3BUypXBr6XDtZAEEk6zNhaNd6VTu2agjs9AlaToK21BAdKZCsZC6KtwcBUQC3WRnKWe0ZAU3QEZAQM87tAnFyKw884maafrZCZACg7hEKQVh3lpw7YwOiWVe3CBZBzdjIlsfZCRd9lGrNzgPgYeQZD',
)

api = FacebookAdsApi(session)

def main():
    FacebookAdsApi.set_default_api(api)
    print("Hello world")
    # facebook = Face
    # campaign = create_campaign()

    # campaign = read_campaign(6048231054913)
    # print(campaign)
    # ad_set = create_adset(campaign.get_id())
    # ad_set = read_adset(ad_set.get_id())
    audience = get_customer_audicence()
    estimate = reach_esitmate()
    # for iter in estimate:
    #     print(iter._json)


    # print(estimate)

def create_campaign():
    campaign = Campaign(parent_id='act_259842962')
    campaign.update({
        Campaign.Field.name: 'My Campaign',
        Campaign.Field.objective: Campaign.Objective.link_clicks,
    })
    campaign.remote_create(params={
        'status': Campaign.Status.paused,
    })
    print(campaign)
    return campaign


def get_cities(name):
    params = {
        'q': name,
        'type': 'adgeolocation',
        'location_types': ['city'],
    }

    resp = TargetingSearch.search(params=params)
    print(resp)
    return resp

def get_customer_audicence():
    account = AdAccount('act_259842962')
    resp = account.get_custom_audiences(fields=["name"])
    print(resp)
    return resp

def create_adset(campaign_id):
    adset = AdSet(parent_id='act_259842962')
    adset.update({
        AdSet.Field.name: 'My Ad Set',
        AdSet.Field.campaign_id: campaign_id,
        AdSet.Field.daily_budget: 10000,
        AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
        AdSet.Field.bid_amount: 2,
        AdSet.Field.targeting: {
            Targeting.Field.geo_locations: {
                'countries': ['IN'],
            },
            Targeting.Field.age_min: 20,
            Targeting.Field.age_max: 24
        },
        AdSet.Field.status: AdSet.Status.paused,
    })
    adset.remote_create()
    return adset


def read_campaign(id):
    campaign = Campaign(id)
    campaign.remote_read(fields=[Campaign.Field.name])
    print(campaign)
    return campaign


def read_adset(id):
    adset = AdSet(id)
    adset.remote_read(fields=[AdSet.Field.account_id,AdSet.Field.adlabels,AdSet.Field.adset_schedule,AdSet.Field.bid_amount,AdSet.Field.bid_info,AdSet.Field.billing_event,AdSet.Field.budget_remaining,AdSet.Field.campaign,AdSet.Field.campaign_id,AdSet.Field.configured_status,AdSet.Field.created_time,AdSet.Field.creative_sequence,AdSet.Field.daily_budget,AdSet.Field.effective_status,AdSet.Field.end_time,AdSet.Field.frequency_cap,AdSet.Field.frequency_cap_reset_period,AdSet.Field.frequency_control_specs,AdSet.Field.id,AdSet.Field.is_autobid,AdSet.Field.lifetime_budget,AdSet.Field.lifetime_frequency_cap,AdSet.Field.lifetime_imps,AdSet.Field.name,AdSet.Field.optimization_goal,AdSet.Field.pacing_type,AdSet.Field.promoted_object,AdSet.Field.recommendations,AdSet.Field.rf_prediction_id,AdSet.Field.rtb_flag,AdSet.Field.start_time,AdSet.Field.status,AdSet.Field.targeting,AdSet.Field.updated_time])
    print(adset)
    return adset


def read_targeting(id):
    adset = AdSet(id)
    adset.remote_read(fields=[AdSet.Field.account_id,AdSet.Field.adlabels,AdSet.Field.adset_schedule,AdSet.Field.bid_amount,AdSet.Field.bid_info,AdSet.Field.billing_event,AdSet.Field.budget_remaining,AdSet.Field.campaign,AdSet.Field.campaign_id,AdSet.Field.configured_status,AdSet.Field.created_time,AdSet.Field.creative_sequence,AdSet.Field.daily_budget,AdSet.Field.effective_status,AdSet.Field.end_time,AdSet.Field.frequency_cap,AdSet.Field.frequency_cap_reset_period,AdSet.Field.frequency_control_specs,AdSet.Field.id,AdSet.Field.is_autobid,AdSet.Field.lifetime_budget,AdSet.Field.lifetime_frequency_cap,AdSet.Field.lifetime_imps,AdSet.Field.name,AdSet.Field.optimization_goal,AdSet.Field.pacing_type,AdSet.Field.promoted_object,AdSet.Field.recommendations,AdSet.Field.rf_prediction_id,AdSet.Field.rtb_flag,AdSet.Field.start_time,AdSet.Field.status,AdSet.Field.targeting,AdSet.Field.updated_time])
    print(adset)
    return adset


def reach_esitmate():
    cities = get_cities("Bangalore")
    targeting_spec_city = []
    for city in cities:
        targeting_spec_city.append(
            {
                'key': city._data['key'],
                'radius': 12,
                'distance_unit': 'mile'
            }
        )

    account = AdAccount('act_259842962')
    targeting_spec = {
        'geo_locations': {
            'cities': targeting_spec_city
        },
        'age_min': 20,
        'age_max': 40,
        'custom_audiences': [6037977332713]  # custom audience id
    }
    params = {
        'optimize_for': AdSet.OptimizationGoal.offsite_conversions,
        'targeting_spec': targeting_spec,
    }
    reach_estimate = account.get_reach_estimate(params=params)
    print(reach_estimate)
    return reach_estimate



if __name__ == "__main__":
    main()
