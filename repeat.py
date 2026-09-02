#Write a Python function to find the maximum and minimum elements in a given list.
#Input: [3, 1, 4, 1, 5, 9]
#Output: (9, 1)
max=0
min=0
list = [3, 1, 4, 1, 5, 9]
for x in list:
    if x >max:
        max = x
    else:
        min = x
print(max, min)


#Remove Duplicates from a List
#Write a Python function to remove duplicates from a list while preserving the order.
#Input: [1, 2, 2, 3, 4, 4, 5]
#Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 2, 3, 4, 4, 5]
d = {}

# 1. Build dictionary frequency count
for x in numbers:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)  # Output: {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
# 2. Compare dictionary values and build new_list
new_list = []
for key in d:
    if d[key] == 1:  # Compare value
        new_list.append(key)

print(new_list)  # Output: [1, 3, 5]

#Find the Intersection of Two Lists
#Write a Python function to find the intersection of two lists.
#Input: [1, 2, 3, 4], [3, 4, 5, 6]
#Output: [3, 4]
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
new_list = []
for x in list1:
    if x in list2:
        new_list.append(x)
print(new_list)  # Output: [3, 4]