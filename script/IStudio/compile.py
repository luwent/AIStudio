from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import py_compile

def main(filename):
    py_compile.compile(filename)

if __name__ == "__main__":
    if len (sys.argv) == 2:
        main(sys.argv[1])
