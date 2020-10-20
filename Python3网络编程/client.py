# encoding:utf-8
import socket

# 建立客户端网络套接字（保持连接型 Transmission Controled Protocol）
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机地址
host = socket.gethostname()
# 指定想要连接的服务端端口
port = 9999
# 客户端尝试指定主机地址及端口进行网络连接
clientsocket.connect((host, port))
while True:	
	# 接收从服务器返回的数据（每次接收1024个字节的数据），并打印
	msg_r = clientsocket.recv(1024)
	print("服务器：", msg_r.decode('utf-8'))
	
	# 定义发送的文本信息到服务端
	msg_s = input('客户端：')
	# 客户端发送数据到服务端
	clientsocket.send(msg_s.encode('utf-8'))
	if msg_s == 'q':
		clientsocket.close()
		break

	
