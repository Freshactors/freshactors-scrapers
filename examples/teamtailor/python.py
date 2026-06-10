"""
Teamtailor Jobs Scraper — normalized career-site job postings (FreshActors / Apify)
Store: https://apify.com/freshactors/teamtailor-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/teamtailor-jobs-scraper").call(run_input={
    "companies": ["polestar", "https://oatly.teamtailor.com"],
    "includeDescription": True,
    "maxJobsPerCompany": 100,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# companies = Teamtailor subdomains ({name}.teamtailor.com), full URLs, or custom-domain career sites.
# One request returns the company's FULL published board, descriptions included.
# includeDescription=False -> smaller records (same cost/speed).
# Same normalized schema as the Greenhouse+Lever, Workable, SmartRecruiters, Recruitee, and Personio scrapers.
