from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from AICommon.graph import Graph

def GetFramework(backend):
    return TensorflowGraph(backend)

class TensorflowGraph(Graph): 
    def __init__(self, backend):
        super(TensorflowGraph, self).__init__()
        self.studio = backend

    def ViewGraphDef(self, graph_or_graph_def):
        if isinstance(graph_or_graph_def, tf.Graph):
            tfgraph = graph_or_graph_def.as_graph_def()
        else:
            tfgraph = graph_or_graph_def
        self.studio.StartSaveGraphDef()
        for node in tfgraph.node:
            self.studio.AddNodeGraphDef(node.name, node.op)
            for input_full_name in node.input:
                self.studio.AddNodeInputGraphDef(input_full_name)
            for key, val in node.attr.items():
                self.studio.AddNodeAttrGraphDef(key, 0)
                """
                if val.HasField('s'):
                    self.studio.AddNodeAttrStringGraphDef(key, val)
                elif val.HasField('i'):
                    self.studio.AddNodeAttrIntGraphDef(key, val)
                elif val.HasField('f'):
                    self.studio.AddNodeAttrFloatGraphDef(key, val)
                elif val.HasField('b'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('type'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('shape'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('tensor'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('list'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('func'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                elif val.HasField('placeholder'):
                    self.studio.AddNodeAttrBoolGraphDef(key, val)
                    """
        self.studio.CloseNodeGraphDef()
