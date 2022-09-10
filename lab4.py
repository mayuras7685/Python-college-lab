# list1 = [1, '2', '3', '4', '5', '6', '7', '8']
# print(int(list1[0])+list1[1])

#remove duplicates
ls = [1, 2, 4, 3, 3, 5, 6, 2]

def rev_dup(list):
  new_ls=[]
  for i in list:
    if i not in new_ls:
      new_ls.append(i)
  return print(new_ls) 

rev_dup(ls)
#output: [1, 2, 4, 3, 5, 6]

# add list elements using for loop, while loop, enumerate function and in built method

l = [1,2,4,5,67,86,45]

#using for loop
sum = 0
for i in l:
  sum = sum + i
print(sum)

#using while loop
a=0
s=0
while a<len(l):
  s = s + l[a]
  a = a + 1
print(s)

#using enumerate
add = 0 
for a, i in enumerate(l):
  add = add + i 

print(add)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# #using in built method
# total = sum(l1)
# print(total)

#-------------------------------------------------------------------------------
for i in range(-10):
  print(i)
#why error not occurs and not display any output

for i in range(-10, 0):
  print(i)
"""
output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
"""