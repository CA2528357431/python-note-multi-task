#守护线程

import threading
import time

#默认条件下，即使主线程结束，子线程也进行
def h():
    for x in range(0,5):
        time.sleep(0.5)
        print(x)
    print('1 finish')

t1=threading.Thread(target=h)
t1.start()
time.sleep(1)
print('main stop')


time.sleep(5)
print('-'*10)

t2=threading.Thread(target=h)
t2.daemon=True
#使主线程的存否制约子线程
t2.start()
time.sleep(1)
print('main stop')