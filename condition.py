#1
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#2
a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
#3
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")
#4
a, b, c = 5, 5, 5
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

