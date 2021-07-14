# 任务名

import time
import multiprocessing

import os


def dance():
    for _ in range(0, 5):
        print('dance')
        print('当前', multiprocessing.current_process())
        time.sleep(1.2)


def sing():
    for _ in range(0, 5):
        print('sing')
        print('当前', multiprocessing.current_process())
        time.sleep(1.8)


def main():
    t1 = multiprocessing.Process(target=dance)
    t2 = multiprocessing.Process(target=sing)
    t1.start()
    t2.start()
    for _ in range(0, 2):
        print('当前', multiprocessing.current_process())
        # 查看该语句所在线程
        # current_process 返回了一个Process对象

    t1.join()
    t2.join()
    print('_______')

    # 或者os模块


def dance1():
    for _ in range(0, 5):
        print('dance')
        print('当前   ', os.getpid())
        print('父进程  ', os.getppid())
        time.sleep(1.2)


def sing1():
    for _ in range(0, 5):
        print('sing')
        print('当前   ', os.getpid())
        print('父进程  ', os.getppid())
        time.sleep(1.8)


def main1():
    t3 = multiprocessing.Process(target=dance1)
    t4 = multiprocessing.Process(target=sing1)
    t3.start()
    t4.start()
    for _ in range(0, 2):
        print('当前', os.getpid())
        # 查看该语句所在线程
        # 返回了一个getpid  当前进程的id（int)
        # 返回了一个getppid 父进程的id（int)


if __name__ == '__main__':
    main()
    time.sleep(6)
    main1()
