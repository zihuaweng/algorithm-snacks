import threading 
import queue

class Buffer:

    def __init__(self,size):
        self.size = size
        self.buffer = queue.Queue()
        self.lock = threading.Lock()
        self.has_data = threading.Condition(self.lock) # small sock depand on big sock
        self.has_pos = threading.Condition(self.lock)
    def get_size(self):
        return self.size
    def get(self):
        with self.has_data:
            while self.buffer.empty():
                print("I can't go out has_data")
                self.has_data.wait()
                print("I can go out has_data")
            result = self.buffer.get()
            self.has_pos.notify_all()
        return result
    def put(self, data):
        with self.has_pos:
            #print(self.count)
            while self.buffer.qsize() >= self.size:
                print("I can't go out has_pos")
                self.has_pos.wait()
                print("I can go out has_pos")
            # If the length of data bigger than buffer's will wait
            self.buffer.put(data)
            # some thread is wait data ,so data need release
            self.has_data.notify_all()
    
if __name__ == "__main__":
	buffer = Buffer(3)
	def get():
	    for _ in range(10000):
	        print(buffer.get())
	        
	def put():
	    a = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
	    for _ in range(10000):
	        buffer.put(a)
    th1 = threading.Thread(target=put)
    th2 = threading.Thread(target=get)
    th1.start()
    th2.start()
    th1.join()
    th2.join()