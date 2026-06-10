"""
Personio Jobs Scraper — normalized DACH job postings + departments & seniority (FreshActors / Apify)
Store: https://apify.com/freshactors/personio-jobs-scraper
Repo:  https://github.com/Freshactors/freshactors-scrapers

Run:   pip install apify-client
       export APIFY_TOKEN=your_token_here
       python python.py
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/personio-jobs-scraper").call(run_input={
    "companies": ["teamative", "https://lanch.jobs.personio.de"],
    "includeDescription": True,
    "maxJobsPerCompany": 100,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# companies = Personio tenants (the {tenant}.jobs.personio.de subdomain) or portal URLs.
# Personio uniquely exposes `department` + `seniority` on virtually every posting.
# Optional: "language": "en" for localized titles/descriptions where the company provides them.
# Same normalized schema as the Greenhouse+Lever, Workable, SmartRecruiters, Recruitee, and Teamtailor scrapers.
