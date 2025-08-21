# 1. Write a Python program to calculate the length of a string.
import textwrap

chuoi = input('Nhập một chuỗi: ')
print(len(chuoi))
# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
chuoi = 'google.com'
tan_suat = {}
for ky_tu in chuoi:
    if ky_tu in tan_suat:
        tan_suat[ky_tu] += 1
    else:
        tan_suat[ky_tu] = 1
print(tan_suat)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
chuoi = input('Nập một chuỗi: ')
if len(chuoi) < 2:
    ket_qua = " "
else:
    ket_qua = chuoi[:2] + chuoi[-2:]
print(ket_qua)
# 4. Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
chuoi = input('Nhập một chuỗi: ')
ky_tu_dau = chuoi[0]
chuoi_moi = ky_tu_dau + chuoi[1:].replace(ky_tu_dau, '$')
print(chuoi_moi)
# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
chuoi_1 = input('Nhập mô chuỗi: ')
chuoi_2 = input('Nhập một chuỗi: ')
chuoi_1_moi = chuoi_2[:2] + chuoi_1[2:]
chuoi_2_moi = chuoi_1[:2] + chuoi_2[2:]
ket_qua = chuoi_1_moi + " " + chuoi_2_moi
print(ket_qua)
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
chuoi = input('Nhập một chuỗi: ')
if len(chuoi) < 3:
    ket_qua = chuoi
elif chuoi.endswith('ing'):
    ket_qua = chuoi + 'ly'
else:
    ket_qua = chuoi + 'ing'
print(ket_qua)
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
chuoi = input('Nhập một chuỗi: ')
pos_not = chuoi.find('not')
pos_poor = chuoi.find('poor')
if pos_not != -1 and pos_poor != -1 and pos_not < pos_poor:
    chuoi_moi = chuoi[:pos_not] + 'good' + chuoi[pos_poor+4:]
else:
    chuoi_moi = chuoi
print(chuoi_moi)
# 8. Write a Python function that takes a list of words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def tim_tu_dai_nhat(danh_sach_tu):
    tu_dai_nhat = max(danh_sach_tu, key=len)
    return tu_dai_nhat, len(tu_dai_nhat)
danh_sach_tu = ['apple', 'banana', 'strawberry']
tu, do_dai = tim_tu_dai_nhat(danh_sach_tu)
print(tu)
print(do_dai)
# 9. Write a Python program to remove the nth index character from a nonempty string.
chuoi = input('Nhập một chuỗi: ')
n = int(input('Nhập chỉ số n cần xóa: '))
chuoi_moi = chuoi[:n] + chuoi[n+1:]
print(chuoi_moi)
# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.
chuoi = input('Nhập một chuỗi: ')
if len(chuoi) < 2:
    chuoi_moi = chuoi[-1] + chuoi[1:-1] + chuoi[0]
else:
    chuoi_moi = chuoi
print(chuoi_moi)
# 11. Write a Python program to remove characters that have odd index values in a given string.
chuoi = input('Nhập một chuỗi: ')
for i in range(len(chuoi)):
    if i % 2 == 0:
        chuoi_moi += chuoi[i]
print('Chuỗi sau khi xóa kí tự lẻ: ', chuoi_moi)
# 12. Write a Python program to count the occurrences of each word in a given sentence.
cau = input('Nhập một câu: ')
tu_ds = cau.split()
dem_tu = {}
for tu in tu_ds:
    if tu in dem_tu:
        dem_tu[tu] += 1
    else:
        dem_tu[tu] =1
print(dem_tu)
# 13. Write a Python script that takes input from the user and displays that input back in upper
# and lower cases.
du_lieu = input('Nhập một chuỗi: ')
print(du_lieu.upper())
print(du_lieu.lower())
# 14. Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
chuoi = input('Nhập các từ, cách nhau bằng dấu phẩy: ')
danh_sach_tu = [tu.strip() for tu in chuoi.split(",")]
tu_phan_biet = sorted(set(danh_sach_tu))
chuoi_sau_thay_doi = join(tu_phan_biet)
print(chuoi_sau_thay_doi)
# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
print(add_tags)
# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle(container, word):
    mid = len(container) // 2
    return container[:mid] + word + container[mid:]
