# 进程池

import multiprocessing
import time



def do(x):
    a=0
    for x in range(0,x+1):
        a+=x
    print(a)




if __name__ == '__main__':

    pool=multiprocessing.Pool(32)

    # 异步
    good1=time.time()
    for x in range(1000):
        pool.apply_async(func=do,args=(x,))
    good2=time.time()


    # 同步
    bad1=time.time()
    for x in range(1000):
        pool.apply(func=do,args=(x,))
    bad2=time.time()

    print('good: ',good2-good1)
    print('bad:  ',bad2-bad1)