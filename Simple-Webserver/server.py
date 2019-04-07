__author__ = "LzyRapx"

import socket
import sys
import re

host = socket.gethostname()
port = 9876

# 创建 socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

print("Server Started")
while True:
    # 建立客户端连接
    client, address = serversocket.accept()
    print("连接地址: {}".format(address))
    # 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量
    print("Socket Connecting")
    msg = '你正在连着服务端！'+"\r\n"
    client.send(msg.encode('utf-8'))
    client.close()




