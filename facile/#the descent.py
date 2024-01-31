#the descent
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    indice_montagne_big = 0
    hauteur_montagne_big = -1
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        if i == 0 or hauteur_montagne_big < mountain_h:
            indice_montagne_big = i
            hauteur_montagne_big = mountain_h



    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(indice_montagne_big)
