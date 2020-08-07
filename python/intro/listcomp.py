#!/usr/bin/python3.7

# no filtering expression
# new_list = [expression for member in iterable (if conditional)]

# filtering expression
# new_list = [expression (if conditional) for member in iterable]

# filtering expression
# new_list = [expression (if conditional) for member in iterable]

s = []
for i in range(10):
    s.append(i * i)
print("squares using array append", s)


squares = [i * i for i in range(10)]
print("squares using list comp", squares)

# filtering (if condition at end) before adding to list
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print("filter vowels in sentense using list comp", vowels)

# filtering (if condition at end) and amending(if condition(or is this just the expression?) in beginning) before adding to list
vowels = [i if i == 'a' else 'b' for i in sentence if i in 'aeiou']
print("filter vowels and make 'a' = 'b' in sentense using list comp", vowels)


# amending instead of filtering
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]

print("input three numbers")
x = int(input())
y = int(input())
z = int(input())
n = int(input())
