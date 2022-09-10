# function to check string is palindrome or not using for loop
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
