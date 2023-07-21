from .google import google
from .unsplash import unsplash
from .flickr import flickr

keywords = [
    "landmark",
    "cityscape",
    "skyline",
    "metropolitan area"
]


class CityImage:
    def __init__(self, url):
        self.url = url
        self.data = google.analyze_image(url)
        self.score = self._calc_score()

    def _calc_score(self, keywords=keywords):
        score = 0
        for label in self.data['labels']:
            if label["description"] in keywords:
                score += label["score"]
        score = score / max(1, min(len(self.data['labels']), len(keywords)))
        return score

    @classmethod
    def search(cls, query, num=10):
        urls = google.search_images(query, num=num)
        images = map(lambda url: cls(url), urls)
        filtered_images = filter(
            lambda image: image.data['safe_search'], images)
        sorted_filtered_images = sorted(
            filtered_images, key=lambda image: image.score, reverse=True)
        return sorted_filtered_images
