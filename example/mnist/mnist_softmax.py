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
import numpy as np
import tensorflow as tf
from time import sleep

np.set_printoptions(threshold=100)

FLAGS = None
def main(_):
    """get ai studio with tensorflow as backend"""
    studio = iv.AIStudio("tensorflow")
 
    # Import data
    mnist = input_data.read_data_sets(studio.DataFolder, one_hot=True)
    # Create the model

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

    #record computation graph
    studio.RecordGraphDef(sess.graph_def, "softmax")
    
    studio.AddRecordVariable(W, "w")
    studio.AddRecordImage(x, "input image")
    studio.AddRecordScalar(cross_entropy, "loss")
    
    summary = studio.GetRecordList()
    
    # Train
    for _ in range(20):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        c, ww, _ = sess.run([cross_entropy, W, train_step], feed_dict={x: batch_xs, y_: batch_ys})
        
        """record data for real-time view"""
        studio.RecordVariable(ww, "w")
        studio.RecordImage(batch_xs, "input image")
        studio.RecordScalar(c, "loss")
        #studio.SaveRecordList(summary_result)
    
    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    ac = sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels})
    #record results for plot
    studio.RecordScalar(ac, "accuracy(true)")
    studio.RecordScalar(1.0 - ac, "accuracy(false)")
   
    #inference
    draw = iv.IPDraw("Draw2D-1")
    image3 = iv.IPGraph("Image-3")
    plot3 = image3.Plots(0)
    print("Start inference, draw number using draw pad")
    for k in range(600):
        # get draw image
        image = draw.GetDrawImage(28*28, 28, 28, 1, False)
        image.astype(np.float32)
        image /= (-image.max())
        image += 1
        #draw the normalized image
        plot3.ImageColor(image, 28, 28)
        xx = np.expand_dims(image, axis=0)
        inference = tf.argmax(y, 1)
        yy, results = sess.run([y, inference], feed_dict={x: xx})
        print("You drawing is:", results)
        sleep(1)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)