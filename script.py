import librosa
import os


dir = "music"
for filename in os.listdir(dir):
    file_path = os.path.join(dir, filename)
    if os.path.isfile(file_path):
       pass