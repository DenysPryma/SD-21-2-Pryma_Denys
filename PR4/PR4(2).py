import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Час виконання:", end_time - start_time, "сек")
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    generator = prime_num_generator()
    for _ in range(n):
        print(next(generator))
def prime_num_generator():
    num = 2
    while True:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num
        num += 1

n = 5
prime_num_getter(n)
