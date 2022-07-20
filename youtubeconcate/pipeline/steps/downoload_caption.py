import os

from youtubeconcate.pipeline.steps.step import Step
from youtubeconcate.pipeline.steps.step import StepException
from youtubeconcate.settings import CAP_DIR
from pytube import YouTube


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            print('downloading captions for ', yt.id)
            if utils.caption_file_exists(yt):
                print("pass this video")
                continue
            else:
                print("i dont find it")
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except AttributeError:
                print("AttributeError for ", yt.url)
                continue

            text_file = open(utils.get_captions_path(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data




