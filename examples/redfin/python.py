"""
Redfin Scraper — US real-estate listings & sold homes (FreshActors / Apify)
Store: https://apify.com/freshactors/redfin-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/redfin-scraper").call(run_input={
    "redfinUrls": ["https://www.redfin.com/city/30818/TX/Austin"],
    "listingType": "forSale",
    "maxListings": 50,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# Pass any Redfin city / zip / neighborhood search URL. The region is read from the URL.
#   Recently sold: {"redfinUrls": ["https://www.redfin.com/zipcode/78701"], "listingType": "sold", "maxListings": 50}
