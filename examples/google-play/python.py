"""
Google Play Scraper — app details, reviews & search (FreshActors / Apify)
Store: https://apify.com/freshactors/google-play-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/google-play-scraper").call(run_input={
    "mode": "details",
    "appIds": ["com.spotify.music"],   # the id= part of the Play Store URL
    "country": "us",
    "lang": "en",
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# Other modes:
#   Customer reviews:{"mode": "reviews", "appIds": ["com.spotify.music"], "maxReviewsPerApp": 100, "reviewsSort": "newest"}
#   Keyword search:  {"mode": "search",  "searchTerms": ["podcast"], "maxSearchResults": 20}
