def talha():
    print("He is In Comedkares")

def umar():
    print("HE is at home sleeping")
    
    
talha()
umar()

def numbers(q,z):
    print(q*z)

multiplication = numbers(3,2)

print(multiplication)


x = 10 

def count():
    x = 7
    print(x)
    
count()
print(x)


x = 9

def multiply():
    global x
    x *= 2
    
multiply()
print(x)

# -------------------

import math
print(math.sqrt(8))
print(math.remainder(2, 3))
import random 
name = ("talha","umar","amaan","mujahid","sagar")
winner = random.choice(name)
print (winner)

# TASK 1
def calc_rectangle(length, width):
    area = length*width
    perimeter = 2*(length+width)
    return area,perimeter

calc_rectangle(3, 4)

length = int(input("Enter the length :"))
width = int(input("Enter the breadth :"))

area,perimeter = calc_rectangle(length, width)

print(f"The area of rectangle is {perimeter}")
print(f"The area of rectangle is {area}")










