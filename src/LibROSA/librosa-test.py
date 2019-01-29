# Beat tracking example
from __future__ import print_function
import librosa

# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y` # y - NumPy floating point array.
#    Store the sampling rate as `sr` # the number of samples per second of audio
y, sr = librosa.load("../../audio-source/wave/littlewing.wav")
# y, sr = librosa.load(filename, duration=5.0)
print(y)
print(sr)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)