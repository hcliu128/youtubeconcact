import os
from youtubeconcate.settings import CAP_DIR
from youtubeconcate.settings import VIDEO


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id(url)
        self.caption_path = self.get_captions_path()
        self.video_path = self.get_video_path()
        self.captions = None

    @staticmethod
    def get_video_id(url):
        return url.split("watch?v=")[1]

    def get_captions_path(self):
        return os.path.join(CAP_DIR, self.id + ".txt")

    def get_video_path(self):
        return os.path.join(VIDEO, self.id + ".mp4")

    def __str__(self):
        return '<YT( >'+self.id+" )>"

    def __repr__(self):
         content = ' : '.join([
            'id =' + str(self.id),
            'caption_path =' + str(self.caption_path),
            'video_path =' + str(self.video_path),
        ])
         return '<YT(' + content + ')>'
