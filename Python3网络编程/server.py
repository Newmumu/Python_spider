# encoding:utf-8
import socket

# 定义服务器套接字
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机地址
host = socket.gethostname()
# 指定服务器运行端口
port = 9999

# 将服务器套接字与主机地址及端口号进行绑定
serversocket.bind((host, port))

# 开始监听客户端的链接（最多可以接受5个客户端的连接）
serversocket.listen(5)

while True:
    # 接受客户端的连接，将连接对象及远程客户端地址分别保存在变量中
    conn, addr = serversocket.accept()
    # 输出远程客户端地址（明确其身份）
    print('连接地址:%s' % str(addr))
    # 输出欢迎语句
    msg_s = "欢迎访问的socket服务器！"
    conn.send(msg_s.encode('utf-8'))
    while True:
        # 接收从客户端发送来的消息，并输出到客户端
        msg_r = conn.recv(1024)
        print("客户端:%s" % msg_r.decode('utf-8'))
        if msg_r == 'q':
            conn.close()
            break

        # 定义服务器返回的数据，并发送回连接状态的客户端
        msg_s2 = input("服务器:")
        conn.send(msg_s2.encode('utf-8'))
        if msg_s2 == 'q':
            conn.close()
            break
    break

serversocket.close()
