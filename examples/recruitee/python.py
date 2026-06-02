"""
Recruitee Jobs Scraper — normalized ATS job postings + salary (FreshActors / Apify)
Store: https://apify.com/freshactors/recruitee-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/recruitee-jobs-scraper").call(run_input={
    "companies": ["bunq", "https://channable.recruitee.com"],
    "includeDescription": True,
    "maxJobsPerCompany": 200,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# companies = Recruitee identifiers (the {name}.recruitee.com subdomain) or board URLs.
# includeDescription=False -> smaller records (same cost/speed; Recruitee returns all in one call).
# Recruitee uniquely exposes a `salary` object when the company sets it.
# Same normalized schema as the Greenhouse+Lever, Workable, and SmartRecruiters scrapers.
