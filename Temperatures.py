# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
temps = []
result = 0
dummy = sys.maxsize
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    temps.append(int(i))  # temps: a temperature expressed as an integer ranging from -273 to 5526

if len(temps) == 0:
    print("0")

else:
    for temp in temps:
        if abs(temp) < dummy:
            dummy = abs(temp)
            result = temp
        elif abs(temp) == abs(result):
            result = max(temp, result)
    print(result)
# loops, arrays, methods