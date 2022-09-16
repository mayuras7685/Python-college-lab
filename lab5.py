# 1.	WRITE A FUNCTION THAT RETURNS ABSOLUTE VALUE.

x= float(input("Enter a value"))
if x<0:
    x= x*-1
print(x)

"""
Output:
Enter a value -1
-1
1.0
"""


# 2.	 WRITE A FUNCTION TO APPEND [11,22,33] TO THE EXISTING LIST 
def lists_append(list):
    list.append(11)
    list.append(12)
    list.append(13)
    print(list)

Sequence=[8,9,10]
lists_append(Sequence)

# Output: [8, 9, 10, 11, 12, 13]


#3.	WRITE A FUNCTION TO PRINT DEFAULT ARGUMENT  WHEN IT IS NOT PASSED TO FUNCTION
def my_function():
    print("This is a function without arguments")
my_function()

# Output: This is a function without arguments


#4.	WRITE A FUNCTION TO RETURN THE SUM OF TWO NUMBER.DEFINED SUM AS GLOBAL AND LOCAL VARIABLE AND SEE THE DIFFERENCE
def sum_function(num1,num2):
    sum=0
    sum=num1+num2
    print(sum)

sum=10
sum_function(3,6)

# Output: 9


# 5.	WRITE A PYTHON PROGRAM TO REVERSE THE STRING USING FUNCTION AND WHILE LOOP 
def string_reverse(s):
    S=""
    length=len(s) -1
    while length>=0:
        S = S + s[length]
        length =length - 1
    print("Your reversed string is  "+ S)

string_reverse("india")

#Output: Your reversed string is  aidni

#6.	WRITE A PYTHON FUNCTION THAT ACCEPTS A STRING AND CALCULATE THE NUMBER OF UPPER CASE LETTERS AND LOWER CASE LETTERS 

def calculate(R):
    U=0
    L=0
    length = len(R)-1
    while length>=0:
        if R[length].isupper():
            U = U+1
        if R[length].islower():
            L=L+1
        length=length-1

    print("Number of lower case letter :")
    print(L)
    print("Number of upper case letter :" )
    print(U)
calculate("HiTLeR@1944")

"""
Output:
Number of lower case letter :
2
Number of upper case letter :
4
"""