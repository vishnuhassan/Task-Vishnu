print("-------------Program 1---------------")
print("-------------check string is palindrome using for loop-----------")
def isPalindrome(str):
	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

# main function
s = input("Enter the word: ")
result = isPalindrome(s)
if (result):
    print("Yes, it's palindrome")
else:
    print("No' it's not palindrome")
print("**************************************************************************")
print("----------------------generator method to find palindrome--------------")
s = "malayalam"
str1 = ""
def Generator(s):
    for i in s[::-1]:
        yield i
               
for i in Generator(s): 
    str1 +=i
    
if str1 == s:
    print("yes ,it is Palindrome")
else:
    print("No ,it is not Palindrome")
print("****************************************************************************")
print("---------------Program 2------------------")
print("---------------adding two numbers by individual elements----------------")

n1 = 1234 # int(input("Enter number1 :" ))
n2 = 9999 # int(input("Enter number2 :" ))
# converting int into string
n1 = str(n1)
n2 = str(n2)
list1 = list(n1)
list2 = list(n2)
# adding two list using list comprehension
res_list = [int(list1[i]) + int(list2[i]) for i in range(len(list1))]

# intializing sum to add all the elments inside the res_list
sum = 0
for i in res_list:
    sum += i

#output
print("OUTPUT:",sum)

print("**************************************************************************")

print("-----------------------Program 3-----------------------")
print("----------------------Reverse String only alphabets----------------------")

st = "ab@#cd!ef"
   # Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba
def reverseString(text):
    index = -1

    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


# Driver code
string = "ab@#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print(string)
print("Output string: ", "".join(string))

print("**************************************************************")

print("-----------------Program 4---------------------")
print("-----------------findout elements duplicate count output in  dict format---------------")

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# convert the list into string
test_str = ''.join(some_list)

dicx = {}
# iterate the each element in string
for i in test_str:
    if i in dicx:
        dicx[i] += 1
    else:
        dicx[i] = 1

print(dicx)

print("***************************************************************")
print("--------------------------Program 5----------------------")
print("--------------------adding respect to integer and respect to string-------------------")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
Output = []
list1 = []
list2 = []
r = []
for i in list(t2):
    if type(i) == int:
        list1.append(i)
    else:
        list2.append(i)

add = list1 + list2

for i in range(len(t1)):
    v = list(t1)
    m = v[i] + add[i]
    r.append(m)
output = tuple(r)
print(output)

print("******************************************************")
print("----------------Program 6---------------------")
print("---------------Remove leading zeros from IP address-----------------")
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)

print("******************************************************")

print("----------------Program 7---------------------")
print("---------------all list convert into a single list-----------------")
from collections.abc import Iterable

# recursively loop over the list and check if an item is iterable(strings are iterable too, but skip them) or not.


def flatten(list):

    for item in list:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item


lis = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(list(flatten(lis)))
print("*******************************************************")

print("--------------------------Program 8--------------------------")
"""
Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total
"""

file = open('sample.txt', 'r')
# no of lines in file
content = file.readlines()
no_lines = len(content)

print("No.of.lines: ", no_lines)

# no of char in each line
count = 0
for i in content:
    for j in i:
        if j != " ":
            count += 1
    print("In this line characters are {} ".format(count))
    count = 0

# no.of.vowels and consonants
vowel_count = 0
total_char = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
for i in content:
    for j in i:
        total_char += 1
        if j in vowels:
            vowel_count += 1
print("The total no of vowels are {}".format(vowel_count))
consonants = total_char - vowel_count
print("The total consonants are {}".format(consonants))


print("***************************************************************************")
