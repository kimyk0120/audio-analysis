import os # 파일 목록을 구할 때 필요한 패키지


def gather_information(part): # part 인자에는 'train', 'valid', 'test' 등을 넣어줍니다.
    label_list = open('labels.txt').read().strip().split('\n') # labels.txt 파일을 읽어서 각 줄을 기준으로 나눕니다.
    files = [] # wav 파일의 목록
    labels = [] # 각 파일의 label
    all_files = os.listdir("../../audio-source/" + part + '/audio') # 각 part 아래 'audio' 안에 있는 파일의 목록을 불러옵니다.
    # print(len(all_files))
    for f in all_files: # all_files에 있는 각 파일들에 대해서
        if f[-4:] == '.wav': # 파일이 '.wav'로 끝나면
            files.append(f[:-4]) # files 목록에 추가하고,
            label = f.split('_')[0] # 파일의 가장 첫 단어를 잘라냅니다.
            if label == 'synth': # synth_lead의 경우는 두 단어로 이루어져 있으므로
                label = 'synth_lead' # 첫 단어가 synth인 경우에는 label 이름을 synth_lead로 바꿔줍니다.
            labels.append(label_list.index(label)) # 이제 label_list에서 label의 위치를 찾아서 labels에 추가합니다.

    file_out = open(part + '_samples.txt', 'w') # part+'_samples.txt' 에 파일 목록을 적어줍니다.

    for f in files:
        file_out.write(f + '\n')

    file_out.close()

    label_out = open(part + '_labels.txt', 'w') # label도 저장합니다.

    for l in labels:
        label_out.write(str(l) + '\n')

    label_out.close()


if __name__ == '__main__' :
    # pass
    gather_information('nsynth-train') # 위 함수를 'train', 'valid', 'test'에 대해 실행합니다.
    gather_information('nsynth-valid')
    gather_information('nsynth-test')

