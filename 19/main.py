# 多文件下载器

import multiprocessing
import os

def copy(x):
    print('do')
    with open('./one/'+str(x)+'.txt','rb') as data:
        while True:
            rr=data.readline()
            if not rr:
                break
            with open('./two/'+x+'.txt','ab') as dataa:
                dataa.write(rr)

if __name__ == '__main__':

    #创建目录
    try:
        os.mkdir('./two/')
    except:
        pass


    pool=multiprocessing.Pool(8)
    for x in range(1,9):
        pool.apply(func=copy,args=(str(x),))




