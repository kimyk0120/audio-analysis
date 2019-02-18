import tensorflow as tf
import model
import data_provider

n_labels = data_provider.n_labels
batch_size = data_provider.batch_size
sequence_length = data_provider.sequence_length
feature_dimension = data_provider.feature_dimension


def train():
    data_provider.prepare_data()

    with tf.Graph().as_default():
        X = tf.placeholder(tf.float32, shape=(batch_size, sequence_length, feature_dimension, 1))
        Y = tf.placeholder(tf.int32, shape=(batch_size,))
        phase_train = tf.placeholder(tf.bool)

        output = model.get_model(X, phase_train, sequence_length, feature_dimension, n_labels)
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=output, labels=Y)
        loss = tf.reduce_mean(cross_entropy)
        evaluation = tf.reduce_sum(tf.cast(tf.nn.in_top_k(output, Y, 1), tf.float32))

        optimizer = tf.train.AdadeltaOptimizer(0.01)
        train_op = optimizer.minimize(loss)

        sess = tf.Session()
        sess.run(tf.local_variables_initializer())
        sess.run(tf.global_variables_initializer())
        accumulated_loss = 0

        for step in range(100000):
            x, y = data_provider.get_random_batch('nsynth-train')
            _, loss_value = sess.run([train_op, loss], feed_dict={phase_train:True, X:x, Y:y})
            accumulated_loss += loss_value
            if (step + 1) % 10 == 0:
                print('step %d, loss = %.5f'%(step+1, accumulated_loss / 10))
                accumulated_loss = 0
            if (step + 1) % 100 == 0:
                correct = 0;
                for i in range(10):
                  x, y = data_provider.get_random_batch('nsynth-valid')
                  corr = sess.run([evaluation], feed_dict={phase_train:False, X:x, Y:y})
                  correct += corr[0]
                print('step %d, valid accuracy = %.2f'%(step+1, 100 * correct / 10 / batch_size))

    saver = tf.Saver(tf.all_variables())
    saver.save(sess, 'model.ckpt')


if __name__ == '__main__':
    train()
