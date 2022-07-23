from youtubeconcate.pipeline.steps.get_video_lists import GetVideoLists
from youtubeconcate.pipeline.steps.downoload_caption import DownloadCaption
from youtubeconcate.pipeline.steps.read_captions import ReadCaptions
from youtubeconcate.pipeline.steps.initialize_yt import InitializeYT
from youtubeconcate.pipeline.steps.search import Search
from youtubeconcate.pipeline.steps.download_video import DownloadVideo
from youtubeconcate.pipeline.steps.edit_video import EditVideo
from youtubeconcate.pipeline.pipeline import Pipeline
from youtubeconcate.utils import Utils
from youtubeconcate.Preflight import Preflight
from youtubeconcate.Postflight import Postflight
inputs = {
    "channel_id": "UC-lHJZR3Gqxm24_Vd_AJ5Yw",
    "term": "entire face",
    "limit":20,
}


def main():
    steps = [
        Preflight(),
        GetVideoLists(),
        InitializeYT(),
        DownloadCaption(),
        ReadCaptions(),
        Search(),
        DownloadVideo(),
        EditVideo(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()







