import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

#Function to transcribe audio using Whisper
def transcribe_audio(audio_file_path, sample_rate, language_code):
    """
    Transcribes audio using the OpenAI Whisper API with the selected language.
    """
    with open(audio_file_path, "rb") as audio_file:
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file,
            language=language_code  # Selected language for transcription
        )
    return transcription['text']

# Function to translate text using GPT-4
def translate_text(text, target_language_code):
    """
    Translates text to the selected language using GPT-4.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Translate the following text to {target_language_code}:"},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']