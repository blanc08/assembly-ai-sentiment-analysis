import youtube_dl

ydl = youtube_dl.YoutubeDL()


def get_video_infos(url: str):
    """
    extract video's information
    """
    with ydl:
        result = ydl.extract_info(
            url,
            download=False,
        )

    if type(result) == dict and "entries" in result:
        return result["entries"][0], ""

    return result, ""


def get_audio_url(video_info) -> str:
    for f in video_info["formats"]:
        if f["ext"] in ["m4a"]:
            return f["url"]
    return ""


if __name__ == "__main__":
    video_info = get_video_infos("https://youtu.be/OvExVA0FS08?si=kSjxnto-ABfEbFia")
    audio_url = get_audio_url(video_info)
    print(audio_url)
