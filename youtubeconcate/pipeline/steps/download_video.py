from .step import Step
from pytube import YouTube
from youtubeconcate.settings import VIDEO


class DownloadVideo(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            url = yt.url
            print("downloading ", url)
            YouTube(url).streams.first().download(output_path=VIDEO, filename=yt.id+'.mp4')

        return data
