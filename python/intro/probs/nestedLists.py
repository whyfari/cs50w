# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    scores.append((name, score))

scores.sort(key=lambda item: (item[1], item[0]))
secondLowest = ""

lowest = scores[0][1]
l = len(scores)


for i in range(l):
    n, s = scores[i]
    if (s == lowest):
        continue
    else:
        if secondLowest != "" and secondLowest != s:
            break
        else:
            secondLowest = s
            print(n)
