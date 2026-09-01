thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print('*')
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print('*')
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print('*')
#list constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print('*')
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print('*')
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print('*')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print('*')
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print('*')
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print('*')
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print('*')
#adds new item at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print ('*')
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print ('*')
#remove specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print ('*')
#IF THERE IS ONE THAN MORE ITEM WITH SAME NAME THEN REMOVE WILL REMOVE ONLY THE FIRST ITEM
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print ('*')
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print ('*')
#if we dont mention any index no in pop then it will remove the last item
thislist=["asd","asdf","sdf","sdsf","saas","sas"]
thislist.pop()
print(thislist)
print ('*')
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print('*')
thislist = ["apple", "banana", "cherry"]
del thislist


print ('*')

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print('*')
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print('*')
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print('*')
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print('*')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print('*')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print('*')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print('*')
print('*')
