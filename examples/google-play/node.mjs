/*
 * Google Play Scraper — app details, reviews & search (FreshActors / Apify)
 * Store: https://apify.com/freshactors/google-play-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/google-play-scraper').call({
  mode: 'details',
  appIds: ['com.spotify.music'], // the id= part of the Play Store URL
  country: 'us',
  lang: 'en',
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// Other modes:
//   Customer reviews: { mode: 'reviews', appIds: ['com.spotify.music'], maxReviewsPerApp: 100, reviewsSort: 'newest' }
//   Keyword search:   { mode: 'search',  searchTerms: ['podcast'], maxSearchResults: 20 }
