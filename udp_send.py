import socket

# 定义服务器地址和端口
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8889

# 创建一个UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 准备要发送的数据
message = b'Hello, World!'

# 发送数据到服务器
sock.sendto(message, (SERVER_ADDRESS, SERVER_PORT))

# 关闭套接字
sock.close()