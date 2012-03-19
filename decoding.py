#!/usr/bin/env python
# coding: utf-8

import sys,os

if __name__ == "__main__":
    print sys.getdefaultencoding()
    
    try:
        a = unicode(sys.argv[1])
    except Exception, e:
        print "wyjątek: %s" %e
        sys.exit(-1)

    print a
    print a.decode( 'unicode-escape' ).encode('utf8')



