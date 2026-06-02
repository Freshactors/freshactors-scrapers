#!/usr/bin/env bash
# Recruitee Jobs Scraper — normalized ATS job postings + salary (FreshActors / Apify)
# Store: https://apify.com/freshactors/recruitee-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~recruitee-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["bunq"],"includeDescription":true,"maxJobsPerCompany":200}'

# companies = Recruitee identifiers ({name}.recruitee.com subdomain) or board URLs.
