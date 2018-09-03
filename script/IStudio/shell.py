#! implemented based on python idle 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import os.path
from platform import python_version
import IVStudio as IP
import interpreter

_console = IP.IPShell();

class PYOutput:
    def __init__(self, type):
        self.type = type;
        self.closed = False;

    def writable(self):
        return True

    def flush(self):
        pass

    def write(self, s):
        if self.closed:
            raise ValueError("write to closed file")
        if type(s) is not str:
            if not isinstance(s, str):
                raise TypeError('must be str, not ' + type(s).__name__)
        return _console.ShellOutput(self.type, s)

class PyShell:
    def __init__(self):
        self.interp = interpreter.PYInterpreter()
        self.save_stdout = sys.stdout
        self.save_stderr = sys.stderr
        #self.save_stdin = sys.stdin

        self.stdout = PYOutput(0)
        self.stderr = PYOutput(1)
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        #sys.stdin = self.stdin
        self.resetbuffer()

    def resetbuffer(self):
        """Reset the input buffer."""
        self.buffer = []
       
    def resetoutput(self):
        return

    def close(self):
        sys.stdout = self.save_stdout
        sys.stderr = self.save_stderr
        #sys.stdin = self.save_stdin
        return
     
    COPYRIGHT = \
          'Type "copyright", "credits" or "license()" for more information.'

    def Run(self):
        self.resetoutput()
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = ">>> "
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = "... "
        print("Python %s on %s\n%s" % 
                         (sys.version, sys.platform, self.COPYRIGHT))
        print("\n")
        more = 0
        inputstatus = 0
        while 1:
            try:
                if more:
                    prompt = sys.ps2
                else:
                    prompt = sys.ps1
                try:
                    if(inputstatus == 0):
                        self.stdout.write(prompt)
                    inputstatus = 0
                    line, inputstatus = self.readinput()
                except EOFError:
                    print("\n")
                    break
                else:
                    if(inputstatus != 2 and inputstatus != 1):
                        more = self.push(line)
                        inputstatus = 0;
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0
            if(inputstatus == 1):
                 break
        print("Exit")
        return True
        
    def push(self, line):
        # Strip off last newline and surrounding whitespace.
        # (To allow you to hit return twice to end a statement.)
        i = len(line)
        while i > 0 and line[i-1] in " \t":
            i = i - 1
        if i > 0 and line[i-1] == "\n":
            i = i - 1
        while i > 0 and line[i-1] in " \t":
            i = i - 1
        if(i > 4):
            line = line[4:i]
        else:
            line = ""

        self.buffer.append(line)
        source = "\n".join(self.buffer)
        more = self.interp.runsource(source)
        if not more:
            self.resetbuffer()
        return more
       
    def readinput(self):
        return _console.ShellInput()

def main():
    console = PyShell()
    console.Run()
    console.close()

if __name__ == "__main__":
    path0, filename0 = os.path.split(sys.argv[0])
    path1, filename1 = os.path.split(path0)
    sys.path.append(path1)
    main()
