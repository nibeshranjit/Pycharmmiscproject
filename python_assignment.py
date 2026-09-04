#Python Assessment
#Section A - Strings
#Q1
#Write a program to reverse a string without using slicing.
#Example: Input: “python” Output: “nohtyp”

from itertools import count


text = "python"
reversed_text = ""
index = len(text) - 1

while index >= 0:
    reversed_text =reversed_text + text[index]
    index = index - 1

print(reversed_text)

print()

#Q2
#Find the first non-repeating character in a string.
#Example: Input: “programming” Output: “p”

input="programming"
for char in input:
    if input.count(char) == 1:
        print(char)
        break   
print ()

#Q3
#Check if a string is a palindrome.
#Example: Input: “madam” Output: True
text = "madam"
reversed_text = ""
index = len(text) - 1

# Step 1: Reverse the string completely using the while loop
while index >= 0:
    reversed_text = reversed_text + text[index]
    index = index - 1

# Step 2: Compare after the loop finishes
if text == reversed_text:
    print(True)
else:
    print(False)

print()

#Q4
#Count the frequency of each character in a string.
#Example: Input: “hello” Output: h:1 e:1 l:2 o:1
input = "hello"
frequency = {}
for char in input:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

print()

#Q5
#Remove duplicate characters from a string while preserving order.
#Example: Input: “programming” Output: “progamin”
text = "programming"
result = ""

for char in text:
    if char not in result:
        result += char

print(result)  
print()

#Section B - Lists
#Q6
#Remove duplicates from a list without using set().
#Example: Input: [1,2,2,3,4,4] Output: [1,2,3,4]
list=[1, 2, 2, 3, 4, 4]
result = []
for item in list:
    if item not in result:
        result.append(item)
print(result)
print()
#Q7
#Find the second largest number in a list.
#Example: Input: [10,20,5,30,25] Output: 25
numbers = [10, 20, 5, 30, 25]

# Step 1: Sort the list in ascending order
numbers.sort()

# Step 2: Declare the second-to-last number as the second largest
second_largest = numbers[-2]

print(second_largest)
print()
#Q8
#Find all duplicate elements in a list.
#Example: Input: [1,2,3,2,4,5,1] Output: [1,2]
input_list = [1, 2, 3, 2, 4, 5, 1]
counter = {}
for num in input_list:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1
print(counter) #checking the counter dictionary to see the frequency of each number

duplicates = []
for num in counter:
    if counter[num] > 1:
        duplicates.append(num)

print(duplicates) 
#Q9
#Rotate a list by K positions.
#Example: Input: [1,2,3,4,5], K=2 Output: [4,5,1,2,3]
nums = [1, 2, 3, 4, 5]
k = 2
n = len(nums)

# Step 1: Use a dictionary to map each element to its new rotated index (harder )
index_map = {}

for i in range(n):
    new_index = (i + k) % n
    index_map[new_index] = nums[i]

# Step 2: Reconstruct the new list from the dictionary in index order
rotated_list = []
for i in range(n):
    rotated_list.append(index_map[i])

print(rotated_list)  # Output: [4, 5, 1, 2, 3]

#Q10
#Find the intersection of two lists.
#Example: Input: [1,2,3,4] [3,4,5,6]
#Output: [3,4]
input_list1 = [1, 2, 3, 4]
input_list2 = [3, 4, 5, 6]
intersection = []
for num in input_list1:
    if num in input_list2:
        intersection.append(num)    
print (intersection)  # Output: [3, 4]

print()

#Section C - Dictionary
#Q11
#Count frequency of elements in a list using a dictionary.
#Example: Input: [1,2,2,3,3,3] Output: {1:1, 2:2, 3:3}
input_list = [1, 2, 2, 3, 3, 3]
frequency={}
for x in input_list:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
print(frequency)  # Output: {1: 1, 2: 2

print()

#Q12
#Find the key having the maximum value.
#Example: {“A”:100,“B”:5440,“C”:300}
#Output: B
data = {"A": 100, "B": 500, "C": 300}

