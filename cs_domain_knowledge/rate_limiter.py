"""
https://gist.github.com/gregburek/1441055
"""
import time
import threading
from functools import wraps

def rate_limited(max_per_second: int):
    """Rate-limits the decorated function locally, for one process."""
    lock = threading.RLock()
    min_interval = 1.0 / max_per_second

    def decorate(func):
        last_time_called = time.perf_counter()

        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            lock.acquire()
            nonlocal last_time_called
            try:
                elapsed = time.perf_counter() - last_time_called
                left_to_wait = min_interval - elapsed
                if left_to_wait > 0:
                    time.sleep(left_to_wait)

                return func(*args, **kwargs)
            finally:
                last_time_called = time.perf_counter()
                lock.release()

        return rate_limited_function

    return decorate


@rate_limited(1)  # 2 per second at most
def PrintNumber():
    print("1234")

if __name__ == "__main__":
    print("This should print 1,2,3... at about 2 per second.")
    for i in range(1,10):
        threading.Thread(target=PrintNumber, args=()).start()
        # PrintNumber()