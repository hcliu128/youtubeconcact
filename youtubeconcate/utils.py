import os
from youtubeconcate.settings import CAP_DIR
from youtubeconcate.settings import DOWNLOADS
from youtubeconcate.settings import VIDEO


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS, exist_ok=True)
        os.makedirs(CAP_DIR, exist_ok=True)
        os.makedirs(VIDEO, exist_ok=True)

    def get_video_list_path(self, channel_id):
        return os.path.join(DOWNLOADS, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_video_id(url):
        return url.split("watch?v=")[1]

    def get_captions_path(self, url):
        return os.path.join(CAP_DIR, self.get_video_id(url) + ".txt")

    def caption_file_exists(self, url):
        path = self.get_captions_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0