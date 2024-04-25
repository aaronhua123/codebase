import time

# $ pip install pydivert


import pydivert

# with pydivert.WinDivert("tcp.DstPort == 80 or tcp.SrcPort == 5000") as w:
#
#     for packet in w:
#         print(packet)
#         w.send(packet)

        # break
#
# import pydivert
# # tcp.DstPort == 80 and
# with pydivert.WinDivert("ip.DstAddr == 183.2.172.42") as w:
#     for packet in w:
#         # if packet.dst_port == 1234:
#         #     print(">") # packet to the server
#         #     packet.dst_port = 80
#         # if packet.src_port == 80:
#         #     print("<") # reply from the server
#         print(packet)
#         # packet.src_addr = '127.0.0.1'
#         # packet.src_port = 5000
#         packet.dst_addr = '127.0.0.1'
#         packet.dst_port = 5000
#         # time.sleep(10)
#         print(packet)
#         # time.sleep(10)
#         w.send(packet)
#         # break


import pydivert
#
with pydivert.WinDivert("tcp.DstPort == 123 or tcp.SrcPort == 123") as w:

    for packet in w:
        # print('>>>>',
        #       'src_addr:%s'%packet.src_addr,
        #       'src_addr:%s'%packet.dst_addr,
        #       'ack:%s'%packet.tcp.ack,
        #       'syn:%s'%packet.tcp.syn,
        #       'fin:%s'%packet.tcp.fin,
        #       'ack_num:%s'%packet.tcp.ack_num,
        #       'cksum:%s'%packet.tcp.cksum,
        #       'payload:%s'%packet.tcp.payload,
        #       'dst_port:%s'%packet.tcp.dst_port,
        #       'src_port:%s'%packet.tcp.src_port,
        #       'data_offset:%s'%packet.tcp.data_offset,
        #       'control_bits:%s'%packet.tcp.control_bits,
        #       'header_len:%s'%packet.tcp.header_len,
        #       'payload:%s'%packet.payload,
        #       packet.protocol,
        #       '<<<<<',sep='\n')

        if packet.dst_port == 123:
            # print(">==",packet) # packet to the server
            packet.dst_port = 443
        if packet.src_port == 443:
            # print("<==", packet) # reply from the server
            packet.src_port = 123
        w.send(packet)