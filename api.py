from youtube_transcript_api import YouTubeTranscriptApi
import json

file = YouTubeTranscriptApi.get_transcript(
    "Yp48NQJygP4")


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(file, f, ensure_ascii=False, indent=4)

i = 0
while i < len(file)-1:
    print(file[i]["text"] + " " + file[i+1]["text"])
    i += 2
