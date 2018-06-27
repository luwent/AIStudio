from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from IVStudio.AIStudio import *

def ViewGraphDef(graph_or_graph_def):
    if isinstance(graph_or_graph_def, tf.Graph):
        tfgraph = graph_or_graph_def.as_graph_def()
    else:
        tfgraph = graph_or_graph_def
    studio.StartSaveGraphDef()
    for node in tfgraph.node:
      studio.AddNodeGraphDef(node.name, node.op)
      for input_full_name in node.input:
          studio.AddNodeInputGraphDef(input_full_name)
      for key, val in node.attr.items():
          studio.AddNodeAttrGraphDef(key, 0)
      studio.CloseNodeGraphDef()
