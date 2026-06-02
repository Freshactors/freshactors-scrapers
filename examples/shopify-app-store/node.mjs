/*
 * Shopify App Store Scraper — app details, reviews & discovery (FreshActors / Apify)
 * Store: https://apify.com/freshactors/shopify-app-store-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/shopify-app-store-scraper').call({
  mode: 'details',
  appHandles: ['klaviyo-email-marketing'], // the slug in the apps.shopify.com URL
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// Other modes:
//   App reviews:   { mode: 'reviews',  appHandles: ['klaviyo-email-marketing'], maxReviewsPerApp: 100 }
//   Discover apps: { mode: 'discover', query: 'email', maxApps: 20 }
