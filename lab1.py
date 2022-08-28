""" 1.	INPUT NUMBER THROUGH THE USER AND FIND OUT WHETHER THE NUMBER IS ZERO,
POSITIVE OR NEGATIVE."""

x = float(input())

if x>0 :
  print("Given Number is Positive")
elif x<0 :
  print("Given Number is Negative")
else:
  print("Given Number is Zero")

# output for 5 is Given Number is Positive

"""2.	INITIALIZE THE ARRAY WITH THE STRING. INPUT STRING THROUGH THE USER AND 
OUTPUT TRUE OR FALSE BASED ON THE PRESENCE OR ABSENCE OF STRING."""

str1 = "My name is mayur"
if "mayur" in str1:
  print("True")
else:
  print("False")

# output : True

"""3.	INITIALIZE THE VARIABLE WITH STRING. PRINT ALL THE CHARACTERS UNTIL A
 LETTER ‘O’ IS ENCOUNTERED USING BREAK STATEMENT. """
 
str2 = "ABCDEFGHIGKLMNO"

for i in str2:
  if i =="O":
    break
  print(i)

""" output : 
A
B
C
D
E
F
G
H
I
G
K
L
M
N
"""

