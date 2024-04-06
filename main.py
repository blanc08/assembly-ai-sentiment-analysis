from yt_extractor import get_audio_url, get_video_infos
from api import save_transcription


def save_video_sentiments(url: str):
    video_info, error = get_video_infos(url)
    if error:
        return "something went wrong"

    if video_info is None:
        return "something went wrong"

    audio_url = get_audio_url(video_info)
    if audio_url == "":
        return "audio url not found"

    title = video_info["title"]
    title = title.strip().replace(" ", "_")
    title = "data/" + title
    save_transcription(audio_url, title, sentiment_analysis=True)


if __name__ == "__main__":
    save_video_sentiments("https://youtu.be/OvExVA0FS08?si=kSjxnto-ABfEbFia")
