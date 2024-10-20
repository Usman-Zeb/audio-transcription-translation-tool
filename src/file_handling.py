import wave
import tempfile
from pydub import AudioSegment
import os

def audio_to_wav(audio_file_path, sample_rate):
    """
    Converts any supported audio file to a WAV format if needed.
    Uses pydub to convert file formats.
    """
    # Extract the file extension
    file_extension = os.path.splitext(audio_file_path)[1].lower()
    
    # If it's already a WAV file, no conversion needed
    if file_extension == '.wav':
        return audio_file_path

    # Otherwise, convert it to WAV using pydub
    audio = AudioSegment.from_file(audio_file_path)
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    audio.export(temp_file.name, format="wav")
    
    return temp_file.name
