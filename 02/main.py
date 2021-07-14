#任务名

import time
import threading

def dance():
    for _ in range(0,5) :
        print('dance')
        print('当前',threading.current_thread())
        time.sleep(1.2)
def sing():
    for _ in range(0,5):
        print('sing')
        print('当前',threading.current_thread())
        time.sleep(1.8)
if __name__ == '__main__':
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    t3 = threading.Thread(target=sing)
    t1.start()
    t2.start()
    t3.start()
    for _ in range(0,2):
        time.sleep(1.5)
        li=threading.enumerate()
        print(li)
        # 查看活跃线程

        print('当前', threading.current_thread())
        # 查看该语句所在线程
        # current_thread 返回了一个Thread对象



    print('_______')


#并发：
#任务多于cpu核心时，通过高速在所有任务之间轮换，达成‘看似同时进行多任务’的状态
#并行：
#任务不多于cpu核心时，真的同时进行多任务