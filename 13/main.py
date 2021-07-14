# 消息队列——————进程之间的数据共享


import multiprocessing


class x:
    def __init__(self, r):
        self.r = r


que = multiprocessing.Queue(5)  # 数字指定队列中数据多少

que.put('sdfsff')
que.put(193)
que.put(True)
que.put([True, 13, 'yes'])
que.put(x(3))

for _ in range(5):
    a = que.get()
    print(a)
# 先进入队列的数据也先出队列,一旦取出后续数据补位

print('_'*50)

'''

此时如果继续get

a=que.get()

该进程（本例中为主进程）会在此堵塞，无法执行后续
直到que被加入一个新数据，从而将其取出

'''


'''
a=que.get_nowait()

get_nowait 不会和get一样等待，而会尝试直接读取数据，如果失败则报错

'''


'''

que.put('sdfsff')
que.put(193)
que.put(True)
que.put([True,13,'yes'])
que.put(x(3))
que.put('cool guy')

for _ in range (5):
    a=que.get()
    print(a)

在此情况下，该进程（本例中为主进程）会在此堵塞，无法执行后续for循环
直到que被取出一个数据，从而放入新数据

'''


'''

que.put('sdfsff')
que.put(193)
que.put(True)
que.put([True,13,'yes'])
que.put(x(3))

que.put_nowait('cool guy')

put_nowait 不会和put一样等待，而会尝试直接加入数据，如果失败则报错

'''
