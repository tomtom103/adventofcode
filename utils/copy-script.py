import os
import shutil

from pathlib import Path

# Script used to copy the sample-file into all files for every day.

sample_files = os.listdir(Path(__file__).parent.absolute() / 'sample-file')

for i in range(3, 26):
    for file in sample_files:
        shutil.copy(Path(__file__).parent.absolute() / 'sample-file' / file, Path(__file__).parent.absolute() / f'day-{i}' / file)