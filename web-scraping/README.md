# Terraria Wiki Web Scraping

## Research Question

How do Terraria item pages and enemy pages differ in their length and organization?

## Why I Chose This Wiki

I chose the Terraria Wiki because it contains information about many items and enemies in the game. I want to compare these two types of pages to see how their information is organized.

## Website and Rules

- **Wiki:** https://terraria.wiki.gg/
- **robots.txt:** https://terraria.wiki.gg/robots.txt

Before scraping, I checked the website's `robots.txt` file and considered its community rules to make sure my scraping approach followed the site's guidelines. The `robots.txt` file provides instructions for crawlers about which parts of a website they may or may not access. My script uses Python's `requests` and BeautifulSoup libraries to collect information from a small number of pages. It also checks response status codes and pauses between requests. I will follow the site's applicable restrictions and avoid scraping pages that are disallowed.

## Data Collection

I collected the page type, page title, URL, approximate word count, and number of links for each page. I compared one enemy page and one item page and saved the results in `terraria_wiki_data.csv` so they can be analyzed in Excel.

## Reflection

The scraper collected the page titles, approximate word counts, and link counts for one enemy page and one item page on the Terraria Wiki. The results show that the Slimes page had about 3,673 words and 1,042 links, while the Gel page had about 1,740 words and 744 links. This suggests that the enemy page contains more text and links than the item page in these examples. However, word count and link count do not directly measure how useful or informative a page is. Since I only collected two pages, I cannot conclude that all enemy pages are longer or more detailed than item pages.
