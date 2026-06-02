/*
 * Recruitee Jobs Scraper — normalized ATS job postings + salary (FreshActors / Apify)
 * Store: https://apify.com/freshactors/recruitee-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/recruitee-jobs-scraper').call({
  companies: ['bunq', 'https://channable.recruitee.com'],
  includeDescription: true,
  maxJobsPerCompany: 200,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// companies = Recruitee identifiers (the {name}.recruitee.com subdomain) or board URLs.
// includeDescription:false = smaller records. `salary` is populated where the company sets it.
