def is_leap(year):
  leap = False
  print (year/4)
  print (year/100)
  print (year/400)
 
  # Write your logic here
  if year % 4 == 0 and ( year % 100 != 0  or ( year % 100 == 0 and year % 400 == 0)):
    leap = True
  return leap

year = int(input())
print (is_leap(year))
