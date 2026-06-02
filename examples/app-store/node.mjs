/*
 * App Store Scraper — iOS app details, search & reviews (FreshActors / Apify)
 * Store: https://apify.com/freshactors/app-store-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/app-store-scraper').call({
  mode: 'details',
  appIds: ['389801252'], // Instagram — the number in the App Store URL
  country: 'us',
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// Other modes:
//   Keyword search:   { mode: 'search',  searchTerms: ['photo editor'], country: 'us', maxSearchResults: 20 }
//   Customer reviews: { mode: 'reviews', appIds: ['389801252'], maxReviewsPerApp: 100, reviewsSort: 'mostRecent' }
