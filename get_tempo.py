import librosa
import os
import pandas as pd

dir = "music"
data = []
for filename in os.listdir(dir):
    file_path = os.path.join(dir, filename)
    if os.path.isfile(file_path):
        print(file_path)
        y, sr = librosa.load(file_path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        data.append({
                'filename': filename,
                'tempo': tempo[0],
            })

df = pd.DataFrame(data)
df.to_csv('output/song_tempos_and_beat_times.csv', index=False)