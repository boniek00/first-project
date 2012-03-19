#!/usr/bin/env python



import sys
import signal
import time
from subprocess import *
#from threading import Thread


def alarmSignalHandle(sig, arg2):
    print "Catch signal %s, \nraise an exception..." %(sig)
    raise Exception

def yourfunction(sec):
    time.sleep(sec)
    print "function was able to finish successfullyn\n"

print "start\n"
signal.signal( signal.SIGALRM, alarmSignalHandle )
signal.alarm(2)
#try:
#    t = Thread(target=yourfunction, args=(10,))
#    t.start()
#except Exception, e:
#    print "Got an exception %s\n" % (e)
#    t.join()



f =Popen(["sleep", "10"])
f.wait()
#time.sleep(10)

print "end\n"
