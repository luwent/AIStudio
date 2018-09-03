import bdb
import os

class Idb(bdb.Bdb):

    def __init__(self, gui):
        self.gui = gui
        self.allowstop = False
        bdb.Bdb.__init__(self)

    def user_line(self, frame):
        """This function is called when we stop or break at this line."""
        try:
            self.gui.interaction(frame)
        except:
            pass

    def user_exception(self, frame, info):
        """This function is called if an exception occurs,
        but only if we are to stop at or just below this level."""
        #self.gui.interaction(frame, info)
        pass
    def stop_here(self, frame):
        if not self.allowstop:
            return False
        return bdb.Bdb.stop_here(self, frame) 

    def break_here(self, frame):
        filename = frame.f_code.co_filename
        if not self.gui.isbreakname(filename):
            return False
        lineno = frame.f_lineno
        if not self.gui.isbreakline(filename, lineno):
            # The line itself has no breakpoint, but maybe the line is the
            # first line of a function with breakpoint set by function name.
            lineno = frame.f_code.co_firstlineno
            if not self.gui.isbreakline(filename, lineno):
                return False
        self.allowstop = True
        self.clear_all_breaks();
        self.set_break(filename, lineno)
        return bdb.Bdb.break_here(self, frame)

    def break_anywhere(self, frame):
        filename = frame.f_code.co_filename
        if not self.gui.isbreakname(filename):
            return False
        return True
       #return bdb.Bdb.break_anywhere(self, frame) 
