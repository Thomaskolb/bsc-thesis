# Thomas Kolb s1027332
# This program interprets all the collected results from training and creates tensorboard log

import tensorflow as tf

logdir = "test/"
file_writer = tf.summary.create_file_writer(logdir + "/metrics")
with file_writer.set_as_default():
    tf.summary.scalar('test ding', 0.1, step=1)
    tf.summary.scalar('test ding', 0.3, step=1)
    tf.summary.scalar('test ding', 0.5, step=2)
    tf.summary.scalar('test ding', 0.8, step=3)
