import time, threading
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
class Ticket(object):
    global count
    def __init__(self, count):
        self.count = count
        print("初始化票数:", self.count)

    def add(self):
        for i in range(10000):
            print("黑心的老板给我多加了一个任务,现在任务数量:",self.count)
            self.count=self.count+1

    def plue(self):
        for i in range(10000):
            self.count = self.count - 1
            print("机智的我做完了一个任务,现在任务数量:",self.count)

    def show(self):
        print("现在的任务数:",self.count)
if __name__ == '__main__':
    ticket = Ticket(0)
    thread_list = []
    t1 = threading.Thread(target=ticket.add())
    t2 = threading.Thread(target=ticket.plue())
    thread_list.append(t1)
    thread_list.append(t2)
    for t in thread_list:
        t.setDaemon(True)
        t.start()
