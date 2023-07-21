import os
import requests


class Unsplash:
    def __init__(self):
        self.api_key = os.environ.get('UNSPLASH_ACCESS_KEY')

    def search_images(self, query=None):
        if query is None:
            return None
        api_url = 'https://api.unsplash.com/search/photos'
        params = {'query': query, 'client_id': self.api_key}

        try:
            res = requests.get(api_url, params=params, allow_redirects=True)
            data = res.json()
            if not data.get('total'):
                return None
            return [item['urls']['raw'] for item in data['results']]

        except requests.exceptions.RequestException:
            return None


unsplash = Unsplash()
