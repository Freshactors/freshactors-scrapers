"""
Microsoft Store Scraper — app details with rating windows, search & reviews with helpful votes (FreshActors / Apify)
Store: https://apify.com/freshactors/microsoft-store-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/microsoft-store-scraper").call(run_input={
    "mode": "details",
    "productIds": ["9NKSQGP7F2NH", "9NCBCSZSJRSB", "9WZDNCRFJ3TJ"],  # WhatsApp, Spotify, Netflix
})

for app in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(app["title"], app["rating"], app["rating30Days"])

# productIds = the 12-char Store ids starting with 9 (apps.microsoft.com/detail/{id} URLs work too).
# Details carry all-time + 7-day + 30-day rating windows (momentum signal Apple/Google don't expose).
# market/language localize everything (e.g. "market": "DE", "language": "de-de").
# Reviews mode returns text + helpfulPositive/helpfulNegative + deviceFamily, deep pagination.
