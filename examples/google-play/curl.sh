#!/usr/bin/env bash
# Google Play Scraper — app details, reviews & search (FreshActors / Apify)
# Store: https://apify.com/freshactors/google-play-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~google-play-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"mode":"details","appIds":["com.spotify.music"],"country":"us","lang":"en"}'

# Other modes (swap the -d payload):
#   reviews: {"mode":"reviews","appIds":["com.spotify.music"],"maxReviewsPerApp":100,"reviewsSort":"newest"}
#   search:  {"mode":"search","searchTerms":["podcast"],"maxSearchResults":20}
