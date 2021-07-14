# 判断消息队列

import multiprocessing

que=multiprocessing.Queue(3)

for _ in range(3):
    que.put(1)
    judge=que.full()
    print('full:',judge)
    # 满否
    size=que.qsize()
    print('size:',size)
    # 队列长短

    print('-'*20)

for _ in range(3):
    que.get()
    judge = que.empty()
    print('empty:', judge)
    # 空否
    size = que.qsize()
    print('size:', size)

    print('-' * 20)