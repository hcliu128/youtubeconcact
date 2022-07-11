import os

from youtubeconcate.pipeline.steps.step import Step
from youtubeconcate.pipeline.steps.step import StepException
from youtubeconcate.settings import CAP_DIR
from pytube import YouTube


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('downloading captions for ', url)
            if utils.caption_file_exists(url):
                print("pass this video")
                continue
            else:
                print("i dont find it")
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except AttributeError:
                print("AttributeError for ", url)
                continue

            text_file = open(utils.get_captions_path(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()




