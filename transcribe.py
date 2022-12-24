import whisper
import os
from download import download_video

model_name = "base.en"
model = whisper.load_model(model_name)

def transcribe(url):
    video = download_video(url)
    result = model.transcribe(video["file_name"])
    os.remove(video["file_name"])

    segments = []
    for item in result["segments"]:
        segments.append(format_item(item))

    return {
        "title": video["title"],
        "segments": segments
    }

def format_item(item):
    return {
        "time": item["start"],
        "text": item["text"]
    }
