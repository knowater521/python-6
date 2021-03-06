import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys

# 1.中间层的作用是什么????????
# 2.把biase 去掉也不行

#使用numpy生成200个随机点
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

#定义两个placeholder
x = tf.placeholder(tf.float32, [None, 1]) #不确定行，一列和x_data形状一样
y = tf.placeholder(tf.float32, [None, 1])

#定义神经网络中间层
Weights_L1 = tf.Variable(tf.random_normal([1, 10])) #一行十列  代表一个输入，十个中间层
biases_L1 = tf.Variable(tf.zeros([1, 10]))
Wx_plus_b_L1 = tf.matmul(x, Weights_L1) + biases_L1
L1 = tf.nn.tanh(Wx_plus_b_L1)

#定义输出层
Weights_L2 = tf.Variable(tf.random_normal([10, 1]))
biases_L2 = tf.Variable(tf.zeros([1, 1]))
Wx_plus_b_L2 = tf.matmul(L1, Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

##############二次代价函数，训练过程就是训练4个变量Weights_L1， Weights_L2， biases_L1， biases_L2##############
loss = tf.reduce_mean(tf.square(y - prediction))#实际的值与预测的值的绝对值的平方##########预测里需要填充横坐标
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for i in range(2000):
		sess.run(train_step, feed_dict={x:x_data, y:y_data})
	
	#获得预测值 ###保存了训练的4个变量？？
	prediction_value = sess.run(prediction, feed_dict={x:x_data})#输入x坐标，得到预测值
	
	#画图
	plt.figure()
	plt.scatter(x_data, y_data)
	plt.plot(x_data, prediction_value, 'r-', lw = 5) #x_data是x坐标,prediction_value是y坐标
	plt.show()
	