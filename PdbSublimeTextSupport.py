import os
import os.path

from os.path import exists

def launch(self):
    frame, lineno = self.stack[self.curindex]
    filename = self.canonic(frame.f_code.co_filename)
    if exists(filename):
        url = "sblm://%s%%3A%d" % (filename, lineno,)
        command = 'subl -b --command \'open_protocol_url {"url": "%s"}\'' % (url,)
        os.system(command)

def preloop(self):
    launch(self)

def precmd(self, line):
    launch(self)
    return line
