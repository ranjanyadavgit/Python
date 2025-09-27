import sys

def add(num1, num2):
  add = num1 + num2
  return add

def sub(num1, num2):
  sub = num1 - num2
  return sub

def mul(num1, num2):
  mul = num1 * num2
  return mul

num1 = int(sys.argv[1])
operation = (sys.argv[2]) 
num2 = int(sys.argv[3])

if operation == "add":
  output=add(num1, num2)
  print(output)

Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/Day-4
$ python calculator.py 2 add 3
5
--------------------------------------------------------


import sys
def addition(num1, num2):
    add = num1 + num2
    return add

def sub(num1,num2):
    subs = num1 - num2
    return subs

def mul(num1,num2):
    multi = num1 * num2
    return multi


num1 = int(sys.argv[1])
operation = (sys.argv[2])
num2 = int(sys.argv[3])

if operation == "mul":
    output = mul(num1,num2)
    print(output)

Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/Day-4
$ python calculator.py 2 mul 3
6

