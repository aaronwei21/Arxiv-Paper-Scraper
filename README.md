# Arxiv-Paper-Scraper
Crawling the web and scraping paper's from arxiv.org using Scrapy and Google's programmable search engine. Crawling
rates are tuned to comply with export.arxiv.org's allowable rates given here: info.arxiv.org/help/bulk_data.html#harvest.

Originally made to crawl the websites of university ML reading groups (hence the name of the Scrapy project folder), 
but the program can be used to seek out arxiv.org papers given any list of Google search inputs. 

Follow these instructions to use:
1. Enter appropriate API information in SearchEngine.py
2. Go to PaperSpiders.py and configure search_inputs and other settings
3. Navigate to MLPaperFeed in terminal and enter "scrapy crawl 'paper'"
4. View output in results folder
