#!/usr/bin/python3.7

for i in [2,3] :
    print(i)

# range - range(n) = 0 - (n-1)
for i in range(3) range(4) :
    print(i)

names = ["Harry", "Ron", "Hermoine"]
for name in names:
    print(name, end = " : ")
    for char in name:
        print(char, end = " ")
    print()

############################
#### while loops
# else considition is a bit weird it gets executed at the end (when the while condition)
# fails, but it's not triggered it something in the while loop 'break's
print("While loop, if number >= 4 print till 4 and exit, else print till 1 as well as 'blah'")
n = int(input ("number: "))
while n > 0 :
    print(n)
    if n == 4:
        break
    n-= 1     
else:
    print("blah")

        
