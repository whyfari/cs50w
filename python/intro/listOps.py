#!/usr/bin/python3.7
out = []

# N = int(input())
# for i in range(N):
#     mes = list(input().split())
#     if (mes[0] == "insert"):
#         out.insert(int(mes[1]), int(mes[2]))

a = []
a.append(30)     # append single item to the end
a.extend(a[0:])  # a[len(a):] = iterable ; append a list to the end
# insert 20 at the 3rd index(if index is greater than length then it just adds at the end)
a.insert(3, 25)
a.remove(25)     # ERROR ValueError raised ; remove the first given from the list
a.pop(0)  # can raise ERROR if index provided is OOR;  removes index(optional; last by default) item and returns it;
a.index(30, 0, 4)  # ERROR ValueError can be thrown; return index of first item that matches 25, 0 and 4 are optional, to limit search to subsequence
31 in a  # returns True/False altenate to index; like if you don't want error thrown for values not found;
"bohiya".find("hi")
# only for strings; str.find(sub[, start[, end]] ); only for strings (not all iterables), returns -1 when not round a.count(25)

a.sort(key=None, reverse=False)  # optional params
a.reverse()
a.copy()  # a[:] # returns shallow copy
a.clear()  # del a[:] ; removes everything
