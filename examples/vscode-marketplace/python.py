"""
VS Code Marketplace Scraper — extension details, install/trending stats, search & reviews (FreshActors / Apify)
Store: https://apify.com/freshactors/vscode-marketplace-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/vscode-marketplace-scraper").call(run_input={
    "mode": "details",
    "extensionIds": ["ms-python.python", "esbenp.prettier-vscode", "github.copilot"],
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["extensionId"], item["installs"], item["averageRating"], item["trendingMonthly"])

# Modes: details (exact extensionIds), search (searchTerms and/or category, sortBy
# relevance|installs|rating|updated, maxSearchResults<=500), reviews (newest 100 max).
# Every row carries installs + trending velocity scores — the extension-market signal.
