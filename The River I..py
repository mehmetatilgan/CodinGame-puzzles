import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
r_1 = int(input())
r_2 = int(input())
isRiver = False
listR_1 = [r_1]
listR_2 = [r_2]
result = 0
answer = r_1
answer2 = r_2

while not isRiver:
    for digit in str(listR_1[-1]):
        answer += int(digit)
    listR_1.append(answer)

    for digit in str(listR_2[-1]):
        answer2 += int(digit)
    listR_2.append(answer2)

    for i in listR_2:
        if i in listR_1:
            result = i
            isRiver = True
            break

print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)