students_details = {"name":"Talha","age": 23,"location":"gulbarga"}
print(students_details)
print(students_details["name"])

# Get
students_details.get("name")
students_details.get("age")

# TASK 1 

contacts = {"Talha": 7204730753, "Umar" : 7829114780, "Mushu" : 9886263627}
contacts["Mujahid" ]= 7381033174
contacts["Mushu"] = 9648264139
print (contacts)
contacts.get("Talha")
contacts.get("sahil")
print("Contact not found")

for contacts,phone in contacts.items():
    print(contacts,phone)


# TASK 2

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users=set(raw_logs)
print(unique_users)
print(raw_logs)
print("ID05" in  raw_logs)
print(len(raw_logs))
print(len(unique_users))
print("3 Dublicates was Removed")


#TASK 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print (friend_a & friend_b)
print (friend_a | friend_b)
print (friend_a - friend_b)
print (friend_b - friend_a)