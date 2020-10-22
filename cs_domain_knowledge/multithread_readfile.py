import threading
import queue

#Number of threads
N_THREAD = 5
#Create queue
queue = queue.Queue()

class ThreadClass(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            host = self.queue.get()
            print(self.getName() + ":" + host)
            #signals to queue job is done
            self.queue.task_done()

#Create number process
for i in range(N_THREAD):
    t = ThreadClass(queue)
    # t.setDaemon(True)
    #Start thread
    t.start()

#Read file line by line
hostfile = open("cs_domain_knowledge/test.txt","r")
for line in hostfile:
    #Put line to queue
    queue.put(line.strip())

#wait on the queue until everything has been processed
queue.join()