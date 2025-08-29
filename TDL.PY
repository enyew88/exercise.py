#1
t = (1, 2, 3, 4)
count = 0
for _ in t:
    count += 1
print(count)
#2
t = (5, 2, 8, 1)
print("Max:", max(t), "Min:", min(t))
#3
lst = [1, 2, 2, 3, 4, 4]
print(list(set(lst)))
#4
lst = [1, 2, 3, 4, 5]
squares = [x*x for x in lst]
print(squares)
#5
a = {"x": 1, "y": 2}
b = {"z": 3}
a.update(b)
print(a)
#6
d = {'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in d.items()})
#7
memo = {0: 0, 1: 1}
def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(10))
#8
n = 20
triplets = [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a*a + b*b == c*c]
print(triplets)
#9
cart = {}

def add_item(name, price, qty):
    cart[name] = {"price": price, "qty": qty}

def remove_item(name):
    cart.pop(name, None)

def total():
    return sum(item["price"] * item["qty"] for item in cart.values())

add_item("apple", 10, 2)
add_item("banana", 5, 3)
print(cart, "Total:", total())
#10
from collections import OrderedDict

class LRUCache:
    def __init__(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

lru = LRUCache(2)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print(lru.cache)

