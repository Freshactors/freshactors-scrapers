#!/usr/bin/env bash
# Teamtailor Jobs Scraper — normalized career-site job postings (FreshActors / Apify)
# Store: https://apify.com/freshactors/teamtailor-jobs-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~teamtailor-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies":["polestar"],"includeDescription":true,"maxJobsPerCompany":100}'

# companies = Teamtailor subdomains ({name}.teamtailor.com), full URLs, or custom-domain career sites.
