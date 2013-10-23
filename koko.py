#!/usr/bin/env python
# coding: utf-8
import sys

def main():
    print "Hello"
    b = input('Izberete chislo 1: ')
    a = input('Izberete chislo 2: ')
    print 'Sumata e %s' % str(b+a)

    return 0

if __name__ == '__main__':
    sys.exit(main())