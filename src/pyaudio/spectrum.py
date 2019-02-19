import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# variable for Audio
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
sample = np.zeros([102400])
t = np.arange(0, 102400)
freq = np.fft.rfftfreq(1024, 1 / RATE)
spec = np.zeros([1024], dtype=complex)

pa = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    global sample, start_time, spec

    in_data = np.fromstring(in_data, np.float32)

    for i in np.arange(99, 0, -1):
        sample[i * 1024:(i + 1) * 1024] = sample[(i - 1) * 1024:i * 1024]
    sample[0:1024] = in_data

    # fourier transform
    spec = np.fft.rfft(sample[0:1024])
    spec = np.sqrt(spec.real ** 2 + spec.imag ** 2)

    return (in_data, pyaudio.paContinue)


stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 output=True,
                 stream_callback=callback)

# variable for Animation
fig = plt.figure()
ax1 = fig.add_subplot(211, xlim=(0, 102400), ylim=(-0.02, 0.02))
line1, = ax1.plot([], [])

ax2 = fig.add_subplot(212, xlim=(0, 3000), ylim=(0, 2))
line2, = ax2.plot([], [])


def init():
    return (line1, line2)


def update(frame):
    line1.set_data(t, sample)
    line2.set_data(freq, spec)
    return (line1, line2)


ani = FuncAnimation(fig, update, frames=100, interval=50,
                    init_func=init, blit=True)

stream.start_stream()
plt.show()
stream.stop_stream()
print("stream stopped")
stream.close()
print("stream closed")
pa.terminate()
