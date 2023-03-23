import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    liste = list()
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        liste.append(mountain_h)

    max = 0
    counter = 0
    index = 0
    for i in liste:
        counter += 1
        if i > max:
            max = i
            index = counter -1

    print(index)
