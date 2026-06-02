#!/usr/bin/env bash
# App Store Scraper — iOS app details, search & reviews (FreshActors / Apify)
# Store: https://apify.com/freshactors/app-store-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~app-store-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"mode":"details","appIds":["389801252"],"country":"us"}'

# Other modes (swap the -d payload):
#   search:  {"mode":"search","searchTerms":["photo editor"],"country":"us","maxSearchResults":20}
#   reviews: {"mode":"reviews","appIds":["389801252"],"maxReviewsPerApp":100,"reviewsSort":"mostRecent"}
