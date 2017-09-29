#!/usr/bin/env python
#-*-coding:utf-8-*-

'''多线程

多任务可以由多进程完成，也可以由一个进程内的多线程完成。进程是由若干线程组成的，一个进程至少有一个线程。

由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread 和 threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：'''


import time ,threading
def loop():
    print('thread %s is running...'% threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'% threading.current_thread().name)

print('thread %s is running...'% threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s is ended' % threading.current_thread().name)

#由于任何进程默认会启动一个线程，我们把该线程称为主线程，主线程又可以启动新线程，python的threading模块有current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫做mainthread，子线程的名字在创建时指定，我们用loopthread命名子线程，名字仅在打印时用来显示，完全没有其他意义 ，如果不起名字，python就会自动给线程命名thread-1,thread-2...


























