__author__ = "LzyRapx"

import sys
import re
import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 9876

# 连接服务，指定主机和端口
s.connect((host,port))

# 接收小于 2000 字节的数据
msg = s.recv(2000)
s.close()

print(msg.decode('utf-8'))
