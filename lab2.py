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

