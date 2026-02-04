cars = ["Creta","Maruti","Ertiga","Forturner"]
print(cars)
#APPEND
cars.append("Ferrari")
print(cars)
cars.append(20)
print(cars)
#POP
cars.pop(1)
print(cars)
cars.pop(4)
#SORT
cars.sort()
print(cars)
#SLICING
cars[1:3] , cars[0:2]
print(cars)
#INDEXING
cars.index("Creta")
cars.index("Forturner")


# TASK 1

fruits = ["Apples", "Bananas", "Carrots", "Dates"]
print(fruits)
fruits.append("Eggs")
fruits.pop(1)
fruits.sort()

print(fruits)

# TASK 2

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temperatures[0])
print(temperatures[-1])

Afternoonpeak = temperatures[3:6]
Last_3_Hours = temperatures[-3:]

print(temperatures)
print(Afternoonpeak)
print(Last_3_Hours)


# TASK 3

screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")
screen_res[0] = 1280
print("Tuples cannot be modified!")

