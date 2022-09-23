project = input("Enter the alphanumeric string: ")
k = int(input("Enter the integer value of characters in one group: "))
div = project.split("-")
char = ""
for x in range(len(div)):
    char = char + str(div[x].upper())
len_1stgrp = len(char)%k
if len_1stgrp == 0:
    len_1stgrp = k
print(len(char)//k)
if len_1stgrp == k:
    number_grps = len(char)//k
else:
    number_grps = (len(char)//k)+1
for x in range(number_grps):
    if x == 0:
        R = char[:(len_1stgrp)]
    else:
        R = R + "-" + char[len_1stgrp + (x-1)*k: len_1stgrp + x*k]
print(R)
