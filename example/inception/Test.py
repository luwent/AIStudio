#https://github.com/tensorflow/models/tree/master/research/slim
#to download inception_v3.ckpt

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import inspect
import numpy as np
import tensorflow as tf
import IStudio as iv

import inception_v3 as inception
import imagenet

slim = tf.contrib.slim
studio = iv.AIStudio("tensorflow")
filename = inspect.getframeinfo(inspect.currentframe()).filename
dir_path     = os.path.dirname(os.path.abspath(filename))
chkpt_file = dir_path + "\\inception_v3.ckpt"
batch_size = 2
height, width = 299, 299
num_classes = 1001

img_tensor = tf.placeholder(tf.float32, shape=(None, height, width, 3))

with slim.arg_scope(inception.inception_v3_arg_scope()):
    logits, end_points = inception.inception_v3(img_tensor, num_classes, is_training=False)

#predictions = tf.argmax(logits, 1)
predictions = end_points['Predictions']
saver = tf.train.Saver()
names = imagenet.create_readable_names_for_imagenet_labels()
camera = iv.IPCamera("Camera-1")
with tf.Session() as sess:
    studio.RecordGraphDef(sess.graph_def, "inception")
    saver.restore(sess, chkpt_file) 
    while(1):
        if(studio.GetKeyState(0x1B) < 0):
            break
        img = np.zeros((1, height, width, 3), dtype=np.float32)
        print("Get Image:")  
        camera.GetImage(img)
        print("calculating:")   
        pred_prob= sess.run(predictions, feed_dict={img_tensor:img})
        probabilities = pred_prob[0, 0:]
        sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]   
        print("result:")     
        for i in range(5):
            index = sorted_inds[i]
            print('Probability %0.2f%% => [%s]' % (probabilities[index], names[index]))