#!/usr/bin/python3.7
line = "This is/was a space seperateds string"
print(line)
print("Convert string to a list using split() and then joining with \"\"")
print("-".join(line.split(" ")))

# join/map/sort stuff


def athleteSort:
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda ath: (ath[k]))
    for i in range(n):
      # arr = [[1 ,2, 3], [11,22,19], [1,2,4]]
        print(" ".join(map(str, (arr[i])))

# SUBSTRINGS
def count_substring(string, sub_string):
    count=0
    l1=len(string)
    l2=len(sub_string)
    for c in range(l1):
        if string[c:c+l2] == sub_string:
            count=count + 1

        if c+l2 == l1:
            break
    return count


string="ABCDCDC"
print("string is", string)
print("ABC is in", string, count_substring("ABCDCDC", "CDC"), "times")
print(": =", string[:], ",1:2 =", string[1:2],
      ",:3 =", string[:3], ",2: =", string[2:])

# functions isalnum, isdigit, isupper


def anyupper(str):
    return(any(c.isupper() for c in str))


print("any upper in 'abcd'", anyupper("abcd"))
print("any upper in 'abCd'", anyupper("abCd"))
