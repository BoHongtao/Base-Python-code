# -*- coding: UTF-8 -*-
'''
import thread
import time
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print "%s: %s" % (threadName, time.ctime(time.time()))
# 创建2个进程
try:
    thread.start_new_thread(print_time,("Thread_1",10))
    thread.start_new_thread(print_time,("Thread_2",10))
except:
    print "Error:unable to start thread"
while 1:
    pass
print  "Main Finished"
'''