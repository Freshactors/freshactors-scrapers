#!/usr/bin/env bash
# Shopify App Store Scraper — app details, reviews & discovery (FreshActors / Apify)
# Store: https://apify.com/freshactors/shopify-app-store-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~shopify-app-store-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"mode":"details","appHandles":["klaviyo-email-marketing"]}'

# Other modes (swap the -d payload):
#   reviews:  {"mode":"reviews","appHandles":["klaviyo-email-marketing"],"maxReviewsPerApp":100}
#   discover: {"mode":"discover","query":"email","maxApps":20}
