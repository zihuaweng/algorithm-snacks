# Singleton/SingletonPattern.py

# https://www.cnblogs.com/huchong/p/8244279.html

# using decorater
def singleton(cls):
    __instances = {}
    def __getinstance(*args, **kargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kargs)
        return __instances[cls]
    return __getinstance

@singleton
class MyClass:
    def __init__(self, a):
        print('aaaa')
        print(a)


a = MyClass('ccc')
print(a)
print('-----')
a = MyClass('cccc')
print(a)
print('-----')


# using class

import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

def task(arg):
    obj = Singleton()
    print(obj, '____')
    obj = Singleton()
    print(obj, '---')

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()