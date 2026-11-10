# IS310 – Getting Cultural Data from APIs

## Project Overview

This project explores how cultural data can be collected and connected through APIs. I used two different APIs: the MediaWiki Action API from the LOTR Fandom Wiki and the Metropolitan Museum of Art Collection API. My goal was to retrieve cultural information, examine how the two APIs organize their data, and explore how different cultural collections can be accessed through programming.

The project uses Python and the `requests` library to send API requests, retrieve JSON responses, and save the results locally.

## APIs Used

### 1. LOTR Fandom MediaWiki API

The first API I used was the MediaWiki Action API from the Lord of the Rings Fandom Wiki.

This API provides information about the fictional world of Lord of the Rings, including characters, locations, articles, and other related information. I used it to retrieve cultural information from the wiki and save the returned data as JSON.

The API uses structured JSON responses, which makes it relatively easy to access specific information without manually scraping HTML pages. However, the data depends on how contributors have organized and documented the wiki.

### 2. Metropolitan Museum of Art Collection API

For my second API, I chose the Metropolitan Museum of Art Collection API because I was interested in exploring how a museum makes its cultural collection accessible through digital infrastructure.

The Met API provides information about artworks in its collection, including object IDs, titles, artists, dates, materials, departments, cultural information, and image URLs.

I used the API to search for paintings and retrieve information about individual museum objects. The data was returned in JSON format, which made it possible to organize the results into a structured dataset.

Unlike the LOTR Fandom API, which focuses on a fictional cultural universe maintained by a community, the Met API provides information about physical artworks collected and documented by a major museum.

## Comparing the Two APIs

The LOTR Fandom MediaWiki API and the Metropolitan Museum of Art Collection API provide different ways of accessing cultural information. The MediaWiki API is designed around a collaborative encyclopedia, while the Met API is designed around a museum collection. The LOTR API allows users to retrieve wiki information through search and other MediaWiki actions, while the Met API provides structured information about individual museum objects. Both APIs return JSON, which makes their data relatively easy to process using Python. However, their structures reflect different priorities: MediaWiki organizes information around articles and their relationships, while the Met organizes information around individual objects and their collection records. The LOTR API is maintained through the Fandom wiki platform and community contributions, while the Met API is provided by the Metropolitan Museum of Art, a public-facing cultural institution. Their access policies and rate limits are different, so researchers need to consider the documentation and usage requirements of each service rather than assuming that every API supports unlimited requests. The two datasets also reflect different cultural choices. LOTR Fandom represents a fictional universe and depends on community interest and editorial activity, while the Met collection reflects the museum's collecting history, cataloguing practices, and decisions about which objects are digitized. Although both APIs make cultural information accessible, neither represents culture in its entirety. The data available through each API is shaped by the institutions, communities, and systems responsible for creating and maintaining it.

## Connecting the APIs

This project uses the LOTR Fandom API and the Metropolitan Museum of Art API to explore cultural information from two different sources.

The LOTR API provides information about a fictional cultural universe, while the Met API provides information about physical artworks and their collection records.

Connecting these APIs demonstrates how cultural information can be retrieved from different systems and organized into structured datasets. However, the connection also highlights the limitations of working with different cultural collections. The APIs organize their information differently, and not every item has an obvious equivalent in the other dataset.

This makes the connection an exploratory process rather than a perfect one-to-one match.

## Data and Files

The project contains the following files:

- `getting_culture.py` – Python script used to retrieve cultural data from the APIs.
- `lotr_data.json` – JSON data retrieved from the LOTR Fandom API.
- `met_data.json` – JSON data retrieved from the Metropolitan Museum of Art API.

The script checks API responses and saves the retrieved data as JSON files.

## Limitations and Reflection

One limitation of this project is that the two APIs represent different types of cultural information. The LOTR Fandom API focuses on a fictional universe, while the Met API focuses on physical artworks and museum collection records. Because their data structures and purposes are different, connecting information between them can be difficult.

Another limitation is that not every museum object has complete metadata or an available image. Some records contain missing artist information, empty image URLs, or incomplete cultural descriptions. These gaps demonstrate that digitized collections are not always complete representations of the objects they describe.

The project also shows that APIs are not neutral systems. Their available data reflects the decisions made by the organizations and communities responsible for collecting, organizing, and maintaining information.

## Conclusion

This project helped me understand how APIs provide access to cultural data and how different systems organize information according to their own purposes. By working with the LOTR Fandom API and the Metropolitan Museum of Art API, I explored the differences between community-maintained cultural information and institutional museum collections.

The project also demonstrated the importance of handling API errors, inspecting returned data, and considering the limitations of cultural datasets. Ultimately, APIs make cultural information easier to access, but they also reflect the choices and limitations of the systems that maintain them.

