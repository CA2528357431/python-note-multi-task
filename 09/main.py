# 进程

# 进程是一个程序以及其调用的资源的综合，其基本操作同线程，地位高于线程,其内部可容纳多个线程

import multiprocessing


def do(x):
    print('x ' * x)


if __name__ == '__main__':
    pro = multiprocessing.Process(target=do, args=(3,))
    pro.start()

# 进程:  类比为 一个电脑上执行qq音乐和网易云音乐
#       每个程序至少有一个进程
#       有独立内存
#       cpu调度资源以此进程基准
# 线程:  类比为 qq音乐同时播放和下载音乐
#       每个进程至少有一个线程
#       与进程内的其他线程共享内存


# 协程参见 类升级