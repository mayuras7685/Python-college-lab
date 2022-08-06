"""4.	REPEAT ABOVE PROGRAM 
TO USE CONTINUE AND PASS STATEMENT FOR LETTER ‘O’.

"""

#for continue 
str2 = "ABOCDEOFGHIGKLMNOPQRSTUVWXYZ"

for i in str2:
  if i =="O":
    continue
  print(i)


"""
output :
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
P
Q
R
S
T
U
V
W
X
Y
Z
"""

#for pass

for i in str2:
  if i =="O":
    pass
  print(i)

"""
output :
A
B
O
C
D
E
O
F
G
H
I
G
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
"""

"""5.	WRITE A PROGRAM TO ADD THE NUMBER 
STORED IN ARRAY TILL THE COUNTER REACHES TO USER DEFINED COUNT
"""

a = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]
b = int(input())

sum = 0
if b in a:
  for i in range(1, b+1):
    sum = sum + i
  print(sum)
else:
  print(b,"is not in array")