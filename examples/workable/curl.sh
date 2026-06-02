#!/usr/bin/env bash
# Workable Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
# Store: https://apify.com/freshactors/workable-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~workable-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["pearltalent","walletconnect"],"includeDescription":true,"maxJobsPerCompany":200}'

# companies = Workable shortcodes or apply.workable.com board URLs.
