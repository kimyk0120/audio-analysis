# from pyaudio import pyaudio_play
from pydub import AudioSegment

# Open file
song = AudioSegment.from_mp3('../../audio-source/mp3/noexcuses.mp3')

# Slice audio
# pydub는 milliseconds 단위를 사용한다

ten_seconds = 10 * 1000
one_min = ten_seconds * 6


first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]

# up/down volumn
beginning = first_10_seconds + 6


# Save the result
# can give parameters-quality, channel, etc
beginning.export('../../output/result.wav', format='wav', parameters=["-q:a", "10", "-ac", "1"])

# change stereo to mono
# sound = AudioSegment.from_wav("audio-source/wave/littlewing.wav")
# sound = sound.set_channels(1)
# sound.export("output/path.wav", format="wav")

fPath = "../../output/result.wav"

# play result
# player = pyaudio_play.Audio_play()
# player.play(fPath)