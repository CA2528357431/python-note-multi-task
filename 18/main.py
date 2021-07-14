# pool  queue


import multiprocessing


def w(que, x):
    print('w')
    while not que.full():
        que.put('x' * x)
        print('w ok')


def r(que):
    print('r')
    while not que.empty():
        a = que.get()
        print(a)


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    que = multiprocessing.Manager().Queue(3)
    # 池中queue

    # 同步
    pool.apply(func=w, args=(que, 3))
    pool.apply(func=r, args=(que,))

    print('-' * 50)

    # 异步
    ww = pool.apply_async(func=w, args=(que, 4))
    ww.wait()
    #作用同join
    rr = pool.apply_async(func=r, args=(que,))

    pool.close()
    # 不再添加新工作，池子不再开放
    pool.join()
    # 等待池子任务结束————防止因主进程失效而导致子进程结束
