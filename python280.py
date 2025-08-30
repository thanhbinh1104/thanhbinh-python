# 1. Write a Python program to sum all the items in a list.
def ex_01():
    list = [1, 2, 3, 4, 5]
    sum = 0
    for item in list:
        sum += item
    print(f"Sum of item in list: {sum}")
# 2. Write a Python program to multiply all the items in a list.
def ex_02():
    product = 1
    for item in list:
        product *= item
    print(f"Product of item in list: {product}")
# 3. Write a Python program to get the largest number from a list.
def ex_03():
    biggest = list[0]
    for item in list:
        if item > biggest:
            biggest = item
    print(f"Biggest item in list: {biggest}")
# 4. Write a Python program to get the smallest number from a list.
def ex_04():
    smallest = list[0]
    for item in list:
        if item < smallest:
            smallest = item
    print(f"Smallest item in list: {smallest}")
# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def ex_05():
    list = ['abc', 'xyz', 'aba', '1221']
    count = 0
    for word in list:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    print(f"Number of strings meeting the criteria: {count}")
# 6. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def ex_06():
    list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sorted(list, key=lambda x: x[-1])
    print(f"Expected Result: {sorted_list}")
# 7. Write a Python program to remove duplicates from a list.
def ex_07():
    list = ["banana", "orange", "banana", "cherry"]
    list.remove("banana")
    print(list)
# 8. Write a Python program to check if a list is empty or not.
def ex_08():
    list = []
    if not list:
        print("The list is empty")
    else:
        print("The list is NOT empty")
# 9. Write a Python program to clone or copy a list.
numbers = [1, 2, 3, 4, 5]
print("Danh sách ban đầu:", numbers)
copy_numbers = []
for num in numbers:
    copy_numbers.append(num)
print("Danh sách sao chép:", copy_numbers)
# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.
words = ["Python", "is", "fun", "programming", "code"]
n = 3
long_words = []
for word in words:
    if len(word) > n:
        long_words.append(word)
print("Các từ dài hơn", n, "là:", long_words)
# 11. Write a Python function that takes two lists and returns True if they have at
# least one common member.
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            print("True")
    else:
        print("False")
list1 = [1, 2, 3, 4, 5]
list2 = ['Python', 'code', 3]
result = have_common_member(list1, list2)
print(result)
# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = []
for i in range(len(color)):
    if i not in (0, 4, 5):
        result.append(color[i])
print(result)
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is
# *.
array_3d = []
for i in range(3):
    layer = []
    for j in range(4):
        row = []
        for k in range(6):
            row.append('*')
        layer.append(row)
    array_3d.append(layer)
print(array_3d)
# 14. Write a Python program to print the numbers of a specified list after removing
# even numbers from it.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)
print("Danh sách sau khi loại bỏ số chẵn:", result)
# 15. Write a Python program to shuffle and print a specified list.
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Danh sách sau khi trộn:", numbers)
# 16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both
# included).
squares = []
for i in range(1, 31):
    squares.append(i ** 2)
first_five = squares[:5]
print("5 số bình phương đầu tiên:", first_five)
last_five = squares[-5:]
print("5 số bình phương cuối cùng:", last_five)
# 17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def is_prime(n):
    if n <= 1:
        print("False")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("False")
    else:
        print("True")
def all_primes(lst):
    for num in lst:
        if not is_prime(num):
            print("False")
    else:
        print("True")
print(all_primes([0, 3, 4, 7, 9]))   #False
print(all_primes([3, 5, 7, 13]))   #True
# 18. Write a Python program to generate all permutations of a list in Python.
import itertools
data = [1, 2, 3]
perms = itertools.permutations(data)
for p in perms:
    print(p)
