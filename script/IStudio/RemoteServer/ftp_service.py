# Revised based on pyftpdlib.

import os
import sys
import shlex, subprocess
import time
from .config import *
from .ftp_filesystem import AbstractedFS
from .ftp_filesystem import FilesystemError
from . import IVGrpc_pb2

CHUNK_SIZE = 1024 * 1024  # 1MB

def _strerror(err):
    if isinstance(err, EnvironmentError):
        try:
            return os.strerror(err.errno)
        except AttributeError:
            # not available on PythonCE
            if not hasattr(os, 'strerror'):
                return err.strerror
            raise
    else:
        return str(err)
        
class FTPHandler():
 
    use_gmt_times = True
    unicode_errors = 'replace'
    running_process = {}

    def __init__(self, home):
        self.fs = AbstractedFS(home, self)
        self.perms = "dwr"
        self._current_facts = ['type', 'perm', 'size', 'modify']
        self._rnfr = None
        self._restart_position = 0

    def ftp_CMD(self, cmdID, info):
        if(cmdID == 1):
            return self.ftp_NLST(cmdID, info)
        elif(cmdID == 2):
            return self.ftp_MLST(cmdID, info)
        elif(cmdID == 3):
            return self.ftp_MLSD(cmdID, info)
        elif(cmdID == 4):
            return self.ftp_SIZE(cmdID, info)
        elif(cmdID == 5):
            return self.ftp_MDTM(cmdID, info)
        elif(cmdID == 6):
            return self.ftp_MKD(cmdID, info)
        elif(cmdID == 7):
            return self.ftp_RMD(cmdID, info)   
        elif(cmdID == 8):
            return self.ftp_DELE(cmdID, info)               
        elif(cmdID == 9):
            return self.ftp_RNFR(cmdID, info)  
        elif(cmdID == 10):
            return self.ftp_RNTO(cmdID, info) 
        elif(cmdID == 11):
            return self.ftp_PWD(cmdID, info)
        elif(cmdID == 99 or cmdID == 98 or cmdID == 97):
            return self.ftp_STOPRUN(cmdID, info)
        elif(cmdID >= 100):
            return self.ftp_RUN(cmdID, info)             
    
    def ftp_STOPRUN(self, cmdID, port):
        iport = int(port)
        task = FTPHandler.running_process.get(iport, None)
        if(task != None):
            if(cmdID == 98):
                task.kill()
                return 1, "terminated"
            elif(cmdID == 97):
                if(task.poll() == None):
                    return 0, "running"
                else:
                    return 1, "stopped"
            else: 
                task.wait()
                del(FTPHandler.running_process[iport])
                return 1, "end" 
        return 0, "no program"

    def ftp_RUN(self, cmdID, cmd): 
        if(len(FTPHandler.running_process) > max_data_port):
            for port in range(data_server_port, data_server_port + max_data_port):
                task = FTPHandler.running_process.get(port)
                if(task != None):
                    if(task.poll() != None): #terminated
                        del(FTPHandler.running_process[port])
        if(len(FTPHandler.running_process) > max_data_port):
            return 0, "Too many running instance"
        for port in range(data_server_port, data_server_port + max_data_port):
            if(port not in FTPHandler.running_process):
                break
        path0 = os.path.dirname(os.path.realpath(__file__))
        path1 = os.path.dirname(path0)
        run_file = os.path.join(path1, "run.py")
        command_line = "python "  + run_file +  " -w " + str(port) + " " + cmd
        try:
            if(os.sep == "\\"):
                command_list = shlex.split(command_line, posix=False)
            else:
                command_list = shlex.split(command_line, posix=True)
            proc = subprocess.Popen(command_list, shell = False)
            FTPHandler.running_process[port] = proc
            return port, "ok"
        except subprocess.SubprocessError as err:
            why = _strerror(err)
            return 0, "Error in starting program"   

    def ftp_LIST(self, cmdID, path, files):
        """Return a list of files in the specified directory to the client.
        """
        try:
            isdir = self.fs.isdir(path)
            if isdir:
                listing = self.fs.listdir(path)
                if isinstance(listing, list):
                    try:
                        # RFC 959 recommends the listing to be sorted.
                        listing.sort()
                    except UnicodeDecodeError:
                        # (Python 2 only) might happen on filesystem not
                        # supporting UTF8 meaning os.listdir() returned a list
                        # of mixed bytes and unicode strings:
                        # http://goo.gl/6DLHD
                        # http://bugs.python.org/issue683592
                        pass
                iterator = self.fs.format_list(path, listing)
            else:
                basedir, filename = os.path.split(path)
                self.fs.lstat(path)  # raise exc in case of problems
                iterator = self.fs.format_list(basedir, [filename])
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return why
        else:
            for f in iterator:
                b = files.add()
                b.basenam = f[0]
                b.perms = f[1]
                b.size = f[2]
                b.mtimestr = f[3]
            return "ok"

    def ftp_NLST(self, cmdID, path):
        """Return a list of files in the specified directory in a compact form to the client.
        """
        try:
            if self.fs.isdir(path):
                listing = list(self.fs.listdir(path))
            else:
                # if path is a file we just list its name
                self.fs.lstat(path)  # raise exc in case of problems
                listing = [os.path.basename(path)]
        except (OSError, FilesystemError) as err:
            return 0,  _strerror(err)
        else:
            data = ''
            if listing:
                try:
                    listing.sort()
                except UnicodeDecodeError:
                    # (Python 2 only) might happen on filesystem not
                    # supporting UTF8 meaning os.listdir() returned a list
                    # of mixed bytes and unicode strings:
                    # http://goo.gl/6DLHD
                    # http://bugs.python.org/issue683592
                    ls = []
                    for x in listing:
                        if not isinstance(x, unicode):
                            x = unicode(x, 'utf8')
                        ls.append(x)
                    listing = sorted(ls)
                data = '\r\n'.join(listing) + '\r\n'
            data = data.encode('utf8', self.unicode_errors)
            return cmdID, data

        # --- MLST and MLSD commands

    # The MLST and MLSD commands are intended to standardize the file and
    # directory information returned by the server-FTP process.  These
    # commands differ from the LIST command in that the format of the
    # replies is strictly defined although extensible.

    def ftp_MLST(self, cmdID, path):
        """Return information about a pathname in a machine-processable
        form as defined in RFC-3659.
        On success return the path just listed, else None.
        """
        line = self.fs.fs2ftp(path)
        basedir, basename = os.path.split(path)
        try:
            iterator =  self.fs.format_mlsx(basedir, [basename], self.perms,
                self._current_facts, ignore_err=False)
            data = "".join(iterator)
        except (OSError, FilesystemError) as err:
            return 0,  _strerror(err)
        else:
            return cmdID, data

    def ftp_MLSD(self, cmdID, path):
        """Return contents of a directory in a machine-processable form
        as defined in RFC-3659.
        On success return the path just listed, else None.
        """
        # RFC-3659 requires 501 response code if path is not a directory
        if not self.fs.isdir(path):
            return 0,  "501 No such directory."
        try:
            listing = self.fs.listdir(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0, why
        else:
            iterator = self.fs.format_mlsx(path, listing, self.perms, self._current_facts)
            data = "".join(iterator)
            return cmdID, data

    def ftp_RETR(self, file, context):
        """Retrieve the specified file (transfer from the server to the
        client).  On success return the file path else None.
        """
        rest_pos = self._restart_position
        self._restart_position = 0
        try:
            fd = self.fs.open(file, 'rb')
        except (EnvironmentError, FilesystemError) as err:
            why = _strerror(err)
            context.abort(3, why)
            return
        try:
            if rest_pos:
                # Make sure that the requested offset is valid (within the
                # size of the file being resumed).
                # According to RFC-1123 a 554 reply may result in case that
                # the existing file cannot be repositioned as specified in
                # the REST.
                ok = 0
                try:
                    if rest_pos > self.fs.getsize(file):
                        raise ValueError
                    fd.seek(rest_pos)
                    ok = 1
                except ValueError:
                    why = "Invalid parameter"
                except (EnvironmentError, FilesystemError) as err:
                    why = _strerror(err)
                if not ok:
                    fd.close()
                    context.abort(3, why)
                    return
            while True:
                piece = fd.read(CHUNK_SIZE);
                if len(piece) == 0:
                    fd.close()
                    return
                yield IVGrpc_pb2.PArray(value=piece)
            fd.close()
        except Exception as e:
            fd.close()
            return context.abort(3, str(e))

    def ftp_STOR(self, chunks, file, mode='w'):
        """Store a file (transfer from the client to the server).
        On success return the file path, else None.
        """
        # A resume could occur in case of APPE or REST commands.
        # In that case we have to open file object in different ways:
        # STOR: mode = 'w'
        # APPE: mode = 'a'
        # REST: mode = 'r+' (to permit seeking on file object)

        rest_pos = self._restart_position
        self._restart_position = 0
        if rest_pos:
            mode = 'r+'
        try:
            fd = self.fs.open(file, mode + 'b')
        except (EnvironmentError, FilesystemError) as err:
            why = _strerror(err)
            return 0, why

        try:
            if rest_pos:
                # Make sure that the requested offset is valid (within the
                # size of the file being resumed).
                # According to RFC-1123 a 554 reply may result in case
                # that the existing file cannot be repositioned as
                # specified in the REST.
                ok = 0
                try:
                    if rest_pos > self.fs.getsize(file):
                        raise ValueError
                    fd.seek(rest_pos)
                    ok = 1
                except ValueError:
                    why = "Invalid REST parameter"
                except (EnvironmentError, FilesystemError) as err:
                    why = _strerror(err)
                if not ok:
                    fd.close()
                    return 0, why  
            for chunk in chunks:
                fd.write(chunk.value)  
            fd.close() 
            return max(1, self.fs.getsize(file)), "ok"
        except Exception:
            fd.close()
            return 0, "error"

    def ftp_STOU(self,cmdID,  line):
        """Store a file on the server with a unique name.
        On success return the file path, else None.
        """
        # Note 1: RFC-959 prohibited STOU parameters, but this
        # prohibition is obsolete.
        # Note 2: 250 response wanted by RFC-959 has been declared
        # incorrect in RFC-1123 that wants 125/150 instead.
        # Note 3: RFC-1123 also provided an exact output format
        # defined to be as follow:
        # > 125 FILE: pppp
        # ...where pppp represents the unique path name of the
        # file that will be written.

        # watch for STOU preceded by REST, which makes no sense.
        if self._restart_position:
            self.respond("450 Can't STOU while REST request is pending.")
            return

        if line:
            basedir, prefix = os.path.split(self.fs.ftp2fs(line))
            prefix = prefix + '.'
        else:
            basedir = self.fs.ftp2fs(self.fs.cwd)
            prefix = 'ftpd.'
        try:
            fd = self.run_as_current_user(self.fs.mkstemp, prefix=prefix,
                                          dir=basedir)
        except (EnvironmentError, FilesystemError) as err:
            # likely, we hit the max number of retries to find out a
            # file with a unique name
            if getattr(err, "errno", -1) == errno.EEXIST:
                why = 'No usable unique file name found'
            # something else happened
            else:
                why = _strerror(err)
            self.respond("450 %s." % why)
            return

        try:
            if not self.authorizer.has_perm(self.username, 'w', fd.name):
                try:
                    fd.close()
                    self.run_as_current_user(self.fs.remove, fd.name)
                except (OSError, FilesystemError):
                    pass
                self.respond("550 Not enough privileges.")
                return

            # now just acts like STOR except that restarting isn't allowed
            filename = os.path.basename(fd.name)
            if self.data_channel is not None:
                self.respond("125 FILE: %s" % filename)
                self.data_channel.file_obj = fd
                self.data_channel.enable_receiving(self._current_type, "STOU")
            else:
                self.respond("150 FILE: %s" % filename)
                self._in_dtp_queue = (fd, "STOU")
            return filename
        except Exception:
            fd.close()
            raise

    def ftp_APPE(self, file):
        """Append data to an existing file on the server.
        On success return the file path, else None.
        """
        # watch for APPE preceded by REST, which makes no sense.
        if self._restart_position:
            return 0, "Can't APPE while REST request is pending."
        else:
            return self.ftp_STOR(file, mode='a')

    def ftp_REST(self, line):
        """Restart a file transfer from a previous mark."""
        try:
            marker = int(line)
            if marker < 0:
                raise ValueError
        except (ValueError, OverflowError):
            return 0, "Invalid parameter."
        else:
            self._restart_position = marker
            return 1, "Restarting at position %s." % marker

        # --- filesystem operations
    def ftp_PWD(self, cmdID, line):
        """Return the name of the current working directory to the client."""
        # The 257 response is supposed to include the directory
        # name and in case it contains embedded double-quotes
        # they must be doubled (see RFC-959, chapter 7, appendix 2).
        cwd = self.fs.cwd
        assert isinstance(cwd, str), cwd
        return cmdID, cwd

    def ftp_CWD(self, cmdID, path):
        """Change the current working directory.
        On success return the new directory path, else None.
        """
        # Temporarily join the specified directory to see if we have
        # permissions to do so, then get back to original process's
        # current working directory.
        # Note that if for some reason os.getcwd() gets removed after
        # the process is started we'll get into troubles (os.getcwd()
        # will fail with ENOENT) but we can't do anything about that
        # except logging an error.
        init_cwd = getcwdu()
        try:
            self.fs.chdir(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0, why
        else:
            cwd = self.fs.cwd
            assert isinstance(cwd, str), cwd
            if getcwdu() != init_cwd:
                os.chdir(init_cwd)
            return cmdID, cwd

    def ftp_CDUP(self, cmdID, path):
        """Change into the parent directory.
        On success return the new directory, else None.
        """
        # Note: RFC-959 says that code 200 is required but it also says
        # that CDUP uses the same codes as CWD.
        return self.ftp_CWD(path)

    def ftp_SIZE(self, cmdID, path):
        """Return size of file in a format suitable for using with
        RESTart as defined in RFC-3659."""

        # Implementation note: properly handling the SIZE command when
        # TYPE ASCII is used would require to scan the entire file to
        # perform the ASCII translation logic
        # (file.read().replace(os.linesep, '\r\n')) and then calculating
        # the len of such data which may be different than the actual
        # size of the file on the server.  Considering that calculating
        # such result could be very resource-intensive and also dangerous
        # (DoS) we reject SIZE when the current TYPE is ASCII.
        # However, clients in general should not be resuming downloads
        # in ASCII mode.  Resuming downloads in binary mode is the
        # recommended way as specified in RFC-3659.

        line = self.fs.fs2ftp(path)
        if not self.fs.isfile(self.fs.realpath(path)):
            why = "%s is not retrievable" % line
            return 0,  why
        try:
            size = self.fs.getsize(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0,  why
        else:
            return cmdID,  str(size)

    def ftp_MDTM(self, cmdID, path):
        """Return last modification time of file to the client as an ISO
        3307 style timestamp (YYYYMMDDHHMMSS) as defined in RFC-3659.
        On success return the file path, else None.
        """
        line = self.fs.fs2ftp(path)
        if not self.fs.isfile(self.fs.realpath(path)):
            why = "550 %s is not retrievable" % line
            return 0,  why
        if self.use_gmt_times:
            timefunc = time.gmtime
        else:
            timefunc = time.localtime
        try:
            secs = self.fs.getmtime(path)
            lmt = time.strftime("%Y%m%d%H%M%S", timefunc(secs))
        except (ValueError, OSError, FilesystemError) as err:
            if isinstance(err, ValueError):
                # It could happen if file's last modification time
                # happens to be too old (prior to year 1900)
                why = "Can't determine file's last modification time"
            else:
                why = _strerror(err)
            return 0,  why
        else:
            return cmdID,  lmt

    def ftp_MFMT(self, cmdID, path, timeval):
        """ Sets the last modification time of file to timeval
        3307 style timestamp (YYYYMMDDHHMMSS) as defined in RFC-3659.
        On success return the modified time and file path, else None.
        """
        # Note: the MFMT command is not a formal RFC command
        # but stated in the following MEMO:
        # https://tools.ietf.org/html/draft-somers-ftp-mfxx-04
        # this is implemented to assist with file synchronization

        line = self.fs.fs2ftp(path)

        if len(timeval) != len("YYYYMMDDHHMMSS"):
            why = "Invalid time format; expected: YYYYMMDDHHMMSS"
            return 0, why
        if not self.fs.isfile(self.fs.realpath(path)):
            return 0, "is not retrievable"
        if self.use_gmt_times:
            timefunc = time.gmtime
        else:
            timefunc = time.localtime
        try:
            # convert timeval string to epoch seconds
            epoch = datetime.utcfromtimestamp(0)
            timeval_datetime_obj = datetime.strptime(timeval, '%Y%m%d%H%M%S')
            timeval_secs = (timeval_datetime_obj - epoch).total_seconds()
        except ValueError:
            why = "Invalid time format; expected: YYYYMMDDHHMMSS"
            return 0, why
        try:
            # Modify Time
            self.fs.utime, path( timeval_secs)
            # Fetch Time
            secs = self.fs.getmtime(path)
            lmt = time.strftime("%Y%m%d%H%M%S", timefunc(secs))
        except (ValueError, OSError, FilesystemError) as err:
            if isinstance(err, ValueError):
                # It could happen if file's last modification time
                # happens to be too old (prior to year 1900)
                why = "Can't determine file's last modification time"
            else:
                why = _strerror(err)
            return 0, why
        else:
            return (cmdID, lmt)

    def ftp_MKD(self, cmdID, path):
        """Create the specified directory.
        """
        line = self.fs.fs2ftp(path)
        try:
            self.fs.mkdir(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0,  why
        else:
            # The 257 response is supposed to include the directory
            # name and in case it contains embedded double-quotes
            # they must be doubled (see RFC-959, chapter 7, appendix 2).
            why = ('"%s" directory created.' % line.replace('"', '""'))
            return cmdID,  why

    def ftp_RMD(self, cmdID, path):
        """Remove the specified directory.
        """
        if self.fs.realpath(path) == self.fs.realpath(self.fs.root):
            why = "Can't remove root directory."
            return 0,  why
        try:
            self.fs.rmdir(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0,  why
        else:
            return cmdID,  "Directory removed."

    def ftp_DELE(self, cmdID, path):
        """Delete the specified file.
        """
        try:
            self.fs.remove(path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0,  why
        else:
            return cmdID,  "File removed."

    def ftp_RNFR(self, cmdID, path):
        """Rename the specified (only the source name is specified
        here, see RNTO command)"""
        if not self.fs.lexists(path):
            return 0,  "No such file or directory."
        elif self.fs.realpath(path) == self.fs.realpath(self.fs.root):
            return 0,  "Can't rename home directory."
        else:
            self._rnfr = path
            return cmdID,  "Ready for destination name."

    def ftp_RNTO(self, cmdID, path):
        """Rename file (destination name only, source is specified with
        RNFR).
        On success return a (source_path, destination_path) tuple.
        """
        if not self._rnfr:
            return 0,  "Bad sequence of commands: use RNFR first."
        src = self._rnfr
        self._rnfr = None
        try:
            self.fs.rename(src, path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            return 0,  why
        else:
             return cmdID,  "Renaming ok."