#!/usr/bin/env python2.7

"""

Written by benaryorg (@benaryorg/binary@benary.org)

"""

from BrowserWidget import BrowserWidget
from PyQt4.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self,args):
        super(MainWindow,self).__init__()
        self.args=args
        if self.args.verbose:
            print 'MainWindow: __init__'
        self.title='Main Window'
        self.initUi()
#        self.statusBar().showMessage('Ready')
        if self.args.verbose:
            print 'MainWindow: finished'

    def initUi(self):
        if self.args.verbose:
            print 'MainWindow: initUi'
        self.resize(640,400)
        self.center()

#        self.toolbar=self.addToolBar('Exit')
#        self.toolbar.setMovable(False)
#
#        action=self.toolbar.addAction('&Quit')
#        action.setShortcut('Ctrl+Q')
#        action.setStatusTip('Exit application')
#        action.setIcon(QIcon.fromTheme('application-exit'))
#        action.triggered.connect(self.quit)

        self.setCentralWidget(BrowserWidget(self.args))

        self.retranslateUi()

    def center(self):
        if self.args.verbose:
            print 'MainWindow: center'
        gm=self.frameGeometry()
        gm.moveCenter(QApplication.desktop().screenGeometry(QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())).center())
        self.move(gm.topLeft())

    def retranslateUi(self):
        if self.args.verbose:
            print 'MainWindow: retranslateUi'
        self.setWindowTitle(self.title)
        self.centralWidget().retranslateUi()

    def closeEvent(self,event):
        event.ignore()
        self.quit()

    def quit(self):
        if self.args.verbose:
            print 'MainWindow: quit'
        qApp.quit()

