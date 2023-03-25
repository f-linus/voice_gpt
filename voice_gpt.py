import os
import pyaudio
import wave
import keyboard
import time
import openai
import dotenv
import gpt
import text_to_speech
from playsound import playsound

def start_listening():
    # Define the audio parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Initialize GPT chatbot
    gpt_chat = gpt.Chat()

    # Initialize text-to-speech synthesizer
    tts = text_to_speech.TextToSpeech()

    while True:
        # Check if "insert" key is pressed
        if not keyboard.is_pressed('insert'):
            # Sleep for 50 ms
            time.sleep(0.05)
            continue

        # Print message when recording starts
        print('Recording started...')

        # Open a stream to capture audio from the microphone
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []
        while keyboard.is_pressed('insert'):
            data = stream.read(CHUNK)
            frames.append(data)

        # Print message when recording stops
        print('Recording stopped.')

        # Close the audio stream
        stream.stop_stream()
        stream.close()

        # Save the audio as a WAV file
        wave_file = wave.open('input.wav', 'wb')
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

        # Transcribe using OpenAI API
        file = open("input.wav", "rb")
        transcription = openai.Audio.transcribe("whisper-1", file)

        # If no transcription found, continue listening
        if "text" not in transcription:
            print("No transcription found")
            continue

        # Get the user's input
        user_input = transcription["text"]

        # Generate a response using GPT chatbot
        response = gpt_chat.message(user_input)

        # Synthesize the response using text-to-speech synthesizer
        # Remove previous audio file if it exists
        if os.path.exists("output.mpeg"):
            os.remove("output.mpeg")
        tts.synthesize_text(response, "output.mpeg")

        # Play the audio file
        playsound("output.mpeg")

if __name__ == '__main__':
    # Load OpenAI API key from environment variable
    dotenv.load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Start listening for user input
    start_listening()
