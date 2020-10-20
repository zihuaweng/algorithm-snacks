"""
https://njuferret.github.io/2018/07/20/python_multithread_producer_consumer/
"""


# 一个对象一个线程方式
from queue import Queue
from threading import Thread
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG,format='[%(threadName)-9s] %(message)s')

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

class Producer(Thread):
    
    def __init__(self,task_queue, out_queue,name=None):
        super().__init__()        
        if name is not None:
            self.name = name
        self.__task_q = task_queue
        self.__rets_q = out_queue
        # 去掉下面依据注释，可以发现，该函数为主线程执行
        # logging.debug("(Producer.__init__)任务大小：{}".format(task_queue.qsize()))
    
    def run(self):
        while True:
            logging.info('P: 任务队列大小  {}，缓冲队列大小 {}'.format(self.__task_q.qsize(),self.__rets_q.qsize()))
            item = self.__task_q.get()
            result = self.job(item)
            logging.info("P: 值= {} , 结果= {} ".format(item,result))
            self.__rets_q.put(result)            
            logging.info("P: -------------压入缓冲队列 {}--------------".format(item))
            self.__task_q.task_done()
            time.sleep(random.randint(1,5)/40)
    
    def job(self,data):        
        logging.debug("P开始处理数据(in job)： {}".format(data))
        #time.sleep(random.randint(1,5)/40)
        d = data*3        
        logging.debug("P数据处理完成(in job)：{}*3={} ".format(data,d))
        return d
    

class Consumer(Thread):
    def __init__(self,task_queue,name=None):
        super().__init__()        
        if name is not None:
            self.name = name
        self.__tasks_q = task_queue
    
    def run(self):
        while True:
            logging.info('C: 任务队列大小  {} '.format(self.__tasks_q.qsize()))
            item = self.__tasks_q.get()
            logging.info('C:-------------取出任务数据 {}({})--------------'.format(item,item//3))
            result = self.job(item)
            logging.info("C: 值= {} , 结果= {} ".format(item,result))
            self.__tasks_q.task_done()
    
    def job(self,data):
        logging.debug("C开始处理数据(in job)： {}".format(data))
        time.sleep(random.randint(1,5)/40)
        d = fib(data)
        logging.debug("C数据处理完成(in job)： --------------({})fib({})={}----------".format(data//3,data,d))
        return d

def main():
    # N 生产者数量
    # M 消费者数量
    N = 3
    M = 1
    
    # 任务队列
    task_queue = Queue()
    # 处理后任务队列
    ret_queue = Queue()
    
    # 初始化任务队列
    for i in range(1,5):
        task_queue.put(i)

    # 创建N个生产者（每个生产者1个线程）
    producers = []
    for i in range(N):
        p = Producer(task_queue=task_queue, out_queue=ret_queue, name=' 生产者{:02d}'.format(i+1))
        producers.append(p)
        p.start()
    
    # 创建M个消费者（每个消费者1个线程）
    consumers = []
    for i in range(M):
        c = Consumer(task_queue=ret_queue, name=' 消费者{:02d}'.format(i+1))
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