# 19. Write a Python program to calculate the difference between the two lists.
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]
diff1 = list(set(list1) - set(list2))
print("Phần tử chỉ có trong list1:", diff1)
diff2 = list(set(list2) - set(list1))
print("Phần tử chỉ có trong list2:", diff2)
# 20. Write a Python program to access the index of a list.
my_list = ['a', 'b', 'c', 'd']
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)
# 21. Write a Python program to convert a list of characters into a string.
chars = ['P', 'y', 't', 'h', 'o', 'n']
result = ''.join(chars)
print("Chuỗi sau khi chuyển đổi là:", result)
# 22. Write a Python program to find the index of an item in a specified list.
my_list = ['apple', 'banana', 'cherry', 'date', 'banana']
item = 'banana'
index = my_list.index(item)
print(f"Phần tử '{item}' xuất hiện lần đầu ở vị trí index:", index)
# 23. Write a Python program to flatten a shallow list.
list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sub_list in list:
    for item in sub_list:
        flat_list.append(item)
print(flat_list)
# 24. Write a Python program to append a list to the second list.
list1 = [1, 2, 3]
list2 = ['a', 'b']
list2.append(list1)
print(list2)
import random
my_list = [10, 20, 30, 40, 50]
index = random.randint(0, len(my_list) - 1)
item = my_list[index]
print("Phần tử được chọn:", item)
# 26. Write a Python program to check whether two lists are circularly identical.
def are_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    doubled_list = list1 + list1
    return ' '.join(map(str, list2)) in ' '.join(map(str, doubled_list))
# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
# 28. Write a Python program to find the second largest number in a list.
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]
# 29. Write a Python program to get unique values from a list.
def get_unique_values(numbers):
    return list(set(numbers))
# 30. Write a Python program to get the frequency of elements in a list.
def get_frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
# 31. Write a Python program to count the number of elements in a list within a
# specified range.
def count_in_range(numbers, low, high):
    count = 0
    for num in numbers:
        if low <= num <= high:
            count += 1
    return count
# 32. Write a Python program to check whether a list contains a sublist.
def contains_sublist(lst, sublist):
    n, m = len(lst), len(sublist)
    if m == 0:
        return True
    if m > n:
        return False
    for i in range(n - m + 1):
        if lst[i:i + m] == sublist:
            return True
    return False
# 33. Write a Python program to generate all sublists of a list.
my_list = [1, 2, 3]
sublists = []
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list) + 1):
        sublists.append(my_list[i:j])
print("Danh sách ban đầu:", my_list)
print("Tất cả sublists:", sublists)
# 34. Write a Python program that uses the Sieve of Eratosthenes method to
# compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον
# Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number
# sieves, is a simple, ancient algorithm for finding all prime numbers up to any
# given limit.
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [i for i in range(n + 1) if primes[i]]
    return prime_numbers
# 35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
my_list = ['p', 'q']
n = 5
result = []
for i in range(1, n + 1):
    for item in my_list:
        result.append(item + str(i))
print(result)
# 36. Write a Python program to get a variable with an identification number or
# string.
x = 100
variable_id = id(x)
print("Giá trị của biến x:", x)
print("ID của biến x:", variable_id)
# 37. Write a Python program to find common items in two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_items = []
for item in list1:
    if item in list2:
        common_items.append(item)
