# import multiprocessing
# def process(num):
#     print "Process",num
# if __name__ == '__main__':
#     for i in range(10):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()

from multiprocessing import Pool
import time
import os
def task(name):
    # 开始执行，我的机器是4核，所以是4个进程一起运行
    print("Run task %s (%s)...")
    print(name, os.getpid())
    print(time.time())
    time.sleep(3)

if __name__ == '__main__':
    print("Parent process %s")
    print(os.getpid())
    p = Pool()
    for i in range(9):
        # pply_async方法中新建的任务只是被添加到任务队列中，还并未执行
        p.apply_async(task, args=(i,))
    print("Waiting ford all subprocess done ...")
    p.close()
    p.join()
    print("All subprocess done")