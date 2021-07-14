# 进程特性————独立变量
import multiprocessing
import time

x = 0
# 必须把 x 放在公共区而非main区域，否则新线程无法寻到x


def h():
    global x
    for _ in range(0, 4):
        time.sleep(0.3)
        x += 1
    print(x)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=h)
    t2 = multiprocessing.Process(target=h)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)
# 最后结果是4,4,0——————多个进程创建独立内存空间，其中的变量重新创建
