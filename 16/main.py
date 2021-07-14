# 线程 获取返回值

import threading

def do(ar:list):
    return [max(ar),min(ar)]



class mypro(threading.Thread):
    def __init__(self,ar:list):
        super().__init__()
        self.result=None
        self.data=ar.copy()
    def run(self):
        self.result=do(self.data)
        print('done')
    def join(self):
        super().join()
        return self.result

if __name__ == '__main__':

    pr=mypro([1,8,2,7,-2])
    pr.start()
    re=pr.join()
    print(re)