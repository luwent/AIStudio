from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class AIFramework(object):
    def ViewGraphDef(self,  graph, name):
        raise NotImplementedError

    def SetupCheckpoint(var_list=None):
        raise NotImplementedError

    def SaveCheckpoint(self,  sess, name):
        raise NotImplementedError

    def RestoreCheckpoint(self,  sess, name):
        raise NotImplementedError