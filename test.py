from multiprocessing import Process
import os
import time
import sys
import random

def info(title):
    print title
    print 'module name:', __name__
    print 'parent process:', os.getppid()
    print 'process id:', os.getpid()
    sleep = random.randrange(5)
    sleep = 5
    print "sleep for %s" % sleep
    time.sleep(sleep)

def f(name):
    info('function f')
    print 'hello', name

if __name__ == '__main__':
    info('main line')
    processes = []
    for i in range(100):
        p = Process(target=f, args=('bob %s'%i,))
        p.start()
        print "starting process %s" %(p.name)
        processes.append(p)
#        p.join()

    while processes:
        for p in processes:
            if not p.is_alive():
                p.join()
                print "process %s eneded" % (p.name)
                processes.remove(p)
            else:
                pass
                #print "process %s is running" % (p.name) 
