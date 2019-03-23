"""
Start a stand alone GRPC server from the command line as in:

$ python server
"""

from concurrent import futures
import optparse
import os
import sys
import time
import grpc
import RemoteServer as rs
 
__ver__ = '1.0.0'
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class OptionFormatter(optparse.IndentedHelpFormatter):
    """Formats options shown in help in a prettier way."""

    def format_option(self, option):
        result = []
        opts = self.option_strings[option]
        result.append('  %s\n' % opts)
        if option.help:
            help_text = '     %s\n\n' % self.expand_default(option)
            result.append(help_text)
        return ''.join(result)
        
def serve(options):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service = rs.IVFTPService()
    if(options.username and options.password):
        service.auth.add_user(options.username, options.password, options.directory)
    rs.IVGrpc_pb2_grpc.add_FTPRPCServicer_to_server(service, server)
    server.add_insecure_port(rs.config.ftp_server_address + ':' + str(self.ftp_server_port))     
    server.start()
    try:
        print("server started")
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

def main():
    """Start a stand alone server."""
    usage = "python server [options]"
    parser = optparse.OptionParser(usage=usage, description=main.__doc__,
                                   formatter = OptionFormatter())
    parser.add_option('-v', '--version', action='store_true',
                      help="print server version and exit")
    parser.add_option('-V', '--verbose', action='store_true',
                      help="activate a more verbose logging")
    parser.add_option('-u', '--username', type=str, default=None,
                      help="specify username to login with (anonymous login "
                           "will be disabled and password required "
                           "if supplied)")
    parser.add_option('-w', '--password', type=str, default=None,
                      help="specify a password to login with (username "
                           "required to be useful)")
    parser.add_option('-d', '--directory', default=None, metavar="FOLDER",
                      help="specify the home directory (default current "
                           "directory)")
                           
    options, args = parser.parse_args()
    if options.version:
        sys.exit("server %s" % __ver__)

    if options.username:
        if not options.password:
            parser.error(
                "if username (-u) is supplied, password ('-w') is required")

    serve(options)

if __name__ == '__main__':
    main()