print(insert_string_middle)
# 17. Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def insert_end(s):
    if len(s) < 2:
        return "Độ dài ít nhất bằng 2"
    last_two_word = s[-2:]
    return last_two_word * 4
print(insert_end)
# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
def first_three(s):
    if len(s) < 3:
        return s
    else:
        return s[:3]
print(first_three)
# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
def last_part(s, sep):
    parts = s.split(sep, 1)
    return parts[0]
print(last_part)
# 20. Write a Python function to reverse a string if its length is a multiple of 4.
def boi_so_cua_4(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s
print(boi_so_cua_4)
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
def so_ky_tu_viet_hoa(s):
    upper_count = sum(1 for c in s[:4] if c.isupper())
    if upper_count >= 2:
        return s.upper()
    else:
        return s
print(so_ky_tu_viet_hoa)
# 22.Write a Python program to sort a string lexicographically.
def danh_sach_ky_tu_da_sap_xep(s):
    return ''.join(sorted(s))
print(danh_sach_ky_tu_da_sap_xep)
# 23. Write a Python program to remove a newline in Python.
text = 'Hello everyone/I am 20 years old'
ket_qua_1 = text.strip()
print(ket_qua_1)
# 24. Write a Python program to check whether a string starts with specified characters.
text = input('Nhập chuỗi: ')
prefix = input('Nhập ký tự hoặc chuỗi cần kiểm tra đầu: ')
if text.startswith(prefix):
    print(f"Chuỗi '{text}' bắt đầu bằng '{prefix}'.")
else:
    print(f"Chuỗi '{text}' không bắt đầu bằng '{prefix}'.")
# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.
def ceasar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
plaintext = input('Nhập chuỗi cần mã hóa: ')
shift = int(input('Nhập số shift: '))
print(ceasar_cipher)
# 26. Write a Python program to display formatted text (width=50) as output.
def format_text():
    sample_text = ('Học lập trình Python không chỉ giúp bạn hiểu rõ về cách máy tính hoạt động mà còn phát triển tư duy logic, khả năng giải quyết vấn đề và sáng tạo. Khi bạn thành thạo, bạn có thể xây dựng ứng dụng, phân tích dữ liệu, hay thậm chí tạo trò chơi thú vị cho riêng mình.')
    formatted_text = textwrap.fill(sample_text, width=50)
print(formatted_text)
# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
def xoa_thut_le(text):
    return textwrap.dedent(text)
sample_text = """ Đây là dòng đầu tiên.
                      Đây là dòng thứ hai.
                  Đây là dòng thứ ba."""
print(sample_text)
# 28. Write a Python program to add prefix text to all of the lines in a string.
def add_prefix(text, prefix):
    lines = text.splitlines()
    new_lines = [prefix + line for line in lines]
    return '\n'.join(new_lines)
sample_text = """Dòng thứ nhất
Dòng thứ hai
Dòng thứ ba"""
prefix_text = ">>> "
print(sample_text)
# 29. Write a Python program to set the indentation of the first line.
def dong_dau_tien(text, indent_spaces):
    lines = text.splitlines()
    if lines:
        lines[0] = ' ' * indent_spaces + lines[0]
    return '\n'.join(lines)
sample_text = """Dòng thứ nhất sẽ thụt lề.
Dòng thứ hai giữ nguyên.
Dòng thứ ba giữ nguyên."""
indent_size = 7
print(sample_text)
# 30. Write a Python program to print the following numbers up to 2 decimal places.
chuoi_so = float(input('Nhập chuỗi số: '))
print(f"{x:.2f}")
# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
so = float(input('Nhập số: '))
print(f"{so:+.2f}")
print(f"{so:-.2f}")
# 32. Write a Python program to print the following positive and negative numbers with no
# decimal places.
so = float(input('Nhập số: '))
print(f"{so:.0f}")
# 33. Write a Python program to print the following integers with zeros to the left of the specified
# width.
num = int(input('Nhập giá trị: '))
print(f"{num:03d}")
# 34. Write a Python program to print the following integers with '*' to the right of the specified
# width.
num = int(input('Nhập giá trị: '))
print(f"{num:*<3d}")
# 35. Write a Python program to display a number with a comma separator.
num = float(input('Nhập giá trị: '))
print(f"{num:,}")
# 36. Write a Python program to format a number with a percentage.
num = float(input('Nhập số: '))
print(f"{num:.2%}")
# 37. Write a Python program to display a number in left, right, and center aligned with a width of
# 10.
x = int(input('Nhập giá trị: '))
print(f"{x:<10}")
print(f"{x:>10}")
print(f"{x:^10}")
# 38. Write a Python program to count occurrences of a substring in a string.
chuoi_lon = "python is amazing, python is powerful"
chuoi_nho = "python"
count = text.count(chuoi_nho)
print(f"Chuỗi nhỏ: '{chuoi_nho}'appears {count} times.")
# 39. Write a Python program to reverse a string.
text = "Hello World"
reversed_text = text[::-1]
print(reversed_text)
# 40. Write a Python program to reverse words in a string.
text = "Hello World Python"
words = text.split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)
print(result)
# 41. Write a Python program to strip a set of characters from a string.
text = "--Hello World--"
chars = "-Hel"
result = text.strip(chars)
print(result)
# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
text = 'thequickbrownfoxjumpsoverthelazydog'
đem_tu= count(text)
if count > 1:
        print(char, count)
# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
length = float(input("Nhập chiều dài hcn(cm): "))
width = float(input("Nhập chiều rộng hcn (cm): "))
radius = float(input("Nhập bán kính hình trụ (cm): "))
height = float(input("Nhập chiều cao hình trụ (cm): "))
area_rectangle = length * width
volume_cylinder = math.pi * (radius ** 2) * height
print(f"The area of the rectangle is {area_rectangle:.2f}cm\u00b2")
print(f"The volume of the cylinder is {volume_cylinder:.3f}cm\u00b3")
# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
chuoi = "w3resource"
print(f"Current character {char} position at {index}")
# 45. Write a Python program to check whether a string contains all letters of the alphabet.
chuoi = "The quick brown fox jumps over the lazy dog"
chuoi_moi = chuoi.lower()
chars_in_text = set(chuoi_moi)
if set(string.ascii_lowercase).issubset(chars_in_text):
    print("The string contains all the letters of the alphabet.")
else:
    print("The string does NOT contain all the letters of the alphabet.")
# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
text = "The quick brown fox jumps over the lazy dog."
words_list = text.split()
print(words_list)
# 47. Write a Python program to lowercase the first n characters in a string.
text = "PYTHON Programming Language"
n = 6
result = text[:n].lower() + text[n:]
print(result)
# 48. Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
so = "32.054,23"
result = so.replace(',', '.')
result = so.replace('.', ',')
print(result)
# 49. Write a Python program to count and display vowels in text.
text = "Write a Python program to count and display vowels in text."
text = text.lower()
nguyen_am = "aeiou"
dem_nguyen_am = {}
for char in text:
    if char in nguyen_am:
        dem_nguyen_am[char] = dem_nguyen_am.get(char, 0) + 1
print("Nguyên âm trong text: ")
# 50. Write a Python program to split a string on the last occurrence of the delimiter.
text = "one-two-three-four"
parts = text.rsplit('-', 1)
print(text)
# 51. Write a Python program to find the first non-repeating character in a given string.
def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
# 52. Write a Python program to print all permutations with a given repetition number of characters
# of a given string.
def permutation_with_repetition(s, r):
    perms = itertools.product(s, repeat=r)
    for p in perms:
        print(''.join(p))
# 53. Write a Python program to find the first repeated character in a given string.
def first_repeated_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None
# 54. Write a Python program to find the first repeated character in a given string where the index
# of the first occurrence is smallest.
def first_repeated_char_min_index(s):
    first_index = {}
    min_index = len(s)
    result_char = None
    for i, ch in enumerate(s):
        if ch in first_index:
            if first_index[ch] < min_index:
                min_index = first_index[ch]
                result_char = ch
        else:
            first_index[ch] = i
    return result_char
