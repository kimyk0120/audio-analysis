import tensorflow as tf


def get_model(X, is_training, sequence_length, spectrum_size, n_labels):
    last_layer, last_minus_one_layer = get_model_and_activation(X, is_training, sequence_length, spectrum_size, n_labels)
    return last_layer


def get_last_minus_one(X, is_training, sequence_length, spectrum_size, n_labels):
    last_layer, last_minus_one_layer = get_model_and_activation(X, is_training, sequence_length, spectrum_size, n_labels)
    return last_minus_one_layer


def get_model_and_activation(X, is_training, sequence_length, spectrum_size, n_labels):
    conv1 = tf.contrib.layers.conv2d(X, 64, (3, spectrum_size), padding='VALID', normalizer_fn=tf.contrib.layers.batch_norm, normalizer_params={"is_training":is_training})
    pool1 = tf.contrib.layers.max_pool2d(conv1, (3, 1), stride=3)
    conv2 = tf.contrib.layers.conv2d(pool1, 64, (3, 1), normalizer_fn=tf.contrib.layers.batch_norm, normalizer_params={"is_training":is_training})
    pool2 = tf.contrib.layers.max_pool2d(conv2, (3, 1), stride=3)
    conv3 = tf.contrib.layers.conv2d(pool2, 128, (3, 1), normalizer_fn=tf.contrib.layers.batch_norm, normalizer_params={"is_training":is_training})
    pool3 = tf.contrib.layers.max_pool2d(conv3, (3, 1), stride=3)
    conv4 = tf.contrib.layers.conv2d(pool3, 128, (3, 1), normalizer_fn=tf.contrib.layers.batch_norm, normalizer_params={"is_training":is_training})
    pool4 = tf.contrib.layers.max_pool2d(conv4, (3, 1), stride=3)
    flatten = tf.contrib.layers.flatten(pool4)
    fc1 = tf.contrib.layers.fully_connected(flatten, 256)
    fc2 = tf.contrib.layers.fully_connected(fc1, 256)
    fc3 = tf.contrib.layers.fully_connected(fc2, n_labels)
    return fc3, fc2
