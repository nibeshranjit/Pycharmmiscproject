a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print('*')
b = "Hello, World!"
print(b[2:13])

print('*')
b = "Hello, World!"
print(b[:5])

print('*')
b = "Hello, World!"
print(b[2:])

print('*')
b = "Hello, World!"
print(b[-5:-2])

print('*')
a = "Hello, World!"
print(a.upper())

print('*')
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print('*')
a = "Hello, World!"
print(a.replace("H", "J"))

print('*')
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print('*')
a = "Hello"
b = "World"
c = a + b
print(c)
print('*')
age = 36
#txt = "My name is John, I am " + age
#print(txt)
print('*')
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print('*')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print('*')
print(10 > 9)
print(10 == 9)
print(10 < 9)

print('*')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print('*')
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('*')
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

print('*')
x = 1    # int
y = 2.8  # float

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

print(a)
print(b)

print(type(a))
print(type(b))


print('*')
import random
print(random.randrange(1, 10))

print('*')
print('*')
print('*')
print('*')

