"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import sys

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)

wf = wave.open("audio-source/wave/littlewing.wav", 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    # print(frame_count)
    # print(time_info)
    # print(status)
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)



# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

# start the stream (4)
stream.start_stream()

# time.sleep(5)
# stream.stop_stream()
# print(stream.is_stopped())
# print(stream.get_time())

# wait for stream to finish (5)
while stream.is_active():
    time.sleep(0.1)



# stop stream (6)
stream.stop_stream()
stream.close()
wf.close()

# close PyAudio (7)
p.terminate()