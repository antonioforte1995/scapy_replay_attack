from scapy.all import *
from scapy.utils import rdpcap

# sniffs the first 4 icmp packets specifing Google host 
packets = sniff(filter='icmp[icmptype] == icmp-echo and host 8.8.8.8', count = 4)

#replay sniffed packets
for pkt in packets:
     sendp(pkt)
