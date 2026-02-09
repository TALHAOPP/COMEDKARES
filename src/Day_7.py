# creta a file

file = open("talha.txt","w")
file.write("Talha is currently in comedkares , doing this internship")
file.close()
 

#read file

file = open("talha.txt","r")
content = file.read()
print(content)
file.close()

#append

file = open("talha.txt","a")
file.write("Good Boy")
file.close()

# using with
with open("talha.txt","r") as file:
    content = file.read()
    print(content)
    
#import csv 

import csv 

with open("choco.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
# error handling using try

try :
    
    with open("missing.txt","r") as file:
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("such file not exists")
    
    
# TASK 1

name = input("Enter your name: ")
daily_goal = input("Enter your Daily Goal: ")

with open("task1.txt", "a") as file:
    file.write(f"{name}: {daily_goal}")
    
    
#TASK 2

with open("students.csv","a") as file:
    file.write("Name,Grade,Status\n")
    file.write("Alice,A,Pass\n")
    file.write("Bob,B,Pass\n")
    file.write("Charlie,F,Fail\n")
    
with open("students.csv","r") as file:
    content = file.read()
    print(content)
    
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])

#TASK 3

filename = (input("Enter a filename : "))

try:
    with open(filename,"r") as file:
        contents = file.read()
        print("File contents: ")
        print(contents)
    
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
