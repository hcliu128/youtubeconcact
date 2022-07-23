from .step import Step
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            begin, end = self.parse_time(found.time)
            video = VideoFileClip(found.yt.video_path).subclip(begin, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(utils.get_output_file(inputs["channel_id"], inputs["term"]))

    def parse_time(self, caption_time):
        print(caption_time)
        begin, end = caption_time.split("-->")
        return self.parse_time_to_str(begin), self.parse_time_to_str(end)

    def parse_time_to_str(self, time):
        h, m, s = time.split(":")
        s, ms = s.split(",")
        return int(h), int (m), int(s) + int(ms) / 1000