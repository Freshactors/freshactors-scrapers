#!/usr/bin/env bash
# Personio Jobs Scraper — normalized DACH job postings + departments & seniority (FreshActors / Apify)
# Store: https://apify.com/freshactors/personio-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~personio-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["teamative"],"includeDescription":true,"maxJobsPerCompany":100}'

# companies = Personio tenants ({tenant}.jobs.personio.de subdomain) or portal URLs.
