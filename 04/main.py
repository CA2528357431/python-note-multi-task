#自定义线程类

import threading
import time

class tp(threading.Thread):

    def __init__(self,x:list):
        super().__init__()
        self.x=x.copy()
    def run(self):
        for x in range(0,max(self.x)):
            time.sleep(0.5)
            print('doing........'+str(x))



if __name__ == '__main__':
    a=tp([1,5,3])
    a.start()
    # run 的重写相当于指定了 target
    #也可以传参

