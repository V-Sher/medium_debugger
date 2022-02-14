import os
from utils.abs import get_abspath

try:
    print(x)
except NameError:
    pass

for i, file in enumerate(os.listdir("audio_data")):
    speaker_id = file.split("_")[-1][:-len(".flac")]
    print("File {}: {}; Speaker id: {}".format(i, get_abspath(file), speaker_id))