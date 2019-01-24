'''
    AudioSegment(…).dBFS
'''
from pydub import AudioSegment
from pydub.playback import play
# import time

# start_time = time.time()

sound = AudioSegment.from_file("../../audio-source/wave/a2002011001-e02.wav")
sound_mono = AudioSegment.from_file("../../audio-source/wave/mono_sample_tone.wav")


#dBFS는 시스템이 가지는 가장 큰 신호(가장 큰 숫자)를 0dBFS로 규정합니다.
# 그러므로 입력되는 신호들은 모두 0dBFS보다 작아야 하고 -10dBFS와 같이 음의 dB형태
loudness = sound.dBFS
# print(loudness)

# print("--- %s seconds ---" % format(time.time() - start_time, '.2f'))



'''
    AudioSegment(…).channels
'''

channel_count = sound.channels
channel_count_mono = sound_mono.channels
# print(channel_count) # 2
# print(channel_count_mono) # 1



'''
    AudioSegment(…).sample_width
    각 샘플의 바이트 수 (1은 8 비트를 의미하고, 2는 16 비트를 의미 함). 
    CD 오디오는 16 비트 (샘플 폭 2 바이트)
'''

bytes_per_sample = sound.sample_width
bytes_per_sample2 = sound_mono.sample_width
# print(bytes_per_sample) # 2
# print(bytes_per_sample2) # 1


'''
   AudioSegment(…).frame_rate
    
'''
frames_per_second = sound.frame_rate
frames_per_second2 = sound_mono.frame_rate
# print(frames_per_second)
# print(frames_per_second2)


'''
   AudioSegment(…).frame_width 
'''
bytes_per_frame = sound.frame_width
bytes_per_frame2 = sound_mono.frame_width
# print(bytes_per_frame)
# print(bytes_per_frame2)


'''
    rms, max , max_dBFS , duration_seconds, raw_data
'''
# loudness = sound.rms
# print(loudness)

# peak_amplitude = sound.max
# print(peak_amplitude)

# normalized_sound = sound.apply_gain(-sound.max_dBFS)
# print(normalized_sound)

# sound.duration_seconds == (len(sound) / 1000.0)
# print(sound.duration_seconds)

# raw_audio_data = sound_mono.raw_data
# print(raw_audio_data)

# number_of_frames_in_sound = sound_mono.frame_count()
# print(number_of_frames_in_sound) #  frames_per_second * duration



'''
    AudioSegment(…).append()
'''

# no crossfade
# no_crossfade1 = sound.append(sound_mono, crossfade=0)

# no crossfade
# no_crossfade2 = sound + sound_mono
# play(no_crossfade2)


'''
    AudioSegment(…).overlay()
'''

# played_togther = sound.overlay(sound_mono)
# play(played_togther)
# sound2_starts_after_delay = sound.overlay(sound_mono, position=5000)
# play(sound2_starts_after_delay)
# volume_of_sound1_reduced_during_overlay = sound.overlay(sound_mono, gain_during_overlay=-12)
# play(volume_of_sound1_reduced_during_overlay)
# sound2_repeats_until_sound1_ends = sound.overlay(sound_mono, loop=True)
# play(sound2_repeats_until_sound1_ends)
# sound2_plays_twice = sound.overlay(sound_mono, times=2)
# play(sound2_plays_twice)
# assume sound1 is 30 sec long and sound2 is 5 sec long:
# sound2_plays_a_lot = sound.overlay(sound_mono, times=10000)
# print(len(sound) == len(sound2_plays_a_lot))
# play(sound2_plays_a_lot)


'''
    AudioSegment(…).apply_gain(gain)
'''
# make sound1 louder by 3.5 dB
# louder_via_method = sound.apply_gain(+3.5)
# louder_via_operator = sound + 3.5

# make sound1 quieter by 5.7 dB
# quieter_via_method = sound.apply_gain(-5.7)
# quieter_via_operator = sound - 5.7


'''
    AudioSegment(…).fade()
    AudioSegment(…).fade_out()
    AudioSegment(…).fade_in()
'''
# fade_louder_for_3_seconds_in_middle = sound.fade(to_gain=+6.0, start=7500, duration=3000)
# fade_quieter_beteen_2_and_3_seconds = sound.fade(to_gain=-3.5, start=2000, end=3000)

# easy way is to use the .fade_in() convenience method. note: -120dB is basically silent.
# fade_in_the_hard_way = sound.fade(from_gain=-120.0, start=0, duration=5000)
# fade_out_the_hard_way = sound.fade(to_gain=-120.0, end=0, duration=5000)

# fade_in = sound.fade_in(5000)
# play(fade_in)


'''
    AudioSegment(…).reverse()
'''

# reverse_sound = sound.reverse()
# play(reverse_sound)


'''
    AudioSegment(…).set_sample_width()
    AudioSegment(…).set_frame_rate()
    AudioSegment(…).set_channels()
    AudioSegment(…).split_to_mono()
'''

# monos = sound.split_to_mono()
# print(monos)


