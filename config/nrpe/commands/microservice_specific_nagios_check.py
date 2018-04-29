#!/usr/bin/env python
from argparse import ArgumentParser
import sys

import grpc

# TODO: We could either package this script in the right spot relative to generated code
# Or install the client as a global - we'll need to have that ability regardless for our
# other types of boxes which need clients
from src.gen import route_guide_pb2
from src.gen import route_guide_pb2_grpc

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
    channel = grpc.insecure_channel('localhost:50051')
    stub = route_guide_pb2_grpc.RouteGuideStub(channel)
    status = get_service_status(stub)
    if status.status_code == 0:
        return 'OK', 'Everything is gucci'
    else:
        return 'CRITICAL', status.status


def get_service_status(stub):
    # TODO: This works, but not sure if it's a proper utilization of the Empty object
    status = stub.GetStatus(route_guide_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
    print('Status {} - {}'.format(status.status, status.status_code))

if __name__ == '__main__':
    try:
        nagios_code, message = main()
        print '%s - %s' % (nagios_code, message)
        sys.exit(NAGIOS_CODE[nagios_code])
    except:
        print 'CRITICAL - Nothing is gucci!'
        sys.exit(NAGIOS_CODE['CRITICAL'])
