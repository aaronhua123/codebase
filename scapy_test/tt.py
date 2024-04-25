import re
import time
from pprint import pprint

import psutil
import socket
#
# host_dict = {}
# def reverse_dns_lookup(ip_address):
#     temp = host_dict.get(ip_address)
#     if temp:
#         return temp
#
#     try:
#         hostname = socket.gethostbyaddr(ip_address)
#         host_dict[ip_address] = hostname[0]
#         return host_dict[ip_address]
#     except socket.herror as e:
#         print(e)
#         host_dict[ip_address] = ip_address
#         return host_dict[ip_address]
#
# print(reverse_dns_lookup('39.156.66.10'))
# # import pcap
# from scapy.all import *
from scapy.layers.inet import TCP, IP

# process_name = "chrome.exe"

# 使用进程ID创建一个psutil.Process对象


# 获取该进程的网络连接信息
# data = {
#
# }
#
# start = time.time()
# while True:
#     pids = [proc.info['pid'] for proc in psutil.process_iter(['pid', 'name']) if proc.info['name'] == process_name]
#     cons = [(pid, psutil.Process(pid)) for pid in pids]
#     for pid, p in cons:
#         if data.get(pid) is None:
#             data[pid] = set()
#         try:
#             connections = p.connections(kind='all')
#         except Exception as e:
#             print(e)
#             continue
#         # 打印网络连接信息
#         for conn in connections:
#             if conn.laddr and conn.raddr:
#                 l = reverse_dns_lookup(conn.laddr[0])
#                 r = reverse_dns_lookup(conn.raddr[0])
#                 data[pid].add(f"{l}:{conn.laddr[1]} -> {r}:{conn.raddr[1]}")
#     if time.time() - start > 3:
#         for k,v in data.items():
#             if v:
#                 print(k,v)
#         start = time.time()

# def packet_callback(packet: Packet):
#     print(packet)
#     for pid in pids:
#         print(psutil.Process(pid).connections(kind='all'))
#         # print(f"Captured packet: {packet}")
#     # if packet[TCP].payload:
#     #     mail_packet = str(packet[TCP].payload)
#     #     if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
#     #         print("[*] Server: %s" % packet[IP].dst)
#     #         print("[*] %s" % packet[TCP].payload)
#
#
# # 开启嗅探器
# sniff(filter="tcp port 443", prn=packet_callback, store=0)
# devs = pcap.findalldevs()
# print(*devs, sep='\n')
# pcap_session = pcap.pcap('\\Device\\NPF_{AEC98E4B-D4F5-4BD2-9B07-EEAE0F8EB7CD}', promisc=True, immediate=True)
# # pcap_session.setfilter('tcp port 443')
# for ts, pkt in pcap_session:
#     print(ts, pkt)
#     if pcap_session.datalink() == pcap.DLT_LINUX_SLL:
#         pkt = pkt[2:]
#     elif pcap_session.datalink() == pcap.DLT_EN10MB:
#         pkt = pkt[14:]
#     try:
#         if psutil.Process(pid).connections(kind='inet', _fd=pkt):
#             print(f"Captured packet: {pkt}")
#     except (psutil.AccessDenied, psutil.NoSuchProcess):
#         continue


# import pcap
#
# # list all of the Internet devices
# devs = pcap.findalldevs()
# print(*devs, sep='\n')
#
# pc = pcap.pcap(devs[3], promisc=True, immediate=True, timeout_ms=50)
# # fiter http pcakets
# pc.setfilter('tcp port 80')
# for ptime, pdata in pc:
#     print(ptime, pdata)
import subprocess

r = subprocess.Popen('chcp 65001 && netstat -ano', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# subprocess是python内置的模块，这个模块中的Popen可以查看用户输入的命令行是否存在

complie = re.compile(
    '([UDPTC]{3})\s{1,100}([0-9:\[\]\*\.]+)\s{1,100}([0-9:\[\]\*\.]+)\s{1,100}([A-Z_]*)\s{1,100}(\d+)')

import psutil


def get_process_name_by_pid(pid):
    try:
        process = psutil.Process(int(pid))
        return process.name()
    except psutil.NoSuchProcess:
        return None


# 示例使用
# pid = 1234  # 替换为你想查询的PID
# process_name = get_process_name_by_pid(pid)
# if process_name:
#     print(f"PID {pid} 的进程名称是: {process_name}")
# else:
#     print(f"没有找到PID {pid} 的进程")

for line in r.stdout.read().decode('utf-8').split('\n'):
    if line.startswith(('  TCP', '  UDP')):
        r = complie.search(line)
        if r:
            name = get_process_name_by_pid(r.group(5))
            dst_addr = r.group(3)
            if ':' in dst_addr:
                host, port = dst_addr.split(':')
            else:
                host = dst_addr
            try:
                dst_addr = socket.gethostbyaddr(host)
            except Exception as e:
                print(e)
            print(name, r.group(5), r.group(1), r.group(2), '->', dst_addr)
        else:
            print('xxx', line)
