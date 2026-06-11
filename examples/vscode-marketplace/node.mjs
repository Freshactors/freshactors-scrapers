/*
 * VS Code Marketplace Scraper — extension details, install/trending stats, search & reviews (FreshActors / Apify)
 * Store: https://apify.com/freshactors/vscode-marketplace-scraper
 * Repo:  https://github.com/Freshactors/freshactors-scrapers
 *
 * Run:  npm install apify-client
 *       export APIFY_TOKEN=your_token_here
 *       node node.mjs
 */
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('freshactors/vscode-marketplace-scraper').call({
  mode: 'search',
  category: 'Data Science',
  sortBy: 'installs',
  maxSearchResults: 25,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.map((i) => `${i.extensionId}  installs=${i.installs}  rating=${i.averageRating}`));

// Modes: details | search | reviews. Search takes searchTerms and/or a category,
// sortable by relevance|installs|rating|updated. Reviews: the newest 100 per extension.
