#Shadows of the Knight - Episode 1
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
minx = miny = 0
maxx = w - 1 
maxy = h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir.find("U")>-1:
        maxy = y0 - 1
    elif bomb_dir.find("D")>-1:
        miny = y0 + 1
    if bomb_dir.find("L")>-1:
        maxx = x0 - 1
    elif bomb_dir.find("R")>-1:
        minx = x0 + 1

    x0 = minx + round((maxx - minx) / 2)
    y0 = miny + round((maxy - miny) / 2)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(int(x0), int(y0))