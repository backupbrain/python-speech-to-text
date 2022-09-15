import os
import wave

from pocketsphinx import AudioFile, get_data_path, get_model_path

model_path = get_model_path()
data_path = "data"

config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, 'sample.wav'),
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)

# ffmpeg -i data/sample.mp3 -acodec pcm_s16le -ac 1 -ar 16000 data/sample.wav
