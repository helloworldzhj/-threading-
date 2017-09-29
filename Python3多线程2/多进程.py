#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import os

print('Process (%s) start...'% os.getpid())
pid = os.fork()
if pid == 0:
    print('i am child process (%s) and my parent is %s.'%(os.getpid()))
else:
    print('i (%s) just created a child process (%s).'% (os.getpid(),pid))'''

'''这个在windows上是运行不了的，因为windows没有fork调用。
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

multiprocessing
如果打算编写多进程的服务程序，multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个process类来代表一个进程对象，下面有一个例子。'''

'''from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))

if __name__ =='__main__':
    print('Parent process %s.'% os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('child process end')'''

'''创建子进程时，只要传入一个执行函数和函数的参数，创建一个process实例，用start（）方法启动，这样创建进程比fork（）还要简单，join（）方法可以等待子进程结束再继续往下运行，通常用于进程间的同步。'''



#pool
'''from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__ == '__main__':
    print('Parent process %s.'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')'''
'''对Pool对象调用join方法会等待所有子进程执行完毕，调用join之前必须先调用close（）之后就不能继续添加新的process了
请注意输出的结果，因为pool默认大小在我的电脑上是4，因此，此时最多执行4个进程，这是pool的有意设计，改成5，就可以同时跑进5个进程。由于pool的默认大小是cpu的核数，如果电脑是8核的就需要提交至少9个进程才能看到上面的等待结果。'''


'''子进程
 很多时候子进程并不是自身，而是一个完毕进程。我们创建了子进程后还需要控制子进程的输入和输出。
ubprocess模块可以让我们非常方便的启动一个子进程，然后控制其输入和输出
下面这个例子演示了如何在python代码中运行nslookup www.python.org 这和命令行直接运行的效果是一样的：'''
'''import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)'''


#如果子进程还需要输入，则可以通过communicate方法输入
'''import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)'''

'''进程间通信
process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。python的multiproceing模块包装了底层的机制，提供了queue。pipes等多种方式来交换数据。
我们以queue为例，在父进程中创建了两个子进程，一个往queue里写数据，一个从queue里读数据'''

'''from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...'% value)
        q.put(value)
        time.sleep(random.random()*20)

def read(q):
    print('Process to read:%s'% os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.'% value)

if __name__ =='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()'''
'''在unix/Linux下，multiprocessing模块封装了fork（）调用，我们不需要关注fork细节，由于Windows没有fork调用，因此，multiprocessing需要模拟出fork的效果，父进程所有python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing再windows下调用失败了，要先考虑是不是pickle失败了
小结
在unix/linux下，可以使用fork（）调用实现多进程
要实现跨平台的多进程，可以使用multiprocessing模块
进程间通信是通过queue，pipes等实现的。'''















