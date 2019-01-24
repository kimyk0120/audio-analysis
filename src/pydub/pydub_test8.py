'''
    AudioSegment.silent()
'''
from pydub import AudioSegment
from pydub.playback import play
import time

start_time = time.time()

ten_second_silence = AudioSegment.silent(duration=10000)
ten_second_silence.export("../../output/silence_10_second.mp3",format="mp3")

# play(ten_second_silence)

print("--- %s seconds ---" % format(time.time() - start_time, '.2f'))




