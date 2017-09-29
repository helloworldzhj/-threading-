#!/usr/bin/env python
#-*-coding:utf-8-*-

'''多进程中，同一个变量在每一个进程中独立拥有，互相之间没有干系，在多线程中，所有变量由所有线程共享，如果多个线程同时修改变量就乱套了。'''

'''import time,threading
balance = 0
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)'''

'''我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是由于线程的调度是由操作系统决定的，当t1，t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了
原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使简单的计算balance = balance + n也要拆成两句1.计算balance + n，存入临时变量中；2.将临时变量的值赋给balance。数据错误的原因：是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。

如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()'''

'''当多个线程同时执行lock，acquire时只有一个线程能成功的获取锁，然后继续执行代码，其他的线程只能等着指导锁被释放。
二获得锁的那个线程一定要记得释放锁，否则其他线程就要一直等待下去，成为死线程。所以我们用try。。。finally。。。来确保所最终一定会被释放。
所得好处如上，画出也有，首先是组织了多线程并发执行，包含锁得某段代码实际上只能以单线程模式执行，效率大大下降。其次由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方的锁，可能出现死锁，导致多个线程全部挂起，即不能执行，也无法结束，只能靠操作系统强制终止。'''

'''import threading,multiprocessing
def loop():
    x=0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()'''
'''启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。

ThreadLocal

在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：'''

import threading
local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello,%s(in%s)'%(std,threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
全局变量local_school就是一个thradlocal对象，每个thread对他都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都看成线程的局部变量，可以任意读写互不干扰，也不用管理锁的问题threadlocal内部会处理。全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

















