#!/usr/bin/env bash
# Microsoft Store Scraper — app details with rating windows, search & reviews with helpful votes (FreshActors / Apify)
# Store: https://apify.com/freshactors/microsoft-store-scraper
# Repo:  https://github.com/Freshactors/freshactors-scrapers
# Usage: export APIFY_TOKEN=your_token_here && bash curl.sh
set -euo pipefail

curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~microsoft-store-scraper/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"mode":"details","productIds":["9NKSQGP7F2NH","9NCBCSZSJRSB","9WZDNCRFJ3TJ"]}'

# productIds = 12-char Store ids starting with 9. Details include 7/30-day rating windows.
