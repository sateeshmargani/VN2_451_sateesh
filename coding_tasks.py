"""
1. Implement palindrome using iterator(for loop) and generator mechanism.
"""
# Using iterator(for loop):

def isPalindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
        return True
string = "MOM"
print(isPalindrome(string))

"""
2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46
"""

def sum_of_digits(num1, num2):
    return int(num1) + int(num2)


n1 = list(str(int(input("Enter n1 : "))))
n2 = list(str(int(input("Enter n2 : "))))
result = list(map(sum_of_digits, n1, n2))
temp = 0
for i in result:
    temp = temp + i
print("output : ", temp)


"""
3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symbols should not be reversed
   # Output: fe@#dc!ba
"""
string = "ab@cd!ef"
string1 = string[::-1]
string1 = list(string1)
reverse = ''
list = []
for idy, val in enumerate(string1):
    if val.isalpha():
        list.append(val)
    else:
        list.insert(idy, string[idy])
rev_string = reverse.join(list)
print(rev_string)

"""
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
"""

list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
sCount = {x:list.count(x) for x in list}
z = dict()
for key, value in sCount.items():
    if value > 1:
        z[key] = value
print(z)

"""
6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
"""

import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)

"""
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
"""

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]


