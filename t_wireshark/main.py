import pyshark
from pyshark.tshark.tshark import get_all_tshark_interfaces_names

all_interfaces_names = get_all_tshark_interfaces_names()
print(all_interfaces_names)
capture = pyshark.LiveCapture(interface='WLAN', display_filter='http or tls') #bpf_filter='tcp')
capture.sniff(packet_count=1)
for packet in capture.sniff_continuously():
    print('Just arrived:', packet)


# def print_callback(pkt):
#     print('Just arrived:', pkt)
#
# capture.apply_on_packets(print_callback, packet_count=1000)