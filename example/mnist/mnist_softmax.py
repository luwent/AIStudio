# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.

See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import IStudio as iv
from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None
def main(_):
  a = tf.constant(1, name="a")
  b = tf.constant(2, name="b")
  c = tf.add(a, b, name="add")
  studio = iv.AIStudio("tensorflow")
  studio.RecordGraphDef(tf.get_default_graph())
 
  reg_g = tf.Graph()
  with reg_g.as_default():
     import numpy as np
     x_data = np.random.rand(100).astype(np.float32)
     y_data = x_data * 0.1 + 0.3
     W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
     b = tf.Variable(tf.zeros([1]))
     y = W * x_data + b
     loss = tf.reduce_mean(tf.square(y - y_data))
     optimizer = tf.train.GradientDescentOptimizer(0.5)
     train = optimizer.minimize(loss)
     studio.RecordGraphDef(tf.get_default_graph())
 
  # Import data
  mnist = input_data.read_data_sets(studio.DataFolder, one_hot=True)
  # Create the model
  with tf.name_scope('hidden') as scope:
      x = tf.placeholder(tf.float32, [None, 784], name="x")
      W = tf.Variable(tf.zeros([784, 10]), name="W")
      b = tf.Variable(tf.zeros([10]), name="b")
      y = tf.matmul(x, W) + b

  # Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  # tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  studio.RecordGraphDef(sess.graph_def)
  #return
  # Train
  for _ in range(20):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    c, ww, _ = sess.run([cross_entropy, W, train_step], feed_dict={x: batch_xs, y_: batch_ys})
    studio.RecordVariable("w", ww)
    studio.RecordImage("input image", batch_xs)
    studio.RecordScalar("loss", c)

  # Test trained model
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels})
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)