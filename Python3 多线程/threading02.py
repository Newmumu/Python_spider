# encoding:utf8
"""
__author__ : weilinlin
__file__   : threading02
__time__   : 2020-10-22
线程同步
避免多个线程对同时对同一个数据进行修改，
Thread对象的Lock和Rlock可以简单实现线程同步，两个对象都有acquire和release方法，
那些同时仅需要一个线程操作的数据，可以将对其的操作放入到acquire和release之间；
"""
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)  # 调用Thread类自身的初始化方法
        self.threadId = threadID
        self.name = name
        self.delay = delay

    def run(self):
        # 重写Thread类的run方法
        print('开启线程:' + self.name)
        # 获取锁, 用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()  # 定义线程锁实例
threads = []    # 定义线程集

# 创建新线程（参数分别为：ThreadID， ThreadName， 延迟-等待时间delay）
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启新线程
thread1.start()     # 启动线程1
thread2.start()     # 启动线程2

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for thread in threads:
    thread.join()  # join 一个线程就先等待这个线程完成执行，再获取下一个线程句柄并执行
print('退出主线程')
