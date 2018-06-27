#! implemented based on python idle 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from code import InteractiveInterpreter
import os
import os.path
from platform import python_version
import tokenize
import debugger
 
class PYInterpreter(InteractiveInterpreter):

    def __init__(self):
        locals = sys.modules['__main__'].__dict__
        InteractiveInterpreter.__init__(self, locals=locals)
  
    debugger = None

    def setdebugger(self, debugger):
        self.debugger = debugger

    def getdebugger(self):
        return self.debugger

    def execfile(self, filename, source=None):
        "Execute an existing file"
        if source is None:
            with tokenize.open(filename) as fp:
                source = fp.read()
        try:
            code = compile(source, filename, "exec")
        except (OverflowError, SyntaxError):
            self.resetoutput()
            print('*** Error in script or command!\n'
                 'Traceback (most recent call last):')
            InteractiveInterpreter.showsyntaxerror(self, filename)
            self.showprompt()
        else:
            self.runcode(code)

    def addsyspath(self, filename):
        "Prepend sys.path with file's directory if not already included"
        self.runcommand("""if 1:
            _filename = %r
            import sys as _sys
            from os.path import dirname as _dirname
            _dir = _dirname(_filename)
            if not _dir in _sys.path:
                _sys.path.insert(0, _dir)
            del _filename, _sys, _dirname, _dir
            \n""" % (filename,))

    def showtraceback(self):
        self.resetoutput()
        InteractiveInterpreter.showtraceback(self)

    def runcommand(self, code):
        "Run the code without invoking the debugger"
        # The code better not raise an exception!
        exec(code, self.locals)
        return 1

    def runcode(self, code):
        "Override base class method"
        debugger = self.debugger
        try:
            if debugger:
                debugger.run(code, self.locals)
            else:
                exec(code, self.locals)
        except SystemExit:
             raise
        except:
             self.showtraceback()
    def resetoutput(self):
        return
