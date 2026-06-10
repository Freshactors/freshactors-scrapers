/*
 * Personio Jobs Scraper — normalized DACH job postings + departments & seniority (FreshActors / Apify)
 * Store: https://apify.com/freshactors/personio-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/personio-jobs-scraper').call({
  companies: ['teamative', 'https://lanch.jobs.personio.de'],
  includeDescription: true,
  maxJobsPerCompany: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// companies = Personio tenants ({tenant}.jobs.personio.de) or portal URLs.
// `department` + `seniority` populated on virtually every posting. language: 'en' for localized output.
