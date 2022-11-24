import datetime
import time
def time_decorator(func):
    def wrapper(*args,**kwargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(int((datetime.datetime.now() - startTime).total_seconds()))
        return result
    return wrapper
@time_decorator
def sleep_1_sec():
    time.sleep(5)
    print("function")
    return 25

result = sleep_1_sec()
print(result)