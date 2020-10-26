"""
https://njuferret.github.io/2018/07/20/python_multithread_producer_consumer/
"""


# 一个对象一个线程方式
import queue
import threading
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG,format='[%(threadName)-9s] %(message)s')

# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1)+fib(n-2)


def fib(n):
    return n


class Producer(threading.Thread):
    
    def __init__(self,task_queue, out_queue, condition):
        super().__init__()       
        self.__task_q = task_queue
        self.__rets_q = out_queue
        self.condition = condition
        # 去掉下面依据注释，可以发现，该函数为主线程执行
        # logging.debug("(Producer.__init__)任务大小：{}".format(task_queue.qsize()))
    
    def run(self):
        while True:
            with self.condition:
                if self.__rets_q.empty():
                    item = self.__task_q.get()
                    result = self.job(item)
                    self.__rets_q.put(result)            
                    self.__task_q.task_done()
                    self.condition.notify_all()
                    self.condition.wait()
    
    def job(self,data):        
        d = data*3        
        return d
    

class Consumer(threading.Thread):
    def __init__(self,task_queue, condition):
        super().__init__()  
        self.__tasks_q = task_queue
        self.condition = condition
    
    def run(self):
        while True:
            with self.condition:
                if self.__tasks_q.empty():
                    self.condition.notify_all()
                    self.condition.wait()
                    # print('aaa')
                item = self.__tasks_q.get()
                result = self.job(item)
                self.__tasks_q.task_done()
    
    def job(self,data):
        d = fib(data)
        return d

def main():
    # N 生产者数量
    # M 消费者数量
    N = 3
    M = 1
    
    # 任务队列
    task_queue = queue.Queue()
    # 处理后任务队列
    ret_queue = queue.Queue()
    # condition
    condition = threading.Condition()
    
    # 初始化任务队列
    for i in range(1000):
        task_queue.put(i)

    # 创建N个生产者（每个生产者1个线程）
    producers = []
    for i in range(N):
        p = Producer(task_queue, ret_queue, condition)
        producers.append(p)
        p.start()
    
    # 创建M个消费者（每个消费者1个线程）
    consumers = []
    for i in range(M):
        c = Consumer(ret_queue, condition)
        consumers.append(c)
        c.start()
        
    # 阻塞线程，等待任务完成
    task_queue.join()
    ret_queue.join()
    
    # 当任务完成后，主线程退出，子线程也随之退出
    
    
if __name__ == "__main__":
    logging.debug("开始运行.......")
    main()
    logging.debug('运行完成.....')