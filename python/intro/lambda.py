#!/usr/bin/python3.7

people = [
        {"name": "Harry", "house": "Grif"},
        {"name": "Ron", "house": "Grif"},
        {"name": "Draco", "house": "Sly"},
        {"name": "Fari", "house": "Huff"}
]

def f(person):
    return person["name"]

# using explicitly defined function which sorts by "name"
people.sort(key=f)

print("sort using explict function and on name", people)

# using a lambda function which sorts by "house"
people.sort(key= lambda person: person["house"])

print("sort using lambda function and on house", people)

student_tuples = [
('john', 'A', 15),
('davb', 'B', 10),
('dave', 'B', 10),
('bane', 'B', 12),
('davb', 'B', 10),
('davc', 'B', 10),
('davb', 'B', 12),
]

# sort by age then name
student_tuples.sort(key=lambda student: (student[2], student[0]))
print ("student", student_tuples)
