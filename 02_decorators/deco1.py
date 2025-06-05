# problem 1 : Timing Function Execution 
# write a decorator that measure the time a function to execute 

import time 

def timer(func):
    def wrapper(*args, **kwargs):
       start_time = time.time()
       result =  func(*args, **kwargs)
       end_time = time.time()
       print(f"{func.__name__} run in {end_time-start_time} time")
       return result
    return wrapper 

@timer
def example_func(n):
    time.sleep(n)

example_func(2)

