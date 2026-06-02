"""
Workable Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
Store: https://apify.com/freshactors/workable-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/workable-jobs-scraper").call(run_input={
    "companies": ["pearltalent", "https://apply.workable.com/walletconnect/"],
    "includeDescription": True,
    "maxJobsPerCompany": 200,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# companies = Workable shortcodes (the slug in apply.workable.com/<shortcode>/) or board URLs.
# One request returns the whole board incl. full descriptions; same schema as Greenhouse+Lever.
