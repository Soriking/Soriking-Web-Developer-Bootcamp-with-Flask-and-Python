friend_age={'ROlf': 24, 'Adam': 30 ,'Anne': 27}

print(friend_age['Adam'])

# --------------------
friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends[1]["name"])

# --------------------
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

#or
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


# --------------------
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")
else:
    print("Bob isn't a student in this class!")
