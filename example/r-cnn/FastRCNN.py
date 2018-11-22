# from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
#to downalod rcnn_ssdlite_mobile.pb, rcnn_resnet50.pb, mask_rcnn_inceptionv2.pb

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import tensorflow as tf
import numpy as np
import IStudio as iv

studio = iv.AIStudio("tensorflow")
filename = inspect.getframeinfo(inspect.currentframe()).filename
dir_path     = os.path.dirname(os.path.abspath(filename))
mobile_file = dir_path + "\\rcnn_ssdlite_mobile.pb"
resnet_file = dir_path + "\\rcnn_resnet50.pb"
maskrnn_file = dir_path + "\\mask_rcnn_inceptionv2.pb"
label_file = dir_path + "\\mscoco_label_map.txt"
height, width = 800, 800
NUM_CLASSES = 90
max_boxes_to_draw = 100

#load label
with open(label_file) as f:
    label_list = f.read().splitlines() 
    
camera = iv.IPCamera("Camera-1")
camera.ClearBoundingBox()
input_img = np.zeros((1, height, width, 3), dtype=np.uint8)

#load forzen graph
studio.LoadGraphDef(maskrnn_file)

with tf.Session() as sess:
    studio.RecordGraphDef(sess.graph_def, "Fast R-CNN")
    # Get handles to input and output tensors
    ops = tf.get_default_graph().get_operations()
    all_tensor_names = {output.name for op in ops for output in op.outputs}
    tensor_dict = {}
    for key in [
        'num_detections', 'detection_boxes', 'detection_scores',
        'detection_classes', 'detection_masks'
    ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
            tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)

    image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

    # Run inference
    while(1):
        if(studio.GetKeyState(0x1B) < 0):
            break      
        camera.GetImage_uint8(input_img) 
        output_dict = sess.run(tensor_dict,  feed_dict={image_tensor: input_img})
        
        num_detections = int(output_dict['num_detections'][0])
        print(num_detections)
        output_classes = output_dict['detection_classes'][0].astype(np.uint8)
        
        output_boxes = output_dict['detection_boxes'][0]
        output_scores = output_dict['detection_scores'][0]
        if 'detection_masks' in output_dict:
            output_masks = output_dict['detection_masks'][0]
            
        if not max_boxes_to_draw:
            max_boxes_to_draw = output_boxes.shape[0]
        camera.ClearBoundingBox()   
        for i in range(min(max_boxes_to_draw, num_detections)):
            if output_classes[i] < len(label_list):
              name = label_list[output_classes[i]]
            else:
              name = 'N/A'
            if i < len(output_scores):
                name = '{}: {}%'.format(name, int(100 * output_scores[i]))
            print(output_boxes[i])
            camera.DrawBoundingBox(output_boxes[i][1].item(), output_boxes[i][0].item(), output_boxes[i][3].item(), output_boxes[i][2].item(), name, True)
            if 'detection_masks' in output_dict:
                camera.DrawMaskImage(output_masks[i], 0.5, 0x7F0000FF, output_boxes[i][1].item(), output_boxes[i][0].item(), output_boxes[i][3].item(), output_boxes[i][2].item(),  True)
        break