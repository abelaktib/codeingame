#Mad pod racings
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop

while True:
    boost = 0 
    # next_checkpoint_x: x position of the next checkpoint
    # next_checkpoint_y: y position of the next checkpoint
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    thrust = 100
    if next_checkpoint_dist < 30:
        thrust -= 5
    if boost == 8 :
        thrust = "BOOST"

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 8
    else:
        thrust = 100


    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    boost += 1
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)  


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
