import os
from youtubeconcate.settings import CAP_DIR
from youtubeconcate.settings import DOWNLOADS
from youtubeconcate.settings import VIDEO

class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS,exist_ok=True)
        os.makedirs(CAP_DIR, exist_ok=True)
        os.makedirs(VIDEO, exist_ok=True)

    @staticmethod
    def get_video_id(url):
        return url.split("watch?v=")[1]

    def get_captions_path(self, url):
        return os.path.join(CAP_DIR, self.get_video_id(url) + ".txt")