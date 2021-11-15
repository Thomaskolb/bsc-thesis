# Thomas Kolb s1027332
# This program interprets all the collected results from training and creates tensorboard log

import tensorboard as tf

sess = tf.Session()
logdir = "test/"
file_writer = tf.summary.SummaryWriter(logdir + "/metrics", sess.graph)
init = tf.initialize_all_variables()
sess.run(init)
with file_writer.set_as_default():
    tf.summary.scalar('test ding', 0.1, step=1)
    tf.summary.scalar('test ding', 0.3, step=1)
    tf.summary.scalar('test ding', 0.5, step=2)
    tf.summary.scalar('test ding', 0.8, step=3)
