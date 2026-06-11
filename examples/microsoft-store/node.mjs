/*
 * Microsoft Store Scraper — app details with rating windows, search & reviews with helpful votes (FreshActors / Apify)
 * Store: https://apify.com/freshactors/microsoft-store-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/microsoft-store-scraper').call({
  mode: 'reviews',
  productIds: ['9NKSQGP7F2NH'], // WhatsApp
  maxReviewsPerApp: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.map((r) => `${r.rating}★ 👍${r.helpfulPositive} [${r.deviceFamily ?? 'n/a'}] ${(r.text ?? '').slice(0, 60)}`));

// Reviews include helpful votes + device family + OS version. Details mode adds
// all-time/7-day/30-day rating windows; market/language localize any country.
