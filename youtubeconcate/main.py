from youtubeconcate.pipeline.steps.get_video_lists import GetVideoLists
from youtubeconcate.pipeline.pipeline import Pipeline
inputs = {
    "channel_id": "UCQ6dAn-1lkPAnYmP4fnRNAg"
}


def main():
    steps = [
        GetVideoLists(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()






# print(get_all_video_in_channel("UCQ6dAn-1lkPAnYmP4fnRNAg"))
# print(len(get_all_video_in_channel("UCQ6dAn-1lkPAnYmP4fnRNAg")))
# print(API_KEY)