'''
    오디오 파일 목록 불러오기
    각 파일을 읽어서 스펙트럼으로 변환
    정규화를 위한 통계 누적
    변환된 파일을 저장하기
'''

import numpy # 수치 연산에 이용
import librosa # 음원 파일을 읽고 분석하는 데 이용
import os # 디렉토리 생성 등 시스템 관련 작업
import os.path # 특정 경로가 존재하는지 파악하기 위해 필요

sequence_length = 251
feature_dimension = 513

def extract_spectrum(part):
  sample_files = open(part + '_samples.txt').read().strip().split('\n') # 샘플 목록을 읽어옵니다.
  if part == 'train': # 'train'인 경우에는 평균과 표준편차를 구해야 합니다.
    data_sum = numpy.zeros((sequence_length, feature_dimension)) # 합계를 저장할 변수를 만듭니다.
    data_squared_sum = numpy.zeros((sequence_length, feature_dimension)) # 제곱의 합을 저장할 변수입니다.
  if not os.path.exists(part+'/spectrum/'): # 'spectrum' 디렉토리가 존재하지 않으면 만들어 줍니다.
    os.mkdir(part+'/spectrum/')
  for f in sample_files:
    print('%d/%d: %s'%(sample_files.index(f), len(sample_files), f)) # 현재 진행상황을 출력합니다.
    y, sr = librosa.load(part+'/audio/'+f+'.wav', sr=16000) # librosa를 이용해 샘플 파일을 읽습니다.
    D = librosa.stft(y, n_fft=1024, hop_length=256).T # short-time Fourier transform을 합니다.
    mag, phase = librosa.magphase(D) # phase 정보를 제외하고, 세기만 얻습니다.
    S = numpy.log(1 + mag * 1000) # 로그형태로 변환합니다.
    if part == 'train': # 'train'인 경우 합계와 제곱의 합을 누적합니다.
      data_sum += S
      data_squared_sum += S ** 2
    numpy.save(part+'/spectrum/'+f+'.npy', S) # 현재 샘플의 스펙트럼을 저장합니다.
  if part == 'train': # 모든 파일의 변환이 끝난 후에, 'train'인 경우 평균과 표준편차를 저장합니다.
    data_mean = data_sum / len(sample_files)
    data_std = (data_squared_sum / len(sample_files) - data_mean ** 2) ** 0.5
    numpy.save('data_mean.npy', data_mean)
    numpy.save('data_std.npy', data_std)

if __name__ == '__main__':
  for part in ['train', 'valid', 'test']:
    extract_spectrum(part)



