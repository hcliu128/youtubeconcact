import os
from pprint import pprint
from .step import Step
from youtubeconcate.settings import CAP_DIR


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAP_DIR):
            captions = {}
            with open(os.path.join(CAP_DIR, caption_file), 'r', encoding='utf-8') as f:
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
            data [caption_file] = captions
        pprint(data)
        return data


