# encoding:utf8
"""
__author__ : weilinlin
__file__   : threading03
__time__   : 2020-10-23
线程优先级队列
"""
import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print('开启线程:' + self.name)
        process_data(self.name, self.q)
        print('退出线程:' + self.name)


def process_data(threadName, q):
    while not exitFlag:  # 退出标识为真（1，则不进入循环）
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s process %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ['Thread-1', 'Thread-2', 'Thread-3']  # 定义线程名 集合
nameList = ['One', 'Two', 'Three', 'Four', 'Five']  # 定义data输出集合
queueLock = threading.Lock()  # 定义线程锁
workQueue = queue.Queue(10)  # 定义队列（使用Queue，先入先出队列）

threads = []  # 定义线程句柄集合
threadID = 1  # 定义线程ID初始值

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    """
    1, Thread-1, workQueue
    # 2, Thread-2, workQueue
    # 3, Thread-3, workQueue
    """
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

print("退出主线程")
