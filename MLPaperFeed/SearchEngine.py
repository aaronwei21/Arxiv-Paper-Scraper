import requests

# Make queries to Google CSE
class SearchEngine():
    API_KEY = 'key'
    SEARCH_ENGINE_ID = 'engine id'
    URL = 'https://www.googleapis.com/customsearch/v1'

    def get_request(self, query, start):
        params = {
            'q': query, 
            'key': self.API_KEY,
            'cx': self.SEARCH_ENGINE_ID,
            'start': start
        }
        return requests.get(self.URL, params = params).json()
    
