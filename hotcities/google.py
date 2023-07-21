import io
import os
import requests
from googleapiclient.discovery import build
from google.cloud import vision
from google.oauth2.service_account import Credentials


class Google:
    def __init__(self):
        api_key = os.environ.get('GOOGLE_API_KEY')
        self.cse_id = os.environ.get('GOOGLE_CSE_ID')
        self.custom_search_service = build(
            'customsearch', 'v1', developerKey=api_key)

        vision_key_file = os.environ.get('GOOGLE_CLOUD_VISION_KEY_FILE')
        vision_credentials = Credentials.from_service_account_file(
            vision_key_file)
        self.vision_service = vision.ImageAnnotatorClient(
            credentials=vision_credentials)

    def search_images(self, query, num=3, **kwargs):
        res = self.custom_search_service.cse().list(
            q=query,
            cx=self.cse_id,
            searchType='image',
            rights='cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
            num=num,
            **kwargs
        ).execute()
        return [item['link'] for item in res['items']]

    def analyze_image(self, image_url):
        res = requests.get(image_url)
        image = vision.Image(content=res.content)
        res = self.vision_service.annotate_image({
            'image': {'content': image.content},
            'features': [
                {'type_': vision.Feature.Type.SAFE_SEARCH_DETECTION},
                {'type_': vision.Feature.Type.LABEL_DETECTION, 'max_results': 100},
                # {'type_': vision.Feature.Type.IMAGE_PROPERTIES},
                # {'type_': vision.Feature.Type.WEB_DETECTION},
                # {'type_': vision.Feature.Type.LANDMARK_DETECTION},
            ]
        })
        safe_search = res.safe_search_annotation.adult != "LIKELY" and res.safe_search_annotation.violence != "LIKELY"
        labels = [{'description': label.description.lower(), 'score': label.score}
                  for label in res.label_annotations]
        # properties = res.image_properties_annotation
        # web_entities = res.web_detection.web_entities
        # landmarks = res.landmark_annotations
        data = {
            'safe_search': safe_search,
            'labels': labels,
            # 'properties': properties,
            # 'web_entities': web_entities,
            # 'landmarks': landmarks,
        }
        return data


google = Google()
