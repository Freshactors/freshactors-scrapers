/*
 * Greenhouse & Lever Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
 * Store: https://apify.com/freshactors/greenhouse-lever-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/greenhouse-lever-jobs-scraper').call({
  companies: ['gitlab', 'https://jobs.lever.co/spotify'], // bare token OR full board URL
  ats: 'auto',
  includeDescription: true,
  maxJobsPerCompany: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// "auto" tries Greenhouse then Lever for bare tokens; full board URLs are auto-detected either way.
