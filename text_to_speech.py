import os
import dotenv
import requests


class TextToSpeech:
    """
    A class for synthesizing text to speech using the Eleven Labs API.
    """

    def __init__(self) -> None:
        """
        Initializes the TextToSpeech object with constants and headers.
        """
        self.chunk_size = 1024
        self.voice_id = "EXAVITQu4vr4xnSDxMaL"
        self.url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
        self.headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        }

    def synthesize_text(self, text: str, output_file: str) -> None:
        """
        Synthesizes the given text to speech and saves it to the given output file.

        Args:
            text (str): The text to synthesize.
            output_file (str): The file to save the synthesized speech to.
        """
        data = {"text": text, "voice_settings": {"stability": 0, "similarity_boost": 0}}

        response = requests.post(self.url, headers=self.headers, json=data)

        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=self.chunk_size):
                if chunk:
                    f.write(chunk)


if __name__ == "__main__":
    dotenv.load_dotenv()

    tts = TextToSpeech()
    tts.synthesize_text("Hello world", "output.mp3")
