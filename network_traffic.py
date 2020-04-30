from scapy.all import *

iface = "[INSERT_INTERFACE]"
for pkt in sniff(iface = iface, count = 5):
    print('Packet: {} \n'.format(str(pkt.summary())))
