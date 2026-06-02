/*
 * SmartRecruiters Jobs Scraper — normalized ATS job postings (FreshActors / Apify)
 * Store: https://apify.com/freshactors/smartrecruiters-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/smartrecruiters-jobs-scraper').call({
  companies: ['visa', 'https://jobs.smartrecruiters.com/BoschGroup'],
  includeDescription: true,
  maxJobsPerCompany: 200,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// companies = SmartRecruiters identifiers or board URLs. includeDescription:false = fast list-only run.
