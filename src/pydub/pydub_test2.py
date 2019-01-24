from pydub import AudioSegment
from pydub.playback import play

wav_path = "../../audio-source/wave/noexcuses.wav"
mp3_path = "../../audio-source/mp3/noexcuses.mp3"

song = AudioSegment.from_wav(wav_path)
song_second = AudioSegment.from_mp3(mp3_path)

# pydub does things in milliseconds
ten_seconds = 10 * 1000

first_10_seconds = song_second[:ten_seconds]

last_5_seconds = song_second[-5000:]


# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3


# Concatenate audio
# output_path = 'output/without_the_middle.wav'
# without_the_middle = beginning + end
# without_the_middle.duration_seconds == 15.0
# without_the_middle.export(output_path, format='wav', parameters=["-q:a", "10", "-ac", "1"])

# backwards = song_second.reverse()

# Crossfade
with_style = beginning.append(end, crossfade=1500)
output_path = '../../output/with_style.wav'
with_style.export(output_path, format='wav', parameters=["-q:a", "10", "-ac", "1"])


# Repeat
do_it_over = with_style * 2
output_path = '../../output/do_it_over.wav'
do_it_over.export(output_path, format='wav', parameters=["-q:a", "10", "-ac", "1"])


# Fade
awesome = do_it_over.fade_in(10000).fade_out(3000)
output_path = '../../output/awesome.wav'
awesome.export(output_path, format='wav', parameters=["-q:a", "10", "-ac", "1"])


# Save the results (again whatever ffmpeg supports)
awesome.export("../../output/mashup.mp3", format="mp3")

# play # need ffmpeg set up
play(awesome)

