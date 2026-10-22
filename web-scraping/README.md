# Terraria Wiki Web Scraping

## Research Question
How do Terraria item pages and enemy pages differ in their length and organization?

## Why I Chose This Wiki
I chose the Terraria Wiki because it contains information about many items and enemies in the game. I want to compare these two types of pages to see how their information is organized.

## Website and Rules
- Wiki: https://terraria.wiki.gg/
- robots.txt: https://terraria.wiki.gg/robots.txt

Before scraping, I will check the website's `robots.txt` and community rules to make sure scraping is allowed. My script will use Python's `requests` and BeautifulSoup libraries to collect information from a small number of pages. It will also check response codes and pause between requests.

## Data Collection
I plan to collect the page title, word count, number of section headings, and number of internal links. I will save the results in a CSV file so they can be analyzed in Excel.

## Reflection
The data can help me compare how item pages and enemy pages are organized. However, having more words or links does not necessarily mean a page is more useful. These measurements only show certain features of the pages, not the accuracy or quality of their information. After collecting the data, I will compare the results and consider these limitations.
