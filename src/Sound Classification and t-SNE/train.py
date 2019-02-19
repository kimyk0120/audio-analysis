import tensorflow as tf
import model
import data_provider


n_labels = data_provider.n_labels # 11
batch_size = data_provider.batch_size # 32
sequence_length = data_provider.sequence_length # 251
feature_dimension = data_provider.feature_dimension # 513


def train():
    data_provider.prepare_data() # 자료 목록 불러오기

    with tf.Graph().as_default(): # Graph객체
        X = tf.placeholder(tf.float32, shape=(batch_size, sequence_length, feature_dimension, 1))
        Y = tf.placeholder(tf.int32, shape=(batch_size,))
        phase_train = tf.placeholder(tf.bool)

        # output :  fc3의 출력으로 주어진 입력이 각 레이블에 속하는 악기의 소리일 확률을 나타냅니다.
        output = model.get_model(X, phase_train, sequence_length, feature_dimension, n_labels)

        #  모델의 출력 확률과 실제 레이블의 차이를 나타내는 크로스엔트로피
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=output, labels=Y)

        # 실제로는 각 배치에서 이 값의 평균을 취한 loss 노드의 값을 사용
        loss = tf.reduce_mean(cross_entropy)

        # 출력 확률이 제일 높은 악기가 실제 레이블과 일치하는지를 판단하는 evaluation
        evaluation = tf.reduce_sum(tf.cast(tf.nn.in_top_k(output, Y, 1), tf.float32))

        # loss, 즉 연산 결과와 실제 레이블의 차이를 최소로 줄여주도록 모델을 학습시키는 optimizer
        # Adadelta 기법을 사
        optimizer = tf.train.AdadeltaOptimizer(0.01)
        train_op = optimizer.minimize(loss)

        # 실제로 각 노드를 연산하는데 필요한 세션(Session)을 생성하고, 연산에 필요한 변수들의 값을 초기화
        sess = tf.Session()
        sess.run(tf.local_variables_initializer())
        sess.run(tf.global_variables_initializer())
        accumulated_loss = 0

        for step in range(100000):

            x, y = data_provider.get_random_batch('nsynth-train') # get_randome_batch 함수를 이용해 데이터를 불러오고
            # train_op와 loss값을 구하도록 연산
            # train_op 연산의 경우 실제로 어떤 값을 출력하는 것은 아니고, loss가 작아지도록 모델을 조금씩 변화시키게 됩니다.
            _, loss_value = sess.run([train_op, loss], feed_dict={phase_train:True, X:x, Y:y})
            # 연산한 loss 값은 accumulated_loss에 저장
            accumulated_loss += loss_value

            if (step + 1) % 10 == 0:
                # 매 10번째 단계에서는 누적된 loss값을 출력해 학습의 진행 정도를 확인
                print('step %d, loss = %.5f'%(step+1, accumulated_loss / 10))
                accumulated_loss = 0
            # 매 100단계는 ‘valid’ 데이터를 이용해 검증
            # 이 때는 loss 대신에 정확도인 evaluation 노드를 사용
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
