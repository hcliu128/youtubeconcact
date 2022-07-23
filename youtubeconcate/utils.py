import os
from youtubeconcate.settings import CAP_DIR
from youtubeconcate.settings import DOWNLOADS
from youtubeconcate.settings import VIDEO
from youtubeconcate.settings import OUTPUT


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS, exist_ok=True)
        os.makedirs(CAP_DIR, exist_ok=True)
        os.makedirs(VIDEO, exist_ok=True)
        os.makedirs(OUTPUT, exist_ok=True)

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_path(self, channel_id):
        return os.path.join(DOWNLOADS, channel_id + '.txt')

    def caption_file_exists(self, yt):
        path = yt.caption_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_output_file(self, channel_id, search_word):
        filename = channel_id + "_" + search_word + ".mp4"
        return os.path.join(OUTPUT, filename)
