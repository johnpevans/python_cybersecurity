import scapy
from subprocess import call

call('netsh wlan show networks mode=Bssid')
