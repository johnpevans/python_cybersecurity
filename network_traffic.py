#!/usr/bin/env python3

import scapy.all
import sys

def interface(iface):
    #iface = "[INSERT_INTERFACE]"
    for pkt in sniff(iface = iface, count = 5):
        return 'Packet: {} \n'.format(str(pkt.summary()))


if __name__ == "__main__":
    iface = sys.argv[1]
    print(interface(iface))
    sys.exit(0)
