import audioop
import wave

wf1 = wave.open("../../audio-source/wave/noexcuses.wav", 'rb')
wf2 = wave.open("../../audio-source/wave/littlewing.wav", 'rb')

a = wf1.getnchannels()
b = wf2.getnchannels()
print(a) # 2
print(b)

a = wf1.getsampwidth()
print(a) # 3

a = wf1.getframerate()
print(a) # 44100

a = wf1.getnframes()
b = wf2.getnframes()
print(a)
print(b)

a = wf1.getcomptype()
print(a) # 'NONE' is the only supported type

a = wf1.readframes(10)
b = wf2.readframes(10)
print(a)
print(b)

a = audioop.add(wf1.readframes(1000000),wf2.readframes(1000000),3)
# print(a)

ww = wave.open("../../audio-source/wave/audioop_add_test.wav",'w')
ww.setnchannels(2)
ww.setsampwidth(3)
ww.setframerate(44100)
ww.writeframesraw(a)

a = audioop.avg(wf1.readframes(2000),3)
print(a)

wf1.close()
wf2.close()


