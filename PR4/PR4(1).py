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

generator = prime_num_generator()
for _ in range(10):
    print(next(generator))