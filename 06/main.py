# 共用变量问题————资源竞争
import threading


def h1():
    global xx
    for _ in range(0, 1000000):
        xx += 1


def do1():
    li = []
    for _ in range(10):
        t = threading.Thread(target=h1)

        li.append(t)
    for x in li:
        x.start()
    for x in li:
        x.join()

    # 理论值 10,000,000    实际   3,500,000左右
    # 同一个瞬间 x 被多个线程同时调用造成了误差


def h2():
    global yy
    global mylock
    for _ in range(0, 1000000):
        mylock.acquire()
        yy += 1
        mylock.release()

    # 同步：同时间只能做一件事，效率低但安全
    # 异步：同时间分别做不同的事，效率高但不安全

    # 添加一个锁，使得 调用y成为同步过程，即y在同一时间只能被一个线程访问,防止原来问题发生

    # 别忘了解锁


def do2():
    li = []
    for _ in range(10):
        t = threading.Thread(target=h2)
        li.append(t)
    for x in li:
        x.start()
    for x in li:
        x.join()


if __name__ == '__main__':
    xx = 0
    do1()
    print(xx)

    print('-' * 40)

    mylock = threading.Lock()
    yy = 0
    do2()
    print(yy)
