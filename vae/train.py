import mnist
from model import *
import os
import shutil

LR = 0.05
BATCH_SIZE = 256
FINAL_STEP = 10000
CKPT_STEP = 10
CKPT_PATH = 'checkpoints'
RE_TRAIN = True


def main():
    if RE_TRAIN:
        shutil.rmtree(CKPT_PATH)
    if not os.path.exists(CKPT_PATH):
        os.mkdir(CKPT_PATH)

    model = VariationalAutoEncoder(X_SIZE, Z_SIZE, CKPT_PATH)
    data = mnist.load_data().train

    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graph', sess.graph)
        model.train(sess, data, FINAL_STEP, LR, BATCH_SIZE, CKPT_STEP)
        writer.close()

if __name__ == '__main__':
    main()