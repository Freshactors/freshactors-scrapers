#!/usr/bin/env bash
# Greenhouse & Lever Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
# Store: https://apify.com/freshactors/greenhouse-lever-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~greenhouse-lever-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["gitlab","https://jobs.lever.co/spotify"],"ats":"auto","includeDescription":true,"maxJobsPerCompany":100}'

# "auto" tries Greenhouse then Lever for bare tokens; full board URLs are auto-detected either way.
