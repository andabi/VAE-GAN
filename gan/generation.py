import mnist
from model import *
import tensorflow as tf

CASE = 'default'
CKPT_PATH = 'checkpoints/' + CASE
GRAPH_PATH = 'graphs/' + CASE
NUM_GEN = 100
CODE_SIZE = 128


def main():
    gen = Generator(CODE_SIZE, NUM_GEN)
    disc = Discriminator(batch_size=NUM_GEN)
    gd = GD(gen, disc, CKPT_PATH)

    data = mnist.load_data().test

    config = tf.ConfigProto(
        device_count={'GPU': 0},
        # log_device_placement=True
    )

    with tf.Session(config=config) as sess:
        writer = tf.summary.FileWriter(GRAPH_PATH, sess.graph)

        # x = np.random.normal(0, 1, (NUM_GEN, X_SIZE))
        # d = gd.discriminate(sess, x)
        # print 'random_image\tmean:{:2.4f}\tstd:{:2.4f}\n{}'.format(np.mean(d), np.std(d), d)
        #
        x = gd.generate(sess, NUM_GEN)
        # d = gd.discriminate(sess, x)
        # print 'fake_image\tmean:{:2.4f}\tstd:{:2.4f}\n{}'.format(np.mean(d), np.std(d), d)

        # x, _ = data.next_batch(NUM_GEN)
        # d = gd.discriminate(sess, x)
        # print 'real_image\tmean:{:2.4f}\tstd:{:2.4f}\n{}'.format(np.mean(d), np.std(d), d)

        x = tf.reshape(x, [NUM_GEN, 28, 28, 1])
        image_summary = tf.summary.image('generated_image', x, NUM_GEN)
        summary = sess.run(image_summary)
        writer.add_summary(summary)

        writer.close()

if __name__ == '__main__':
    main()