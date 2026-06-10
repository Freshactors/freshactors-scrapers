/*
 * Teamtailor Jobs Scraper — normalized career-site job postings (FreshActors / Apify)
 * Store: https://apify.com/freshactors/teamtailor-jobs-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/teamtailor-jobs-scraper').call({
  companies: ['polestar', 'https://oatly.teamtailor.com'],
  includeDescription: true,
  maxJobsPerCompany: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);

// companies = Teamtailor subdomains, full URLs, or custom-domain career sites.
// One request returns the company's FULL published board, descriptions included.
