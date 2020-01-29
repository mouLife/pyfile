import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
# tensoflow 通过张量构建计算图，用会画来启动各个结点
a = tf.constant([[1.2,12]])
b = tf.constant([[5.3],[2.2]])
y = tf.matmul(a,b)
with tf.Session() as sess:
    print(sess.run(y))