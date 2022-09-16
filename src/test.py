import os
from os import listdir
from os.path import isfile, join

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


def get_sound_files(folder):
    return [f for f in listdir(folder) if isfile(join(folder, f)) and f.endswith(".wav")]


# sound = AudioSegment.from_mp3("data/sample.mp3")

# sound.export("data/sample.raw", format="wav", bitrate="16k")

# with open("data/sample.raw", 'wb') as file:
#     file.write(sound._data)
#     file.close()

files = get_sound_files("data/")
file = files[0]

ps.decode(
    audio_file=os.path.join(data_path, file),
    buffer_size=2048,
    no_search=False,
    full_utt=False
)

# print(ps.segments())
# print('Detailed segments:', *ps.segments(detailed=True), sep='\n')

print(ps.hypothesis())
print(ps.confidence())

# print(*ps.best(count=10), sep='\n')
