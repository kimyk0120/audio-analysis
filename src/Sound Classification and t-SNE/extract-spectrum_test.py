'''
    # 스펙트럼 추출하기
    오디오 파일 목록 불러오기
    각 파일을 읽어서 스펙트럼으로 변환
    정규화를 위한 통계 누적
    변환된 파일을 저장하기
'''

import numpy # 수치 연산에 이용
import librosa # 음원 파일을 읽고 분석하는 데 이용
import os # 디렉토리 생성 등 시스템 관련 작업
import os.path # 특정 경로가 존재하는지 파악하기 위해 필요

# 매 스펙트럼마다 1024 개의 샘플(기록)을 사용하고, 다음 스펙트럼은 256 샘플만큼 뒤에서 다시 추출합니다.
# 즉, 모든 스펙트럼은 자신과 인접한 스펙트럼과 768개의 샘플을 공유하게 됩니다.
# NSynth 데이터셋의 경우(전부 4초) 16,000 Hz로 일초에 16,000번 기록했다는 의미입니다.
# 전체 샘플 길이는 4초이니 각 샘플은 총 16,000 * 4 = 64,000개의 샘플
# 그러므로 64000을 256 개씩 넘어가며 스펙트럼을 추출
sequence_length = 251
# ?? 스펙트럼에 1024개의 샘플을 넣었기 때문에 결과로 나오는 한 스펙트럼은 513개의 값을 가집니다. ??
feature_dimension = 513


def extract_spectrum(part):
    # sample_files = open(part + '_samples.txt').read().strip().split('\n') # 샘플 목록을 읽어옵니다.
    testFileNm =  "bass_synthetic_059-025-025"
    print(testFileNm)

    # if part == 'nsynth-train': # 'train'인 경우에는 평균과 표준편차를 구해야 합니다.
        # data_sum = numpy.zeros((sequence_length, feature_dimension)) # 합계를 저장할 변수를 만듭니다.
        # data_squared_sum = numpy.zeros((sequence_length, feature_dimension)) # 제곱의 합을 저장할 변수입니다.


    # if not os.path.exists("../../audio-source/"+part+'/spectrum/'): # 'spectrum' 디렉토리가 존재하지 않으면 만들어 줍니다.
    #     os.mkdir("../../audio-source/"+part+'/spectrum/')
    # for f in sample_files:
    #     print('%d/%d: %s'%(sample_files.index(f), len(sample_files), f)) # 현재 진행상황을 출력합니다.
    #     y, sr = librosa.load("../../audio-source/"+part+'/audio/'+f+'.wav', sr=16000) # librosa를 이용해 샘플 파일을 읽습니다.
    #     D = librosa.stft(y, n_fft=1024, hop_length=256).T # short-time Fourier transform을 합니다.
    #     mag, phase = librosa.magphase(D) # phase 정보를 제외하고, 세기만 얻습니다.
    #     S = numpy.log(1 + mag * 1000) # 로그형태로 변환합니다.
    #     if part == 'nsynth-train': # 'train'인 경우 합계와 제곱의 합을 누적합니다.
    #         data_sum += S
    #         data_squared_sum += S ** 2
    #     numpy.save("../../audio-source/"+part+'/spectrum/'+f+'.npy', S) # 현재 샘플의 스펙트럼을 저장합니다.
    # if part == 'nsynth-train': # 모든 파일의 변환이 끝난 후에, 'train'인 경우 평균과 표준편차를 저장합니다.
    #     data_mean = data_sum / len(sample_files)
    #     data_std = (data_squared_sum / len(sample_files) - data_mean ** 2) ** 0.5
    #     numpy.save('data_mean.npy', data_mean)
    #     numpy.save('data_std.npy', data_std)


if __name__ == '__main__':
    for part in ['nsynth-train']:
        extract_spectrum(part)



