#线程

#多任务并行处理，大大加快效率

import threading
from time import sleep,time



def slow():
    a=time()
    sleep(1)
    sleep(1.1)
    sleep(1.2)
    b=time()
    print(b-a)


def fast():
    x=threading.Thread(target=sleep,args=(1,))
    y=threading.Thread(target=sleep,args=(1.1,))
    z=threading.Thread(target=sleep,args=(1.2,))
    # 前者是目标函数，后者是参数

    a=time()

    #开启线程
    x.start()
    y.start()
    z.start()

    #等待线程结束
    x.join()
    y.join()
    z.join()

    b=time()

    print(b-a)

#必须由如下形式调用
if __name__ == '__main__':
    slow()
    fast()