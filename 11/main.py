#守护进程

import time
import multiprocessing

def do():
    for _ in range(5):
        time.sleep(0.2)
        print('do')
    print('do done')
if __name__ == '__main__':
    p1=multiprocessing.Process(target=do)
    p1.start()
    print('main')
    
    time.sleep(1.2)
    print('_________')

    p2 = multiprocessing.Process(target=do)
    p2.daemon=True
    p2.start()
    print('main')
