
from pydub import AudioSegment
from pathlib import Path

sound1 = AudioSegment.from_file("audio-source/wave/a2002011001-e02.wav", format="wav")
sound2 = AudioSegment.from_file("audio-source/wave/littlewing.wav", format="wav")

# also supports the os.PathLike protocol for python >= 3.6
# wav_path = Path("path/to/sound.wav")
# wav_audio = AudioSegment.from_file(wav_path)

# raw 포맷은 명시 가능
# raw_audio = AudioSegment.from_file("/path/to/sound.raw", format="raw",
#                                    frame_rate=44100, channels=2, sample_width=2)

# use a file you've already opened (advanced …ish)
# with open("/path/to/sound.wav", "rb") as wav_file:
#     audio_segment = AudioSegment.from_file(wav_file, format="wav")

# sound1 6 dB louder, then 3.5 dB quieter
louder = sound1 + 10
quieter = sound1 - 3.5

# louder.export("output/louder.mp3",format="mp3")

# sound1, with sound2 appended
combined = sound1 + sound2

# sound1 repeated 3 times
repeated = sound1 * 3

# duration
duration_in_milliseconds = len(sound1)
# print(duration_in_milliseconds)

# first 5 seconds of sound1
beginning = sound1[:5000]

# last 5 seconds of sound1
end = sound1[-5000:]

# split sound1 in 5-second slices
slices = sound1[::5000]

# Advanced usage, if you have raw audio data:
# sound = AudioSegment(
#     # raw audio data (bytes)
#     data=b'…',
#
#     # 2 byte (16 bit) samples
#     sample_width=2,
#
#     # 44.1 kHz frame rate
#     frame_rate=44100,
#
#     # stereo
#     channels=2
# )

