#naviguer sur 2 chaine de caracteres
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
t2 = input()
result=''

for element1, element2 in zip(t, t2):
    if element1 < element2:
        result += element2
    else:
       result += element1
print(result)

