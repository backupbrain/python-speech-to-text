import os

from pocketsphinx import Pocketsphinx, get_data_path, get_model_path
from pydub import AudioSegment

model_path = get_model_path()
# data_path = get_data_path()
data_path = "data"

config = {
    # 'sampling_rate': 24000,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

ps = Pocketsphinx(**config)


sound = AudioSegment.from_mp3("data/sample.mp3")

sound.export("data/sample.raw", format="wav", bitrate="16k")

with open("data/sample.raw", 'wb') as file:
    file.write(sound._data)
    file.close()

ps.decode(
    audio_file=os.path.join(data_path, 'sample.wav'),
    buffer_size=2048,
    no_search=False,
    full_utt=False
)

# print(ps.segments())
# print('Detailed segments:', *ps.segments(detailed=True), sep='\n')

print(ps.hypothesis())
print(ps.confidence())

# print(*ps.best(count=10), sep='\n')
