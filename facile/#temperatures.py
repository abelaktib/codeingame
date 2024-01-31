import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n!=0 :
    temperature = input().split(' ')
    min = int(temperature[0])
    for i in temperature:
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        
        if (abs(min)>abs(t)  or (abs(min)==abs(t) and t >min)):
            min = t 
else:
    min = 0
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(min)