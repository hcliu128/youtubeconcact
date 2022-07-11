import os

from youtubeconcate.pipeline.steps.step import Step
from youtubeconcate.pipeline.steps.step import StepException
from youtubeconcate.settings import CAP_DIR
from pytube import YouTube


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        print(data)
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            text_file = open(utils.get_captions_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break