max_key = None
max_value = None

for key in data:
    value = data[key]
    if max_value is None or value > max_value:
        max_value = value
        max_key = key

print(max_key)  # Output: B

#Q13
#Reverse a dictionary.
#Example: {“a”:1,“b”:2}
#Output: {1:“a”,2:“b”}

original = {"a": 1, "b": 2}
reversed_d = {}

for key in original:
    value = original[key]  # Get the value corresponding to the current key
    reversed_d[value] = key  # Assign the old key as the new value

print(reversed_d)  # Output: {1: 'a', 2: 'b'}

#Q14
#Merge two dictionaries.
#Example: d1={“a”:1} d2={“b”:2}
#Output: {“a”:1,“b”:2}
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}
print(merged)  # Output: {'a': 1, 'b': 2}

#Q15
#Count word frequency in a sentence using dictionary.
#Example: Input: “python is good python is easy”
#Output: { “python”:2, “is”:2, “good”:1, “easy”:1 }

sentence = "python is good python is easy"
words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)  

#Section D - Loops
#Q16
#Print the following pattern:
#●	   **
n = 5

for i in range(1, n + 1):
    row = ""
    
    for j in range(i):
        row = row + "*"
    print(row)

#Q17
#Print multiplication table of a given number.
#Example: Input: 5
#Output: 5 x 1 = 5 … 5 x 10 = 50
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")       

print()
#Q18
#Find factorial using for loop.
#Input: 5 Output: 120
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)

#Q19
#Find all prime numbers between 1 and 100.
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(primes)

print ()

#Q20
#Generate Fibonacci series up to N terms.
#Example: Input: 8
#Output: 0 1 1 2 3 5 8 13
n = 8
fib_sequence = []

# Step 1: Initialize the first two numbers of the Fibonacci sequence
a = 0
b = 1

# Step 2: Loop N times to generate each term
for i in range(n):
    fib_sequence.append(a)  # Store current term
    next_term = a + b  # Calculate the next term
    a = b  # Shift 'a' forward
    b = next_term  # Shift 'b' forward

print(fib_sequence)
print('*')
#Section E - Interview Coding Questions
#Q21
#Find the first non-repeating number in a list.
#Input: [1,2,3,4,5,1,2,3]
#Output: 4
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
counts = {}

# Step 1: Count frequency of each number using a dictionary
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

# Step 2: Find the first number in the original list with a count of 1
first_non_repeating = 0
for num in numbers:
    if counts[num] == 1:
        first_non_repeating = num
        break

print(first_non_repeating)

print()

#Q22
#Find the Nth non-repeating number in a list.
#Input: [1,2,3,4,5,1,2,3] N = 2
#Output: 5
#Note - First non repeating is 4
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
N = 2
counts = {}

# Step 1: Count frequency of each number using a dictionary
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

# Step 2: Find the Nth number in the original list with a count of 1
nth_non_repeating = 0
count = 0
for num in numbers:
    if counts[num] == 1:
        count += 1
        if count == N:
            nth_non_repeating = num
            break

print(nth_non_repeating)

print()

#Q23
#Check whether two strings are anagrams.
#Input: “listen” “silent”
#Output: True
str1 = "listen"
str2 = "silent"

# Convert strings to lowercase and sort their characters
sorted_str1 = sorted(str1.lower())
sorted_str2 = sorted(str2.lower())

# Check if the sorted characters are equal
if sorted_str1 == sorted_str2:
    print(True)
else:
    print(False)
print()

#Q24
#Find missing number from array.
#Input: [1,2,3,5]
#Output: 4
numbers = [1, 2, 3, 5]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum
print(missing_number)

#Q25
#Find top occurring element in a list.
#Input: [1,2,2,3,3,3,4]
#Output: 3
numbers = [1, 2, 2, 3, 3, 3, 4]
counts = {}
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1
top_element = max(counts, key=counts.get)
print(top_element)
