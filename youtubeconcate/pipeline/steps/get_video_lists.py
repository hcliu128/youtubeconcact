import urllib.request
import json
from youtubeconcate.settings import API_KEY
from youtubeconcate.pipeline.steps.step import Step


class GetVideoLists(Step):
    def process(self, data, inputs):
        channel_id = (inputs['channel_id'])
        api_key = API_KEY

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        # print(video_links)
        return video_links