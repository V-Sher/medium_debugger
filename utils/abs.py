import os
from .upper import to_upper

def get_abspath(filename: str):
    print("UPPERCASE filename: ", to_upper(filename))
    return os.path.abspath(filename)