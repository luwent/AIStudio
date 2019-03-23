from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from RemoteServer import config
if(config.is_remote_run):
    from RIVStudio import *
else:
    from IVStudio import *
from IVEnum import *
from AIStudio import *
