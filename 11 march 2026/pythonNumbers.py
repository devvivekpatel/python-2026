# There are three types of number in python
# int , float , complex

# first talk about integer
import random

x =4
y=453344343355353
z = -444444445353

print(z)
print(y)
print(x)

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# remember

a=444.444
b=5e2

print(b)
# answer is 500 cause e indicates 10 sand after that number power that means
# 5e2 = 5X10X10


num1 = 56
num2 = 43.23
num3 = 1j

g= float(num1)
# you can't convert a complex number to any type
# h = int(num3)
i = complex(num2)

print(type(g))
# print(type(h))
print(type(i))
print(i)

randomNum = random.randrange(1,10)
print(randomNum)
