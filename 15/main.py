#  queue 通讯
import multiprocessing


def w(que: multiprocessing.Queue, x):
    while not que.full():
        que.put(x)


def r(que: multiprocessing.Queue):
    while not que.empty():
        a = que.get()
        print(a)


if __name__ == '__main__':
    que = multiprocessing.Queue(3)
    p = multiprocessing.Process(target=w, args=(que, 1))
    p.start()

    p.join()
    # 本例中 必须让第一个进程结束才能开始第二个，否则que中空空如也没法读取

    pp = multiprocessing.Process(target=r, args=(que,))
    pp.start()


