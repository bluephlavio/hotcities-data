import os
import flickrapi


class Flickr:
    def __init__(self):
        api_key = os.environ.get('FLICKR_API_KEY')
        api_secret = os.environ.get('FLICKR_API_SECRET')
        self.api = flickrapi.FlickrAPI(
            api_key, api_secret, format='parsed-json')

    def search_images(self, query=None):
        if query is None:
            return None
        photos = self.api.photos.search(text=query, per_page=3)[
            'photos']['photo']
        return [self.get_photo_url(photo) for photo in photos]

    def get_photo_url(self, photo):
        return f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg"


flickr = Flickr()
