import numpy
import random

n_labels = 11   # 라벨
batch_size = 32
sequence_length = 251
feature_dimension = 513


def prepare_data():
    global train_samples, train_labels, valid_samples, valid_labels, test_samples, test_labels, data_mean, data_std

    train_samples = open('nsynth-train_samples.txt').read().strip().split('\n')
    train_labels = [int(label) for label in open('nsynth-train_labels.txt').read().strip().split('\n')]

    valid_samples = open('nsynth-valid_samples.txt').read().strip().split('\n')
    valid_labels = [int(label) for label in open('nsynth-valid_labels.txt').read().strip().split('\n')]

    test_samples = open('nsynth-test_samples.txt').read().strip().split('\n')
    test_labels = [int(label) for label in open('nsynth-test_labels.txt').read().strip().split('\n')]

    data_mean = numpy.load('data_mean.npy')
    data_std = numpy.load('data_std.npy')


def get_random_sample(part):
    global train_samples, train_labels, valid_samples, valid_labels, test_samples, test_labels, data_mean, data_std

    if part == 'nsynth-train':
        samples = train_samples
        labels = train_labels
    elif part == 'nsynth-valid':
        samples = valid_samples
        labels = valid_labels
    elif part == 'nsynth-test':
        samples = test_samples
        labels = test_labels
    else:
        print('Please use train, valid, or test for the part name')

    i = random.randrange(len(samples))
    spectrum = numpy.load("../../audio-source/"+part+'/spectrum/'+samples[i]+'.npy')
    spectrum = (spectrum - data_mean) / (data_std + 0.0001)
    return spectrum, labels[i]


def get_sample_at(part, i):
    global train_samples, train_labels, valid_samples, valid_labels, test_samples, test_labels, data_mean, data_std

    if part == 'nsynth-train':
        samples = train_samples
        labels = train_labels
    elif part == 'nsynth-valid':
        samples = valid_samples
        labels = valid_labels
    elif part == 'nsynth-test':
        samples = test_samples
        labels = test_labels
    else:
        print('Please use train, valid, or test for the part name')

    spectrum = numpy.load("../../audio-source/"+part+'/spectrum/'+samples[i]+'.npy')
    spectrum = (spectrum - data_mean) / (data_std + 0.0001)
    return spectrum, labels[i]


def get_random_batch(part):
    X = numpy.zeros((batch_size, sequence_length, feature_dimension, 1))
    Y = numpy.zeros((batch_size,))
    for b in range(batch_size):
        s, l = get_random_sample(part)
        X[b, :, :, 0] = s[:sequence_length, :feature_dimension]
        Y[b] = l
    return X, Y


# if __name__ == '__main__':
#     prepare_data()
#     get_random_sample("nsynth-test")

