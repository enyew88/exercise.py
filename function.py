#1
def square(n):
    return n * n

print(square(5))
#2
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
#3
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done")

slow_function()
#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

gen = prime_generator()
for _ in range(10):
    print(next(gen))
