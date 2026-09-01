a = 33
b = 200
if b > a:
  print("b is greater than a")
print("*")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("*")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("*")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("*")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print("*")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

print("*")