print("Các phần tử chung:", common_items)
# 38. Write a Python program to change the position of every n-th value to the
# (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
lst = [0, 1, 2, 3, 4, 5]
for i in range(0, len(lst)-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print("Danh sách sau khi đổi chỗ:", lst)
# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
nums = [11, 33, 50]
str_nums = [str(num) for num in nums]
joined_str = ''.join(str_nums)
result = int(joined_str)
print("Input list:", nums)
print("Single integer:", result)
# 40. Write a Python program to split a list based on the first character of a word.
words = ["apple", "banana", "cherry", "apricot", "blueberry", "avocado"]
result = {}
for word in words:
    first_char = word[0]
    if first_char not in result:
        result[first_char] = []
    result[first_char].append(word)
print("Original list:", words)
print("Grouped by first character:")
for key, group in result.items():
    print(f"{key}: {group}")
# 41. Write a Python program to create multiple lists.
lists = []
for i in range(5):
    lists.append([])

print("Multiple empty lists:")
print(lists)
# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
missing_in_list2 = set(list1) - set(list2)
additional_in_list2 = set(list2) - set(list1)
print("Missing values in second list: ", ','.join(missing_in_list2))
print("Additional values in second list: ", ','.join(additional_in_list2))
# 43. Write a Python program to split a list into different variables.
color = ["Red", "Green", "White", "Black"]
c1, c2, c3, c4 = color
print(c1)
print(c2)
print(c3)
print(c4)
# 44. Write a Python program to generate groups of five consecutive numbers in a
# list.
result = [(range(i, i+5)) for i in range(1, 21, 5)]
print(result)
# 45. Write a Python program to convert a pair of values into a sorted unique array.
pairs = [(1, 2), (3, 4), (1, 2)]
all_values = [x for pair in pairs for x in pair]
unique_values = set(all_values)
sorted_list = sorted(unique_values)
print("Danh sách sau khi sắp xếp và loại trùng:", sorted_list)
# 46. Write a Python program to select the odd items from a list.
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_items = [x for x in numbers if x % 2 != 0]
print("Các phần tử lẻ trong danh sách:", odd_items)
# 47. Write a Python program to insert an element before each element of a list.
my_list = ['a', 'b', 'c']
element = 'X'
result = []
for item in my_list:
    result.append(element)
    result.append(item)
print("Danh sách sau khi chèn:", result)
# 48. Write a Python program to print nested lists (each list on a new line) using
# the print() function.
my_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
for sub_list in my_list:
    print(sub_list)
# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
# "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
# 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = []
for name, code in zip(color_names, color_codes):
    color_dict = {'color_name': name, 'color_code': code}
    result.append(color_dict)
print(result)
# 50. Write a Python program to sort a list of nested dictionaries.
my_list = [
    {'name': 'John', 'age': 25},
    {'name': 'Alex', 'age': 30},
    {'name': 'Chris', 'age': 20}
]
sorted_list = sorted(my_list, key=lambda x: x['age'])
print("Danh sách sau khi sắp xếp:")
for item in sorted_list:
    print(item)
# 51. Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [sample_list[i::n] for i in range(n)]
print("Danh sách sau khi tách:")
print(result)
# 52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green",
# "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
set1 = set(color1)
set2 = set(color2)
diff1 = list(set1 - set2)
diff2 = list(set2 - set1)
print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)
# 53. Write a Python program to create a list with infinite elements.
def infinite_list():
    num = 0
    while True:
        yield num
        num += 1
numbers = infinite_list()
result = [next(numbers) for _ in range(10)]
print(result)
# 54. Write a Python program to concatenate elements of a list.
list1 = ['Python', 'is', 'fun']
result = ' '.join(list1)
print(result)
# 55. Write a Python program to remove key-value pairs from a list of dictionaries.
list_of_dicts = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Paris"},
    {"name": "Charlie", "age": 35, "city": "London"}
]
key_to_remove = "age"
for d in list_of_dicts:
    d.pop(key_to_remove, None)
print(list_of_dicts)
# 56. Write a Python program to convert a string to a list.
text = "Hello"
char_list = list(text)
print(char_list)
# 57. Write a Python program to check if all items in a given list of strings are equal
# to a given string.
string_list = ["apple", "apple", "apple"]
check_str = "apple"
result = all(item == check_str for item in string_list)
print("Danh sách:", string_list)
print("Chuỗi kiểm tra:", check_str)
print("Tất cả phần tử đều bằng chuỗi kiểm tra?", result)
# 58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
list1[-1:] = list2
print("Danh sách sau khi thay thế:", list1)
# 59. Write a Python program to check whether the n-th element exists in a given
# list.
my_list = [10, 20, 30, 40, 50]
int(input("Nhập giá trị n: "))
if 0 <= n < len(my_list):
    print(f"Phần tử ở vị trí {n} là: {my_list[n]}")
else:
    print(f"Không tồn tại phần tử ở vị trí {n}.")
# 60. Write a Python program to find a tuple, the smallest second index value from
# a list of tuples.
my_list = [(4, 10), (1, 25), (3, 5), (7, 8)]
result = min(my_list, key=lambda x: x[1])
print("Tuple có phần tử thứ hai nhỏ nhất là:", result)