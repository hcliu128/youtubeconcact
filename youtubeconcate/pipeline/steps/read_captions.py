import os
from pprint import pprint
from .step import Step
from youtubeconcate.settings import CAP_DIR


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            captions = {}
            with open(yt.caption_path, 'r', encoding='utf-8') as f:
                time_line = False
                caption = None
                time = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        time_line = False
            yt.captions = captions
            pprint(data)
            # print(yt.captions)
        return data


