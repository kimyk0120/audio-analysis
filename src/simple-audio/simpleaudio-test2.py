
'''

    Playing audio directly , WaveObject’s
'''

import simpleaudio as sa


# play_obj = sa.play_buffer(audio_data, 2, 2, 44100) # bytes objects, Python arrays, and Numpy arrays all qualify.):
# wave_obj = sa.WaveObject(audio_data, 2, 2, 44100)

# wave_obj = sa.WaveObject.from_wave_file(path_to_file)
# play_obj = wave_obj.play()

# wave_read = wave.open(path_to_file, 'rb')
# wave_obj = sa.WaveObject.from_wave_read(wave_read)


'''
    Using Numpy
'''

import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.25
a = sample_rate * T
t = np.linspace(0, T, int(a), False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)

# concatenate notes
audio = np.hstack((A_note, Csh_note, E_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()




'''
    Playing an object supporting the buffer interface:
'''

# import simpleaudio as sa
# import wave
#
# wave_read = wave.open(path_to_file, 'rb')
# audio_data = wave_read.readframes(wave_read.getnframes())
# num_channels = wave_read.getnchannels()
# bytes_per_sample = wave_read.getsampwidth()
# sample_rate = wave_read.getframerate()
#
# wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
# play_obj = wave_obj.play()
# play_obj.wait_done()


