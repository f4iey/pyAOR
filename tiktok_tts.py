import requests
import base64
import json
import pydub
from pydub.playback import play
from io import BytesIO
import os

# API endpoint URL
url = 'https://tiktok-tts.weilnet.workers.dev/api/generation'

# Function to play the audio using PyDub playback
def play_audio(audio_data):
    audio_segment = pydub.AudioSegment.from_file(BytesIO(audio_data))
    play(audio_segment)

def say(text, voice="fr_001"):

    # Set the text and voice parameters
    #text = "Je voudrais juste intervenir un moment!"
    voice = "fr_001"

    # Define the request payload as a dictionary
    payload = {
        "text": text,
        "voice": voice
    }

    # Send the POST request with JSON payload
    response = requests.post(url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        json_response = json.loads(response.text)

    # Check if the audio was generated successfully
    if json_response['success']:
        # Decode the audio data from base64
        audio_data = base64.b64decode(json_response['data'])

        # Play the audio
        play_audio(audio_data)

        # Alternatively, save the audio to a temporary file, play it, and then delete the file
        # temp_filename = "temp_audio.mp3"
        # with open(temp_filename, "wb") as temp_file:
        #     temp_file.write(audio_data)
        # play_audio(audio_data)
        # os.remove(temp_filename)

    else:
        print(f"Error: {response.status_code} - {response.text}")
