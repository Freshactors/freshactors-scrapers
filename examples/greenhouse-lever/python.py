"""
Greenhouse & Lever Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
Store: https://apify.com/freshactors/greenhouse-lever-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/greenhouse-lever-jobs-scraper").call(run_input={
    "companies": ["gitlab", "https://jobs.lever.co/spotify"],  # bare token OR full board URL
    "ats": "auto",
    "includeDescription": True,
    "maxJobsPerCompany": 100,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# "auto" tries Greenhouse then Lever for bare tokens; full board URLs are auto-detected either way.
