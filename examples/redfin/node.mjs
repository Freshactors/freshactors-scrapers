/*
 * Redfin Scraper — US real-estate listings & sold homes (FreshActors / Apify)
 * Store: https://apify.com/freshactors/redfin-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/redfin-scraper').call({
  redfinUrls: ['https://www.redfin.com/city/30818/TX/Austin'],
  listingType: 'forSale',
  maxListings: 50,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// Pass any Redfin city / zip / neighborhood search URL. The region is read from the URL.
//   Recently sold: { redfinUrls: ['https://www.redfin.com/zipcode/78701'], listingType: 'sold', maxListings: 50 }
