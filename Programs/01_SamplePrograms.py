from random import random
import random

# Hello World
demo = 'Hello World'
print(f'**** {demo} *****')
print('Hello world')

# Add two numbers
demo = 'Add two numbers'
print(f'**** {demo} *****')
num1 = 10
num2 = 20
result = num1 + num2
print('Sum:\t',result)

# Square Root
demo = 'Square Root'
print(f'**** {demo} *****')
input = 18
square_root = input ** 0.5
print('Square root of %0.2f is %0.2f:\t'%(input, square_root))

#  Fibonacci series
print('**** Fibonacci series *****')
fab_series = []
a,b = 0,1
while(a<10):
    fab_series.append(a)
    a,b = b, a+b
print(fab_series)

#  Swap two numbers
print('**** Swap two numbers *****')
x = 10
y = 12
print(f'Before Swap x = {x} \t y = {x}')
temp = x
x = y
y = x
print(f'After Swap x = {x} \t y = {x}')

print('**** Swap two numbers with out third variable*****')
x = 100
y = 120
x,y = y,x
print(f'After Swap x = {x} \t y = {y}')

print('Random Number:  \t', random.randint(0,9))






