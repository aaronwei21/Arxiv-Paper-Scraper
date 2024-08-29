from ..SearchEngine import SearchEngine
import scrapy, re, math, json

# Crawls and scrapes Arxiv paper links 
# stored in JSON files
class LinkSpider(scrapy.Spider):
    name = "paper" 
    max_queries = 5 # maximum number of queries made to CSE
    num_pages = 1 # pages of results to per search input
    file_name = "test.csv" # store results in this file 
    data_path = 'spiders/data/CANSchools.json'
    with open(data_path, 'r') as file:
        data = json.load(file)
    
    def start_requests(self):
        search_inputs = [u["Name"] + " Machine Learning Reading Group" for u in self.data] # change this to what you want
        engine = SearchEngine()
        num_inputs = min(math.floor(self.max_queries/self.num_pages), len(search_inputs))

        for n in range(num_inputs):
            for i in range(self.num_pages):
                result = engine.get_request(search_inputs[n], start = i*10 + 1)
                for item in result.get('items', []):
                    url = item['link']
                    if "reading" in url or "mlrg" in url:
                        yield scrapy.Request(url = url, callback = self.parse_page)    

    # Collecting papers via Arxiv links on crawled pages
    def parse_page(self, response):
        origin = response.url
        links = response.css("a::attr(href)").getall()

        for link in links: 
            if "arxiv.org/pdf" in link:  
                link = link.replace("arxiv.org/pdf", "export.arxiv.org/abs")
                yield scrapy.Request(url = link, callback = self.parse_arxiv, meta={"origin":origin})
            elif "arxiv.org/abs" in link: 
                link = link.replace("arxiv.org", "export.arxiv.org")
                yield scrapy.Request(url = link, callback = self.parse_arxiv, meta={"origin":origin})

    # Collect information from Arxiv abstract page
    def parse_arxiv(self, response):
        # Use regex to find submission date
        pattern = r'\b\d{1,2} [A-Za-z]{3} \d{4}\b'
        match = re.search(pattern, response.css("div.dateline::text").get())
        date = match.group() if match else "Not Available"
        # Yield paper information in a dictionary
        yield {
            "Title": response.css("h1.title::text").get().replace("\n", ""),
            "Author(s)": ', '.join(response.css("div.authors a::text").getall()),
            "Link": response.url,
            "Submission Date": date,
            "Origin": response.meta["origin"]
        }

