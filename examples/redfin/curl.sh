#!/usr/bin/env bash
# Redfin Scraper — US real-estate listings & sold homes (FreshActors / Apify)
# Store: https://apify.com/freshactors/redfin-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~redfin-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"redfinUrls":["https://www.redfin.com/city/30818/TX/Austin"],"listingType":"forSale","maxListings":50}'

# Recently sold (swap the -d payload):
#   {"redfinUrls":["https://www.redfin.com/zipcode/78701"],"listingType":"sold","maxListings":50}
