import socket

# 创建UDP Socket对象
tdp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置本地IP和端口号
local_ip = '127.0.0.1'
local_port = 5000

# 将Socket绑定到指定的IP和端口上
tdp_sock.bind((local_ip, local_port))
print("等待数据...")
tdp_sock.listen(5)
while True:
    # 从网络中接收数据并返回发送者的地址和端口号
    conn, addr = tdp_sock.accept()
    while True:
        data = conn.recv(8)
        print("Received message from {}: {}".format(addr, data.decode()))
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World')
    conn.close()