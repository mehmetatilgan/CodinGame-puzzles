w= int(input())
h = int(input())
t = list(map(int, input().split()))

image = [[' ' for i in range(w)] for i in range(h)]

currentColor = '*'


row, col = 0, 0
while row < h:
    for pixels in t:
        for a in range(pixels):
            image[row][col] = currentColor
            col += 1
            if col == w:
                col = 0
                row += 1
        currentColor = '*' if currentColor == ' ' else ' '
for row in image:
    print('|' + ''.join(row) + '|')
#loops,decompression,2d arrays