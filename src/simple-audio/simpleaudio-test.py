'''
    Simpleaudio supports standard integer PCM formats -
    basically what is usually contained in a plain WAV file.
    8, 11.025, 16, 22.05, 32, 44.1, 48, 88.2, 96 및 192 kHz의 샘플 속도가 허용됩니다
'''


# import simpleaudio.functionchecks as fc
# fc.LeftRightCheck.run()


import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("../../audio-source/wave/a2002011001-e02.wav")
play_obj = wave_obj.play()
play_obj.wait_done()


