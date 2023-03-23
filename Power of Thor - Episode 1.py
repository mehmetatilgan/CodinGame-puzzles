import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())
    if light_x - initial_tx < 0 and light_y - initial_ty < 0:
        print("NW")
        initial_tx -= 1
        initial_ty -=1
    elif light_x - initial_tx < 0 and light_y - initial_ty > 0:
        print("SW")
        initial_tx -= 1
        initial_ty +=1
    elif light_x - initial_tx > 0 and light_y - initial_ty > 0:
        print("SE")
        initial_tx += 1
        initial_ty +=1
    elif light_x - initial_tx > 0 and light_y - initial_ty < 0:
        print("NE")
        initial_tx += 1
        initial_ty -=1
    elif light_x - initial_tx == 0 and light_y - initial_ty > 0:
        print("S")
        initial_ty +=1
    elif light_x - initial_tx < 0 and light_y - initial_ty == 0:
        print("W")
        initial_tx -= 1
    elif light_x - initial_tx == 0 and light_y - initial_ty < 0:
        print("N")
        initial_ty -=1
    elif light_x - initial_tx > 0 and light_y - initial_ty == 0:
        print("E")
        initial_tx += 1