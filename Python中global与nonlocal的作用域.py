#!/usr/bin/env python
#-*-coding:utf-8-*-

#http://www.cnblogs.com/z360519549/p/5172020.html
'''gcount = 0#定义一个全局变量（在这儿省略了global关键字）

def global_test():
    gcount += 1
    print(gcount)
global_test()

这样是不行的，在函数中程序会因为“如果内部函数有引用外部函数的同名变量或者全局变量，并且对这个变量有修改，那么python会认为他是一个局部变量，又因为函数中没有gcount的定义和赋值，所以报错了。

二。声明全局变量，如果在局部要对全局变量修改，需要在局部也要先声明该全局变量
gcount = 0
def global_test():
    global gcount
    gcount += 1
    print(gcount)
global_test()
这个意思就是如果在函数中声明我们使用的是全局的变量gcount，我们就可以修改他了，然后在全局的时候也可以看到修改后的答案然后输出1

三如果在局部不声明全局变量，并且也不修改他，这样的话我们可以正常使用它，比如说打印啊之类的

gcount = 0
def global_test():
    print(gcount)
global_test()

四。nonlocal关键字用来在函数或其他作用域使用外层（非全层）变量
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
def make_counter_test():
    mc= make_counter()
    print(mc())
    print(mc())
    print(mc())
make_counter_test()

也就是说函数1里面的函数2 调用函数1里面定义的一个变量这个时候我就要使用nonlocal了然后就可以在函数2里面修改变量了


五
def scope_test():
    def do_local():
        spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_nonlocal():
        nonlocal  spam        #使用外层的spam变量
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    print(spam)
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)

scope_test()
print("In global scope:",spam)

在这个例子中可能情况就比较干脆了，1。刚开始输出一个原始的spam 2.后来他也没有声明nonlocal。global之类的然后就要该变量，这肯定是不行的，3.然后声明nonlocal，然后就依靠这这是函数1里面的函数2修改成功了，4.然后又声明全局变量，那我觉得他就是global的话就在全局声明了一个变量就在函数1外面就出现了一个新的全局spam但是在函数2里面想修改函数1的变量靠global是不行的，结果还是没有修改成功，5.不过也不是没有意义。在函数1外面也就是全局，生成了spam，然后在最后我在全局说那再来一个global的spam时。我就输出了spam

def add_b():
    global b
    b = 42
    def do_global():
        global b
        b= b + 10
        print(b)
    do_global()
    print(b)
add_b()
在函数add_b内global定义的变量b，只能在do_global内引用，如果do_global内修改，也必须要在do_global内声明global b表明是修改外面的全局变量b


global定义的变量，表明其作用域在局部以外，即局部函数执行完以后，不销毁函数内部以global定义的变量
def add_a():
    global a
    a = 3
add_a()
print(a)

def add_b():
    global b
    b = 42
    def do_global():
        #global b #如果我把它注释了就错了，因为global定义的b只能引用，不能修改
        b = b + 10
        print(b)
    do_global()
    print(b)
add_b()
print(b)

def add_b():
    global b
    b = 42
    def do_global():
        global a
        a = b + 10
        print(b)
    do_global()
    print(a)
add_b()
print('a= %s,b = %s'%(a,b))

def add_b():
    #global b
    b = 42
    def do_global():
        global b
        b = 10
        print(b)
    do_global()
    print(b)
add_b()
print(b)



def add_b():
    #global b
    b = 42
    def do_global():
        nonlocal b
        b = 10
        print(b)
    do_global()
    print(b)
add_b()


def add_b():
    #global b
    b = 42
    def do_global():
        nonlocal b
        b = 10
        print(b)
    do_global()
    print(b)
add_b()
#print(b)再加上这句话就是错的，因为nonlocal适用于在局部函数中的局部函数，把最内层的局部变量设置成外部局部可用，但还不是全局的


def add_b():
    #global b
    #b = 42
    def do_global():
        nonlocal b
        b = 10
        print(b)
    do_global()
    #print(b)
add_b()
他还是报错了，因为nonlocal要绑定一个局部变量





def add_b():
    #global b
    #b = 42
    def do_global():
        global b
        b = 10
        print(b)
    do_global()
    print(b)
add_b()
print(b)

def add_b():
    #global b
    #b = 42
    def do_global():
        global b
        b = 10
        print(b)
    do_global()
    print(b)
add_b()
b = b + 30
print(b)

def add_b():
    #global b
    #b = 42
    def do_global():
        global b
        b = 10
        print(b)
    do_global()
    b = b + 20
    print(b)
add_b()
b = b + 30
print(b)'''


def add_b():
    #global b
    b = 42
    def do_global():
        global b
        b = 10
        print(b)
    do_global()
    b = b + 20
    print(b)
add_b()
b = b + 30
print(b)























