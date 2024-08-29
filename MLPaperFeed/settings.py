# Scrapy settings for MLPaperFeed project
#

BOT_NAME = "MLPaperFeed"

SPIDER_MODULES = ["MLPaperFeed.spiders"]
NEWSPIDER_MODULE = "MLPaperFeed.spiders"
# Staying on the safe side of Arxiv's regulations 
# but you can increase CONCURRENT_REQUESTS to 4
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 1 
DOWNLOAD_DELAY = 1 

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "MLPaperFeed.pipelines.GeneralPipeline": 100
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
