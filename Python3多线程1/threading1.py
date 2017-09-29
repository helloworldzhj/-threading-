#!/usr/bin/env python
#-*-coding:utf-8-*-
#开始学习python
import _thread
import time

def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (threadName,time.ctime(time.time()) ))

try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
except:
    print("Error:无法启动线程")

while 1:
   pass

'''python中使用线程有两种方式，函数或者用类来包装线程对象。
函数式：调用_thread模块中的start_new_thread()函数来产生新线程。
_thread.start_new_thread(function,args[,kwargs])
function-线程函数
args - 传递给线程函数的参数，它必须是一个tuple类型
kwargs - 可选参数'''

