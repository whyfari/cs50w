#!/usr/bin/python3.7

#####################################################
# str object- sequence of letters, str is immutable
#####################################################
string = "Fari"
print(f"string: {string}, first letter of string is {string[0]}")
# can't change a char in str, we can convert to list and change it
#string[0] = "F"
stringList = list(string)
stringList[0] = "T"
print(
    f"stringList: {stringList}, first (changed)letter of string is {stringList[0]}")

# change list -> string
stringList = "".join(stringList)
print(f"stringList changed to string: {stringList} ")

#####################################################
# list - sequence of mutable values
#####################################################
names = ["Fari", "Jeff", "Saba"]
print("list:", names, "first name in list", names[0])
# change existing item
names[0] = "Tari"
print("list amended:", names, "first name in list", names[0])
names.append("Draco")
print("list after append:", names, "first name in list", names[0])
names.sort()
print("list sorted:", names, "first name in list", names[0])


#####################################################
# tupple - sequence of immutable values
#####################################################
# values in tupples can't change
coord = (1, 2, 3)
print("tupple:", coord)
stringTupple = ("Fari", "is", "my", "name")
print("stringTupple:", stringTupple)
stringTupple = "_".join(stringTupple)
print("stringTupple joined with _:", stringTupple)

#####################################################
# set - collecction of unique values
#####################################################
s = set()
s.add(1)
s.add(11)
s.add(2)
# won't be added
s.add(11)
print("set:", s)
s.remove(2)
print("set after remove:", s)

#####################################################
# dict/map - collecction of key-value values
#####################################################
houses = {"Harry": "Grif", "Draco": "Sly"}
print("dict:", houses["Harry"])
houses["Hermione"] = "Grif"
# can amend value for existing key
houses["Hermione"] = "Sly"
print(houses)


#####################################################
# common funcs
#####################################################
print(f"The set has {len(s)} elements")
print(f"The string has {len(string)} elements")
