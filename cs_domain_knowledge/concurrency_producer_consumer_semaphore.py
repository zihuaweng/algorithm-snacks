"""
https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem

A semaphore manages an internal counter
acquire()  count -= 1
release()  count += 1
The counter can never go below zero

when acquire() finds that it is zero, it blocks, waiting until some other thread 
calls release().

works fine when there is only one producer and consumer.
"""

from threading import Thread, Semaphore

# Buffer size
N = 10
# Buffer init
buf = [0] * N

fill_count = Semaphore(0)
empty_count = Semaphore(N)

def produce():
    print("One time produced!")
    return 1

def producer():
    front = 0
    while True:
        x = produce()
        empty_count.acquire()
        buf[front] = x
        fill_count.release()
        front = (front+1) % N

def consume(y):
    print("{} item consumed!".format(y))

def consumer():
    rear = 0
    while True:
        fill_count.acquire()
        y = buf[rear]
        empty_count.release()
        consume(y)
        rear = (rear+1) % N

producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()


