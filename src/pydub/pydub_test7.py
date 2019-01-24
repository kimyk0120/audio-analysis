'''
    AudioSegment.from_mono_audiosegments()
'''
from pydub import AudioSegment
from pydub.playback import play
import time

start_time = time.time()

left_channel = AudioSegment.from_wav("../../audio-source/wave/mono_sample_tone.wav")
right_channel = AudioSegment.from_wav("../../audio-source/wave/mono_sample_tone.wav")

stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

play(stereo_sound)

print("--- %s seconds ---" % format(time.time() - start_time, '.2f'))

