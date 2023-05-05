import math

n = int(input("Enter num1: ")) 
op = input("Enter op(sqrt, sin, cos, tan, factorial): ")

if op == "sqrt":
    result = math.sqrt(n)
    print('The Radical value of', n, 'is: ', result) 
if op == "sin":
    result = math.sin(n)
if op == "cos":
    result = math.tan(n)
if op == "tan":
    result = math.cos(n)
if op == "factorial":
    result = math.factorial(n)
print('The', op, 'value of', n, 'is: ', result) 
