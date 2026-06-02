# FreshActors — Reliable Apify Web Scrapers 🟢

Production-ready, **always-fresh** web scrapers on the [Apify Store](https://apify.com/freshactors) for the data sources teams actually need — the **Apple App Store**, **Google Play**, **Redfin** real estate, the **Shopify App Store**, and **Greenhouse / Lever / Workable / SmartRecruiters / Recruitee** job boards.

Every scraper here is:

- **Pure HTTP/JSON** — no headless browser, no API key, no login. Fast and cheap to run.
- **Pay-per-event** — you pay only for the data you actually receive, and there's **no per-run start fee**.
- **Monitored daily** — each actor is health-checked every day against the real customer path and patched fast when a target site changes. Most marketplace scrapers rot; these don't. That's the *always-fresh* promise.

> No tokens to babysit, no CSS selectors to maintain, no proxies to rent. Call the actor, get clean structured JSON.

This repo has copy-paste **Python, Node.js, and cURL** examples for every scraper. Each one links to its Apify Store page where you can run it in one click.

## The scrapers

| Scraper | What it extracts | Modes | Apify Store |
|---|---|---|---|
| **App Store Scraper** | iOS app details, keyword search & rankings, customer reviews | `details` · `search` · `reviews` | [freshactors/app-store-scraper](https://apify.com/freshactors/app-store-scraper) |
| **Google Play Scraper** | Android app details, ratings histogram, reviews, keyword search | `details` · `reviews` · `search` | [freshactors/google-play-scraper](https://apify.com/freshactors/google-play-scraper) |
| **Redfin Scraper** | US real-estate listings & sold homes — price, beds, baths, sqft, lat/long, MLS ID | `listings` (city / zip / sold) | [freshactors/redfin-scraper](https://apify.com/freshactors/redfin-scraper) |
| **Shopify App Store Scraper** | Shopify app details, reviews, and catalog discovery | `details` · `reviews` · `discover` | [freshactors/shopify-app-store-scraper](https://apify.com/freshactors/shopify-app-store-scraper) |
| **Greenhouse & Lever Jobs Scraper** | Job postings normalized into one schema across Greenhouse + Lever ATS | `greenhouse` · `lever` · `auto` | [freshactors/greenhouse-lever-jobs-scraper](https://apify.com/freshactors/greenhouse-lever-jobs-scraper) |
| **Workable Jobs Scraper** | Every role from a Workable company board, normalized — full descriptions in one call | `jobs` (per company) | [freshactors/workable-jobs-scraper](https://apify.com/freshactors/workable-jobs-scraper) |
| **SmartRecruiters Jobs Scraper** | Every posting from a SmartRecruiters company board, normalized — full descriptions, no API key | `jobs` (per company) | [freshactors/smartrecruiters-jobs-scraper](https://apify.com/freshactors/smartrecruiters-jobs-scraper) |
| **Recruitee Jobs Scraper** | Every posting from a Recruitee company board, normalized — full descriptions **+ salary**, one call, no API key | `jobs` (per company) | [freshactors/recruitee-jobs-scraper](https://apify.com/freshactors/recruitee-jobs-scraper) |

## Quickstart

You need a free [Apify account](https://apify.com) and your API token (**Settings → Integrations → API token**). Then pick a language — full runnable examples for every scraper live in [`examples/`](examples/).

### Python

```bash
pip install apify-client
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("freshactors/app-store-scraper").call(run_input={
    "mode": "details",
    "appIds": ["389801252"],   # Instagram
    "country": "us",
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/app-store-scraper').call({
  mode: 'details',
  appIds: ['389801252'], // Instagram
  country: 'us',
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL (no SDK)

```bash
curl -s -X POST \
  "https://api.apify.com/v2/acts/freshactors~app-store-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode":"details","appIds":["389801252"],"country":"us"}'
```

## Examples by scraper

Each folder has a runnable `python.py`, `node.mjs`, and `curl.sh`. Set your token first: `export APIFY_TOKEN=your_token_here`.

### App Store — [`examples/app-store/`](examples/app-store) · [store page](https://apify.com/freshactors/app-store-scraper)
Scrape iOS app metadata, keyword search results (great for ASO), and customer reviews. Apple's legacy review feed silently returns an empty `200` when throttled — this actor retries through it so you never get a false "0 reviews".

```jsonc
{ "mode": "details", "appIds": ["389801252"], "country": "us" }
```

### Google Play — [`examples/google-play/`](examples/google-play) · [store page](https://apify.com/freshactors/google-play-scraper)
Android app details with the ratings histogram, installs, and developer response, plus reviews and keyword search — without parsing Google's nested `AF_initDataCallback` payloads yourself.

```jsonc
{ "mode": "details", "appIds": ["com.spotify.music"], "country": "us", "lang": "en" }
```

### Redfin — [`examples/redfin/`](examples/redfin) · [store page](https://apify.com/freshactors/redfin-scraper)
Clean US real-estate data from a city, zip, or "sold" search URL — list/sold price, beds, baths, square footage, lat/long, MLS ID, and more.

```jsonc
{ "redfinUrls": ["https://www.redfin.com/city/30818/TX/Austin"], "listingType": "forSale", "maxListings": 50 }
```

### Shopify App Store — [`examples/shopify-app-store/`](examples/shopify-app-store) · [store page](https://apify.com/freshactors/shopify-app-store-scraper)
Shopify app details (rating, review count, pricing, developer), full reviews, and catalog **discovery** via the App Store sitemap — for app market research and lead-gen.

```jsonc
{ "mode": "details", "appHandles": ["klaviyo-email-marketing"] }
```

### Greenhouse & Lever Jobs — [`examples/greenhouse-lever/`](examples/greenhouse-lever) · [store page](https://apify.com/freshactors/greenhouse-lever-jobs-scraper)
Job postings from **both** Greenhouse and Lever boards, normalized into one schema with full descriptions — pass bare company tokens or full board URLs; the ATS is auto-detected.

```jsonc
{ "companies": ["gitlab", "https://jobs.lever.co/spotify"], "ats": "auto", "includeDescription": true }
```

### Workable Jobs — [`examples/workable/`](examples/workable) · [store page](https://apify.com/freshactors/workable-jobs-scraper)
Every open role from a company's Workable board — with full descriptions — in one request, normalized into the same schema as the Greenhouse & Lever scraper. Pass shortcodes or board URLs.

```jsonc
{ "companies": ["pearltalent", "https://apply.workable.com/walletconnect/"], "includeDescription": true }
```

### SmartRecruiters Jobs — [`examples/smartrecruiters/`](examples/smartrecruiters) · [store page](https://apify.com/freshactors/smartrecruiters-jobs-scraper)
Every posting from a company's SmartRecruiters board — with full descriptions — normalized into the same schema as the Greenhouse, Lever, and Workable scrapers. No API key. Pass company identifiers or board URLs; set `includeDescription: false` for a fast list-only run.

```jsonc
{ "companies": ["visa", "https://jobs.smartrecruiters.com/BoschGroup"], "includeDescription": true }
```

### Recruitee Jobs — [`examples/recruitee/`](examples/recruitee) · [store page](https://apify.com/freshactors/recruitee-jobs-scraper)
Every posting from a company's Recruitee board — with full descriptions **and salary** — in a single API call, normalized into the same schema as the Greenhouse, Lever, Workable, and SmartRecruiters scrapers. No API key. Pass company identifiers (the `{name}.recruitee.com` subdomain) or board URLs.

```jsonc
{ "companies": ["bunq", "https://channable.recruitee.com"], "includeDescription": true }
```

## Use with AI agents (MCP)

Every FreshActors scraper is callable as a tool from AI agents through the [Apify MCP server](https://mcp.apify.com). Point Claude, Cursor, or any MCP client at `https://mcp.apify.com`, then call an actor by name (e.g. `freshactors/app-store-scraper`) — the agent passes the same JSON input shown above and gets structured results back.

## Why FreshActors?

Most marketplace scrapers are published once and left to rot — a site changes its markup, the scraper silently returns nothing, and you find out in production. **FreshActors scrapers are monitored every single day** against the real run path and patched fast when a target changes, with a public "last verified working" signal on each listing. Reliability isn't a feature here — it *is* the product.

## License

[MIT](LICENSE) — the example code in this repo is yours to use freely.

---

**FreshActors** · reliable data extraction on the [Apify Store](https://apify.com/freshactors). Found a site change before we did? [Open an issue on the actor's Apify page](https://apify.com/freshactors) — fast fixes are the whole point.
