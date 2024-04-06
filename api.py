import json
import time
import requests
import assemblyai as aai
import sys

from api_secrets import API_KEY_ASSEMBLYAI


# upload
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {"authorization": API_KEY_ASSEMBLYAI}


def upload(filename: str) -> str:
    def read_file(filename, chunk_size=5242880):
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(
        upload_endpoint,
        headers=headers,
        data=read_file(filename),
    )

    audio_url = upload_response.json()["upload_url"]
    return audio_url


# transcibe
def transcribe(audio_url: str, sentiment_analysis=False) -> str:
    json = {"audio_url": audio_url, "sentiment_analysis": sentiment_analysis}

    transcript_response = requests.post(
        transcript_endpoint,
        json=json,
        headers=headers,
    )

    print(transcript_response.json())

    job_id = transcript_response.json()["id"]
    return job_id


# pool
def poll(transcript_id):
    pooling_endpoint = transcript_endpoint + "/" + transcript_id
    pooling_response = transcript_response = requests.get(
        pooling_endpoint,
        headers=headers,
    )

    return pooling_response.json()


def get_transcription_url(audio_url, sentiment_analysis=False):
    transcript_id = transcribe(audio_url, sentiment_analysis)

    while True:
        pooling_response = poll(transcript_id)

        if pooling_response["status"] == "completed":
            return pooling_response, None
        elif pooling_response["status"] == "error":
            return pooling_response, pooling_response["error"]

        print("waiting 30 seconds")
        time.sleep(30)


def save_transcription(audio_url: str, filename: str, sentiment_analysis=False):
    data, error = get_transcription_url(audio_url, sentiment_analysis)
    if error is not None:
        print("no, its not working...")

    # save transcibe
    text_filename = filename + ".txt"
    with open(text_filename, "w") as f:
        f.write(data["text"])

    if sentiment_analysis == True:
        sentiment_filename = filename + "_sentiments.json"
        with open(sentiment_filename, "w") as f:
            sentiments = data["sentiment_analysis_results"]
            json.dump(sentiments, f, indent=4)

    print("transcription saved")
