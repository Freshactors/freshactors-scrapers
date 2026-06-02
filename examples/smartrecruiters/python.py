"""
SmartRecruiters Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
Store: https://apify.com/freshactors/smartrecruiters-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/smartrecruiters-jobs-scraper").call(run_input={
    "companies": ["visa", "https://jobs.smartrecruiters.com/Bosch"],
    "includeDescription": True,
    "maxJobsPerCompany": 200,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# companies = SmartRecruiters identifiers (jobs.smartrecruiters.com/<company>) or board URLs.
# includeDescription=False -> fast list-only run (metadata + URL, no per-posting detail call).
# Same normalized schema as the Greenhouse+Lever and Workable scrapers.
