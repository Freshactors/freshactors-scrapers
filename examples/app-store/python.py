"""
App Store Scraper — iOS app details, search & reviews (FreshActors / Apify)
Store: https://apify.com/freshactors/app-store-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/app-store-scraper").call(run_input={
    "mode": "details",
    "appIds": ["389801252"],   # Instagram — the number in the App Store URL
    "country": "us",
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# Other modes:
#   Keyword search:  {"mode": "search",  "searchTerms": ["photo editor"], "country": "us", "maxSearchResults": 20}
#   Customer reviews:{"mode": "reviews", "appIds": ["389801252"], "country": "us", "maxReviewsPerApp": 100, "reviewsSort": "mostRecent"}
