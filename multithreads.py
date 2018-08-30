#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:14:38 2018

@author: wsw
"""

# test multithreads
import os
import time
import threading
import glob
import skimage.io as imageio

classes = os.listdir('./trainval_Animals/train')

# read one class images
def read_one_class(class_name,work_id):
    start = time.time()
    imgdir = os.path.join('./trainval_Animals/train',class_name)
    # get all image path
    imgpaths = glob.glob(imgdir+'/*.jpg')
    print(imgdir)
    print('Starting Thread Id:',work_id)
    for imgpath in imgpaths:
        img = imageio.imread(imgpath)
#        print(img.shape)
    end = time.time()
    print('Stop Thread Id:',work_id,'Time:%.3f(Sec)'%(end-start))
    
# read 5 class images
def read_five_class():
    start = time.time()
    for i in range(32):
        imgdir = os.path.join('./trainval_Animals/train',classes[i])
        # get all image path
        imgpaths = glob.glob(imgdir+'/*.jpg')
        print(imgdir)
        for imgpath in imgpaths:
            img = imageio.imread(imgpath)
    #        print(img.shape)
    end = time.time()
    print('Total Time:%.3f(Sec)'%(end-start))

  
# read 4 class images for every thread
def read_four_class(class_name,work_id):
    start = time.time()
    print('Starting Thread Id:',work_id)
    for cls in class_name:
        imgdir = os.path.join('./trainval_Animals/train',cls)
        # get all image path
        imgpaths = glob.glob(imgdir+'/*.jpg')
        print(imgdir)
        for imgpath in imgpaths:
            img = imageio.imread(imgpath)
    #        print(img.shape)
    end = time.time()
    print('Stop Thread Id:',work_id)
    print('Thread %d Run Total Time:%.3f(Sec)'%(work_id,end-start))
    
def main():
    threads = [threading.Thread(target=read_one_class,args=(classes[idx],idx)) for idx in range(5)]
    start = time.time()
    
    for thread in threads:
        thread.setDaemon(False)
        thread.start()
    
    # sub-thread needs to join()
    # main-thread can wait all of sub-thread
    # finished then to excute
    # join是让所有子线程执行完毕后让主线程在运行
    for thread in threads:
        thread.join()
    
    # main-thread
    end = time.time()
    print('Total Time:%.3f(Sec)'%(end-start))

def test_8_threads():
    threads = [threading.Thread(target=read_four_class,args=(classes[4*idx:4*idx+4],idx)) for idx in range(8)]   
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print('Run 8 Threads Total Time:%.3f(Sec)'%(end-start))
    

def test_32_threads():
    threads = [threading.Thread(target=read_one_class,args=(classes[idx],idx)) for idx in range(32)]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print('Run 32 Threads Total Time:%.3f(Sec)'%(end-start))

   
if __name__ == '__main__':
    main()
    test_8_threads()
    read_five_class()
    # test_32_threads()



'''
结论：
单线程：运行时间254.699(Sec)
4线程：运行时间238.975(Sec)
8线程：运行时间199.361(Sec)
16线程：运行时间209.219(Sec)
32线程：运行时间228.888(Sec)
线程数并不是越多越好，也不是越少越好
最好是和CPU核数一致
'''
    

    
