#!/usr/bin/env python2.7

"""

Written by benaryorg (@benaryorg/binary@benary.org)

"""

import sys
from argparse import ArgumentParser
from PyQt4.QtGui import QApplication
from MainWindow import MainWindow

if __name__=='__main__':
    parser=ArgumentParser(description='A Browser')
    parser.add_argument('-v','--verbose',action='store_true',dest='verbose',default=False,help='Verbose Output')

    args=parser.parse_args()
    
    app=QApplication(sys.argv)
    win=MainWindow(args)
    win.show()
    sys.exit(app.exec_())
