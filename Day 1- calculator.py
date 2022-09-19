import re
import math

a = input("enter the number: ")
b = input("enter the number: ")
c = input("operation symbol: ")

x= re.findall("[a-zA-Z]",a)
y= re.findall("[a-zA-Z]",b)
if(x and y):
    print("enter a valid number")

    #return total
else:
    print("success")
    if c == "+":
        total = int(a) + int (b)
        print(total)
    elif c == "-":
        total = int(a) - int (b)
        print(total)
    elif c == "/":
        total = int(a) / int (b)
        print(total)
    elif c == "*":
        total = int(a) * int (b)
        print(total)
    pass