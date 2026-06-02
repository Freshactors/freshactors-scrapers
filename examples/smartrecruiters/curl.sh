#!/usr/bin/env bash
# SmartRecruiters Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
# Store: https://apify.com/freshactors/smartrecruiters-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~smartrecruiters-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["visa"],"includeDescription":true,"maxJobsPerCompany":200}'

# companies = SmartRecruiters identifiers or jobs.smartrecruiters.com board URLs.
