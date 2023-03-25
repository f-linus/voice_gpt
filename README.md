# VoiceGPT

This project is a simple voice assistant that uses WhisperAI to transcribe audio to text, GPT-4 to generate responses, and ElevenLabs text-to-speech to speak the response.

## Getting Started

To get started with this project, you will need to clone this repository and install the required dependencies. You can do this by running the following commands:

``` bash
git clone git@github.com:f-linus/voice_gpt.git
cd voice_gpt
pip install -r requirements.txt
```

### API keys

You need to add your OpenAI and your ElevenLabs API keys to the .env file.

Once you have installed the dependencies and added the API keys, you can run the voice assistant by running the following command:

python voice_gpt.py

## Usage

To use the voice assistant, simply speak into your microphone while pressing the "insert" key. Then wait for a response. The voice assistant will transcribe your speech to text using WhisperAI, generate a response using GPT-4, and speak the response using ElevenLabs text-to-speech.
