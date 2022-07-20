from .step import Step
from youtubeconcate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        word = inputs['term']
        found = []
        for yt in data:
            captions = yt.captions
            # print(captions)
            if not captions:
                continue
            for caption in captions:
                if word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        print(found)
        return found
