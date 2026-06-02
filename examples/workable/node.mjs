/*
 * Workable Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
 * Store: https://apify.com/freshactors/workable-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/workable-jobs-scraper').call({
  companies: ['pearltalent', 'https://apply.workable.com/walletconnect/'],
  includeDescription: true,
  maxJobsPerCompany: 200,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// companies = Workable shortcodes (slug in apply.workable.com/<shortcode>/) or board URLs.
