from youtubeconcate.pipeline.steps.get_video_lists import GetVideoLists
from youtubeconcate.pipeline.steps.downoload_caption import DownloadCaption
from youtubeconcate.pipeline.pipeline import Pipeline
from youtubeconcate.utils import Utils
from youtubeconcate.Preflight import Preflight
from youtubeconcate.Postflight import Postflight
inputs = {
    "channel_id": "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
}


def main():
    steps = [
        Preflight(),
        GetVideoLists(),
        DownloadCaption(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()







