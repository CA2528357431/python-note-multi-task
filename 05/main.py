# 线程特性————共用变量
import threading
import time
x = 0
def h():
    global x
    for _ in range(0,4):
        time.sleep(0.3)
        x+=1
    print(x)
if __name__ == '__main__':

    t1 = threading.Thread(target=h)
    t2 = threading.Thread(target=h)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)
#最后结果是8——————多个线程公用一个内存空间，其中的变量自然也是公用