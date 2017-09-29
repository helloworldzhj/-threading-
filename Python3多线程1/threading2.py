#!/usr/bin/env python
#-*-coding:utf-8-*-
#线程模块
#使用thrading模块创建线程

import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('开始线程:'+self.name)
        print_time(self.name,self.counter,5)
        print('退出线程：'+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()
thread1.join()
thread1.join()
print('退出主线程')

'''我们可以通过直接从threading.Thread继承创建一个新的子类，并实例化后调用start（）方法启动新的线程，即它调用了线程的run（）方法
python3有两个标准库_thread和threading提供对线程的支持
_thread提供了低级别的，原始的线程以及一个简单的锁，它相比于threading模块的功能还是有限的
threading模块除了包含_thread模块中的所有方法外，还提供了其他方法
threading.currentThread()
threadingenumerate()
threading.activeCount()
除此之外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法；
run()
start()
join([time])
isAlive()
getName()
setName()'''


























