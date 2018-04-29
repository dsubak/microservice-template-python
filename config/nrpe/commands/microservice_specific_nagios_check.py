#!/usr/bin/env python
from argparse import ArgumentParser
import sys

import redis

NAGIOS_CODE = {
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
    'UNKNOWN': 3,
    'DEPENDENT': 4,
}

def main():
    parser = ArgumentParser()

    parser.add_argument('--warning', type=int, dest='warning_threshold')
    parser.add_argument('--critical', type=int, dest='critical_threshold')

    return 'OK', 'Everything is gucci'


if __name__ == '__main__':
    try:
        nagios_code, message = main()
        print '%s - %s' % (nagios_code, message)
        sys.exit(NAGIOS_CODE[nagios_code])
    except:
        print 'CRITICAL - Nothing is gucci!'
        sys.exit(NAGIOS_CODE['CRITICAL'])
