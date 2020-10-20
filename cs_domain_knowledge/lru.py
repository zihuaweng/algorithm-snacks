"""
https://my.oschina.net/u/4255396/blog/3471088
"""

import collections
import threading

class LRUCache:
    def __init__(self, capacity=128):
        self.dic = collections.OrderedDict()
        self.remain = capacity
        self.lock = threading.RLock()

    def get(self, key, default=None):
        if key not in self.dic:
            return default
        
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def set(self, key, val):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = val

    def __call__(self, func, n):
        def _(n):
            with self.lock:
                if n in self.dic:
                    return self.get(n)
                else:
                    val = func(n)
                    self.set(n, val)
                    return val
        return _


def f(n):
    if n <= 1:  # 0 or 1
        return n
    return f(n - 1) + f(n - 2)

    
@LRUCache(10)
def f_use_lru(n):
    if n <= 1:  # 0 or 1
        return n
    return f_use_lru(n - 1) + f_use_lru(n - 2)


def test():
    import time
    beg = time.time()
    for i in range(34):
        print(f(i))
    print(time.time() - beg)
    beg = time.time()
    for i in range(34):
        print(f_use_lru(i))
    print(time.time() - beg)


if __name__ == '__main__':
    test()