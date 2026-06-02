"""
Shopify App Store Scraper — app details, reviews & discovery (FreshActors / Apify)
Store: https://apify.com/freshactors/shopify-app-store-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/shopify-app-store-scraper").call(run_input={
    "mode": "details",
    "appHandles": ["klaviyo-email-marketing"],   # the slug in the apps.shopify.com URL
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# Other modes:
#   App reviews:   {"mode": "reviews",  "appHandles": ["klaviyo-email-marketing"], "maxReviewsPerApp": 100}
#   Discover apps: {"mode": "discover", "query": "email", "maxApps": 20}
