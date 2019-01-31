import librosa
from sklearn import linear_model

# Load the example clip
y, sr = librosa.load("../../audio-source/wave/Baby Crying-SoundBible.com-1143552027.wav")

'''
- - arguments 설명
- - - sr=22050 : input 샘플링 주파수입니다. 아마도 갖고있는 오디오 파일의 샘플링 주파수는 22050이 아닐 확률이 큽니다. 이렇게 값을 설정해주는 것은 11025 Hz 까지의 값만 써도 된다는 가정을 한 것이죠. 잘 모르시면 그냥 두세요.
- - - mono=True : 스테레오 음원일경우 모노로 바꿔준다는 말입니다. 역시 그냥 두시면 됩니다. 대부분의 경우 모노면 충분합니다. 이 글의 타겟이시면 스테레오 음원이 필요한 경우가 아닐거에요.
- - - offset, duration: 오디오 파일의 특정 구간만 쓰실경우 설정하시면 됩니다. 그러나, 초심자라면 이걸 쓰지 마시구요, 갖고있는 오디오 파일에서 의미있는 구간만 미리 잘라놓으세요. 예를들어 음원이 60초인데 아기 우는 소리가 20~35초에 있다면 그 부분만 남기고 나머지는 버려서 15초로 만들어놓고 쓰시면 됩니다.
'''

# print(y)
# print(sr)

mfcc = librosa.feature.mfcc(y=y,sr=sr) # 오디오 신호를 mfcc로 바꾼다.

'''
- - arguments 설명
- - - n_mfcc=20 : mfcc 계수의 개수입니다. mfcc가 가장 활발하게 쓰이는 음성 인식에서는 대략 이 값을 수십개 (20~50)로 설정하고 씁니다. 즉 그정도면 충분하다고 알려져있습니다. 다만 주어진 상황과 목표에 따라 그 값은 다를 수 있습니다. 우선 20으로 두시면 됩니다.
- - mfcc란?
- - mfcc는 음성/음악 인식에서 가장 널리 쓰이는 특징값입니다. 자세한 설명은 위키를 참조.
mfcc 프레임 기반 특징값입니다. 즉, 각 프레임 (대체로 수 십 ms)마다 하나의 mfcc vector가 나오게 됩니다.
위의 코드를 실행하면 mfcc는 2차원 어레이가 할당됩니다. 
'''

print(mfcc)
print(mfcc.shape) # (20, number_of_frames)


# logreg = linear_model.LogisticRegression()
# logreg.fit(X_train, y_train)
# y_test_estimated = logreg.predict(X_test)


