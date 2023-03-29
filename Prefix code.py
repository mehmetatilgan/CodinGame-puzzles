Bi = []
Ci = []
answer = ""
condition = True

n = int(input())

if n > 0:
    for i in range(n):
        inputs = input().split()
        b = inputs[0]
        Bi.append(b)
        c = int(inputs[1])
        Ci.append(c)
else:
    answer = "DECODE FAIL AT INDEX 0"
    condition = False

encodedString = input()
decodeCounter = 0
temp = len(encodedString)

while(condition):
    for i in range(len(Bi)):
        if encodedString.startswith(Bi[i]):
            answer += chr(Ci[i])
            encodedString = encodedString.replace(Bi[i],"",1)
            decodeCounter += len(Bi[i])
    if temp == len(encodedString):
        answer = "DECODE FAIL AT INDEX "+str(decodeCounter)
        break
    else:
        temp = len(encodedString)
    if encodedString == "":
        condition = False

print(answer)