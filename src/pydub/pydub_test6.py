
from pydub import AudioSegment
from pathlib import Path
import time

start_time = time.time()

wav_path = Path("../../audio-source/wave/a2002011001-e02.wav")
output_path = Path("../../output/output_test.mp3")
sound = AudioSegment.from_file(wav_path, format="wav")

# simple export
file_handle = sound.export(output_path, format="mp3")

# more complex export
file_handle = sound.export(output_path,
                           format="mp3",
                           bitrate="192k",
                           tags={"album": "The Bends", "artist": "Radiohead"},
                           cover="../../audio-source/SampleJPGImage_50kbmb.jpg")

# split sound in 5-second slices and export
for i, chunk in enumerate(sound[::5000]):  # slicing [start:end:step]
  with open("../../output/sound-%s.mp3" % i, "wb") as f:
    chunk.export(f, format="mp3")

print("--- %s seconds ---" % format(time.time() - start_time, '.2f'))

