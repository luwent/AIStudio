#! implemented based on python idle 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import interpreter as ip
import os
import os.path
import pprint
import inspect
import traceback
import IVStudio as iv
import debugger

_runconsole = iv.IPRun();

class _rstr(str):
    """String that doesn't quote its repr."""
    def __repr__(self):
        return self

class PYRunOutput:
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
        #if(self.type == 1):
        #    sys.__stderr__.write(s)
        #else:
        #    sys.__stdout__.write(s)
        return _runconsole.RunOutput(self.type, s)


class Debugger:
    def __init__(self):
        self.idb = debugger.Idb(self)
        self.interp = ip.PYInterpreter()
        self.interp.setdebugger(self);
        self.frame = None
        self.interacting = 0
   
    def close(self):
        self.idb.set_quit()
        return
     
    def start(self, filename):
        self.interp.execfile(filename)

    def run(self, *args):
        try:
            self.interacting = 1
            return self.idb.run(*args)
        finally:
            self.interacting = 0

    def __frame2fileline(self, frame):
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        return filename, lineno

    def show_stack(self):
        want = _runconsole.DebugInfoStatus(0, 0)
        if not want:
            return
        if self.frame:
            stack, index = self.idb.get_stack(self.frame, None)
            self.stack = stack
            for i in range(len(stack)):
                frame, lineno = stack[i]
                try:
                    modname = frame.f_globals["__name__"]
                except:
                    modname = "?"
                code = frame.f_code
                filename = code.co_filename
                funcname = code.co_name

                import linecache
                sourceline = linecache.getline(filename, lineno)
                sourceline = sourceline.strip()
                if funcname in ("?", "", None):
                   item = "%s, line %d: %s" % (modname, lineno, sourceline)
                else:
                   item = "%s.%s(), line %d: %s" % (modname, funcname,
                                                 lineno, sourceline)
                if i == index:
                   item = "> " + item
                _runconsole.DebugInfoOutput(0, item)

    def show_frame(self, stackindex):
        if stackindex >= 0 and stackindex < len(self.stack):
            stackitem = self.stack[stackindex]
            self.frame = stackitem[0]  # lineno is stackitem[1]
            self.show_locals()
            self.show_globals()

    def show_locals(self):
        want = _runconsole.DebugInfoStatus(1, 0)
        if not want:
            return
        if not self.frame:
            return
        if(self.frame.f_locals == self.frame.f_globals):
            return
        self.load_dict(1, self.frame.f_locals)

    def show_globals(self):
        want = _runconsole.DebugInfoStatus(2, 0)
        if not want:
            return
        if not self.frame:
            return
        self.load_dict(2, self.frame.f_globals)

    def load_dict(self, type, dict):
        keys_list = dict.keys()
        names = sorted(keys_list)
        for name in names:
            value = dict[name]
            svalue = repr(value)
            _runconsole.DebugInfoOutput(type, name + ":"  + svalue)

    def show_variable(self):
        index = 0;
        name = _runconsole.GetWatchVariable(index)
        while name != "":
            value = self._getval_except(name)
            type = self._gettype(value)
            n = self._getlength(value)
            _runconsole.DebugInfoOutput(3, name + ":"  + type + ":" + str(n) + ":" + repr(value))
            name = _runconsole.GetWatchVariable(index)
            index = index + 1

    def update_variable(self, status):
        name = _runconsole.GetWatchVariable(-1)
        if name != "":
            if status == 2:
                self._getexec_except(name)
            else:
                value = self._getval_except(name)
                type = self._gettype(value)
                n = self._getlength(value)
                _runconsole.DebugInfoOutput(3, name + ":"  + type + ":" + str(n) + ":" + repr(value))

    def _getexec_except(self, arg, frame=None):
        try:
            if frame is None:
                return exec(arg, self.frame.f_globals, self.frame.f_locals)
            else:
                return exec(arg, frame.f_globals, frame.f_locals)
        except:
            exc_info = sys.exc_info()[:2]
            print(exc_info)

    def _getval(self, arg):
        try:
            return eval(arg, self.frame.f_globals, self.frame.f_locals)
        except:
            exc_info = sys.exc_info()[:2]
            err = traceback.format_exception_only(*exc_info)[-1].strip()
            raise

    def _getval_except(self, arg, frame=None):
        try:
            if frame is None:
                return eval(arg, self.frame.f_globals, self.frame.f_locals)
            else:
                return eval(arg, frame.f_globals, frame.f_locals)
        except:
            exc_info = sys.exc_info()[:2]
            err = traceback.format_exception_only(*exc_info)[-1].strip()
            return _rstr('** raised %s **' % err)

    def _gettype(self, value):
        code = None
        # Is it a function?
        try:
            code = value.__code__
        except Exception:
            pass
        if code:
            return ('Function')
        # Is it an instance method?
        try:
            code = value.__func__.__code__
        except Exception:
            pass
        if code:
            return ('Method')
        # Is it a class?
        if value.__class__ is type:
            return ('Class')
        # None of the above...
        try:
           return type(value).__name__
        except:
            pass
        return " "

    def _getlength(self, value):
        try:
           return len(value)
        except:
            pass
        return 1

    def repr_pp(self, arg):
        """pp expression
        Pretty-print the value of the expression.
        """
        try:
            return pprint.pformat(self._getval(arg))
        except:
            pass

    def interaction(self, frame, info=None):
        self.frame = frame
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        basename = os.path.basename(filename)
        self.show_stack();
        self.show_locals();
        self.show_globals();
        self.show_variable()
        more = True
        while(more):
            more = False
            status = _runconsole.WaitAtBreakPoint(filename, lineno)
            if status == 1:
                self.idb.set_step() #Stop after one line of code
            elif status == 2:
                self.idb.set_next(self.frame) #Stop on the next line in or below the given frame.
            elif status == 3:
                self.idb.set_return(self.frame) #Stop when returning from the given frame
            elif status == 99: #quit debug
                self.idb.set_quit()
            elif status == -99: #exit running program
                self.idb.set_quit()
                os._exit(0)
            elif status >= 3000 and status <= 3100: #updae new watch variable
                self.update_variable(status - 3000)
                #lineno = -1
                more = True
            elif status >= 1000 and status < 2000: #change calling stack
                self.show_frame(status - 1000)
                code = self.frame.f_code
                filename = code.co_filename
                lineno = self.frame.f_lineno
                basename = os.path.basename(filename)
                more = True
            else:
                if not self.idb.breaks:
                    name, line = _runconsole.GetBreakPoint()
                    if(line >= 0):
                        self.idb.set_break(name, line);
                self.idb.set_continue()
        self.frame = None

    def isbreakname(self, name):
        return _runconsole.IsBreakPoint(name, -1)
 
    def isbreakline(self, name, lineno):
        return _runconsole.IsBreakPoint(name, lineno)

def main(filename, mode):
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    #save_stdin = sys.stdin
    sys.stdout = PYRunOutput(0)
    sys.stderr = PYRunOutput(1)
    #sys.stdin = self.stdin
    print(sys.argv)
    if(mode == '-d'):
        _runconsole.DebugStart()
        debugrun = Debugger()
        debugrun.start(filename)
        debugrun.close()
    else:
        print("Running...")
        interp = ip.PYInterpreter()
        interp.execfile(filename)
    sys.stdout = save_stdout
    sys.stderr = save_stderr
    #sys.stdin = save_stdin

if __name__ == "__main__":
    if len (sys.argv) >= 3:
        sys.path.append(os.path.dirname(sys.argv[1]))
        path0, filename0 = os.path.split(sys.argv[0])
        path1, filename1 = os.path.split(path0)
        sys.path.append(path1)
        rfile = sys.argv[1]
        mode = sys.argv[2]
        del sys.argv[2]
        del sys.argv[0]
        main(rfile, mode)
