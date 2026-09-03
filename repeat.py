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

#Flatten a Nested List
#Write a Python function to flatten a nested list.
#Input: [[1, 2], [3, 4], [5]]
#Output: [1, 2, 3, 4, 5]
nested_list = [[1, 2], [3, 4], [5]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)  # Output: [1, 2, 3, 4, 5]

#Merge Two Sorted Lists
#Write a Python function to merge two sorted lists into a single sorted list.
#Input: [1, 3, 5], [2, 4, 6]
#Output: [1, 2, 3, 4, 5, 6]
input1 = [1, 3, 5]
input2 = [2, 4, 6]
merged_list = []
i = 0
j = 0
for i in range(len(input1)):
    merged_list.append(input1[i])
    print (merged_list)
for j in range(len(input2)):
    merged_list.append(input2[j])
    print (merged_list)
merged_list.sort()
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

#Find All Pairs in a List that Sum to a Specific Value
#Write a Python function to find all pairs in a list that sum to a specific value.
#Input: [1, 2, 3, 4, 5], Sum=6
#Output: [(1, 5), (2, 4)]
input_list = [1, 2, 3, 4, 5]
sum_value = 6
pairs = []
for i in range(len(input_list)):
    for j in range(i + 1, len(input_list)):
        if input_list[i] + input_list[j] == sum_value:
            pairs.append((input_list[i], input_list[j]))
print(pairs)  # Output: [(1, 5), (2, 4