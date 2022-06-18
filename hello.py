import os
import numpy as np
import pandas as pd
from utils.abs import get_abspath

import warnings
warnings.filterwarnings('error')
  
# displaying the warning message 
warnings.warn('Warning Message: 4')

try:
    print(x)
except NameError:
    pass

for i, file in enumerate(os.listdir("audio_data")):
    speaker_id = file.split("_")[-1][:-len(".flac")]
    print("File {}: {}; Speaker id: {}".format(i, get_abspath(file), speaker_id))