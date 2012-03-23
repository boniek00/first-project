#!/usr/bin/env python
# coding: utf-8


"""
test unicode escape
tete
aaa
"""

import sys,os

if __name__ == "__main__":
    print sys.getdefaultencoding()
    
    try:
        a = unicode(sys.argv[1], encoding='utf8')
    except Exception, e:
        print "wyjątek: %s" %e
        sys.exit(-1)

    print a
    print a.encode('unicode_escape')


