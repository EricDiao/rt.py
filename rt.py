#!/usr/bin/env python


# This script provides a easy way to add route for my Linux router.
# run ./rt.py [network/host] ([interface] [gateway]), if the latter
# two parameter is not provided, this script will add route to the
# DEFAULT_INTERFACE.

import commands
import sys

VERSION = 'alpha 2017-8-3'
DEFAULT_INTERFACE = 'sfo0'
ROUTE_SH = "/home/pi/r.sh"

def gen_route(net,interface,gw):
    prefix = 'sudo route add'
    net_sec = ''
    if '/' in net :
        net_sec = " -net " + net
    else:
        net_sec = " -host " + net
    if gw :
        gw_sec = " gw " + gw
    else: gw_sec = ''
    return prefix + net_sec + " dev " + interface + gw_sec

def add_route(cmd):
    print cmd
    a,b = commands.getstatusoutput(cmd)
    print b
    return a

def write_route(cmd,path=ROUTE_SH):
    script = "echo "
    script = script +"'"+cmd+"' >> " + path
    a,b = commands.getstatusoutput(script)
    return a

if __name__ == '__main__':
    #print sys.argv
    #print sys.argv[1]
    if len(sys.argv) < 2:
        print 'No action specified.'
        sys.exit()
    if sys.argv[1] == 'version':
        print  VERSION
        sys.exit()
    net = sys.argv[1]
    if len(sys.argv) >= 3 :
        dev = sys.argv[2]
    else: dev = DEFAULT_INTERFACE
    if len(sys.argv) >= 4:
        gw = sys.argv[3]
    else: gw = False
    cmd = gen_route(net,dev,gw)
    add_route(cmd)
    write_route(cmd)
