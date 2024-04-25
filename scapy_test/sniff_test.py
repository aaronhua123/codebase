# coding=utf-8
from pprint import pprint

from scapy.all import *

### 嗅探一个包
# def packet_callbacke(packet):
#     print(packet.show())
#
#
# sniff(prn=packet_callbacke, count=1)


# coding=utf-8
from scapy.all import *
from scapy.layers.dns import DNS, DNSRR
from collections import defaultdict

from scapy.layers.inet import IP, UDP, TCP

dns_cache = defaultdict(set)
ip_to_host = defaultdict(set)


# 数据包回调函数
def packet_callback(pkt: Packet):
    print(pkt.sprintf("{TCP:%TCP.dport%}"))
    if pkt.haslayer(IP):
        ip_src: str = pkt[IP].src
        ip_dst = pkt[IP].dst

        flag = ' -> '
        if ip_dst.startswith(('192.', '172.')):
            ip_src, ip_dst = ip_dst, ip_src
            flag = ' <- '
        ip_src = ip_to_host.get(ip_src, ip_src)
        ip_dst = ip_to_host.get(ip_dst, ip_dst)
        if pkt.haslayer(UDP):
            if pkt.haslayer(DNS):
                if pkt[DNS].an:
                    rrname = pkt[DNS].an.rrname
                    account = pkt[DNS].ancount
                    for x in range(account):
                        rdata = pkt[DNSRR][x].rdata
                        if isinstance(rdata, str):
                            dns_cache[rrname].add(rdata)
                            ip_to_host[rdata].add(rrname)
                link = f'DNS {ip_src}{flag}{ip_dst}'
                print(link)
            else:
                link = f'UDP {ip_src}:{pkt[UDP].sport}{flag}{ip_dst}:{pkt[UDP].dport}'
                print(link)
        elif pkt.haslayer(TCP):  # pkt.haslayer(TCP):
            link = f'TCP {ip_src}:{pkt[TCP].sport}{flag}{ip_dst}:{pkt[TCP].dport}'
            print(link)
        else:
            print(pkt.layers(),pkt.show())



# 开启嗅探器

sniff(prn=packet_callback)
print('==============')
