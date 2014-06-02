#!/usr/bin/env python2.7

"""

Written by benaryorg (@benaryorg/binary@benary.org)

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class BrowserWidget(QWidget):

    def __init__(self,args,**kwargs):
        super(BrowserWidget,self).__init__()
        self.args=args
        if self.args.verbose:
            print 'ChatWidget: __init__'
        self.initUi()
        if self.args.verbose:
            print 'ChatWidget: finished'
        self.load('http://duckduckgo.com')

    def initUi(self):
        if self.args.verbose:
            print 'ChatWidget: initUi'

        layout=QGridLayout()

        self.edit=QLineEdit()
        self.connect(self.edit,SIGNAL('returnPressed()'),self.load)
        layout.addWidget(self.edit,1,0,1,4)

        self.button=QPushButton('Load')
        self.connect(self.button,SIGNAL('clicked()'),self.load)
        layout.addWidget(self.button,1,4,1,1)

        self.view=QWebView()
        self.page=QWebPage()
        self.view.setPage(self.page)
        layout.addWidget(self.view,2,0,5,0)

        self.setLayout(layout)

    def load(self,*largs):
        if self.args.verbose:
            print 'ChatWidget: load'
        text=self.edit.text()
        if 'https://' not in text[:8] and 'http://' not in text[:7]:
            text='http://'+text
        self.view.load(QUrl(text))
        self.edit.setText('')

    def retranslateUi(self):
        if self.args.verbose:
            print 'ChatWidget: retranslateUi'
        self.edit.setFocus()
