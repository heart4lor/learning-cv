import cv2
from queue import Queue
import numpy
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def checkEmptyLine(line):
    for i in line:
        if i==255:
            return False
    return True

def cutEdge(array):
    top = 0
    while checkEmptyLine(array[top]):
        top = top + 1

    buttom = array.shape[0] - 1
    while checkEmptyLine(house_bin[buttom]):
        buttom = buttom - 1

    return top, buttom

dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs():
    while(not q.empty()):
        p = q.get()
        i, j = p[0], p[1]
        house_bin[i][j] = 255
        out[i][j] = 255
        for ii in range(4):
            ni, nj = i + dir[ii][0], j + dir[ii][1]
            if(ni < height and nj < width and ni >= 0 and nj >= 0 and house_bin[ni][nj] == 0 and not vis[ni][nj]):
                print(ni, nj, house_bin[ni][nj], vis[ni][nj])
                q.put((ni, nj))
                vis[ni][nj] = 1

def drawText(pos, value):
    draw = ImageDraw.Draw(out)
    font = ImageFont.truetype('in/ubuntu.ttf', 20)
    draw.text(pos, str(value), fill=(0, 0, 0), font=font)


def calcValue():
    prev, now = 0, 0
    for i in range(width - 1):
        if out[10][i].sum() == 255 * 3 and out[10][i + 1].sum() == 0:
            if prev == 0:
                prev = i
            else:
                now = i
                print(prev, now)
                value = now - prev
                pos = prev + int(value * 0.42)
                drawText((pos, 8), value)
                prev = now

house_bin = cv2.imread('in/test.jpg', 0)

house_bin = cv2.Canny(house_bin, 200, 255)
top, buttom = cutEdge(house_bin)
house_bin = house_bin[top-10:buttom+10]
house_bin = house_bin.transpose()
left, right = cutEdge(house_bin)
house_bin = house_bin[left-10:right+10]
house_bin = house_bin.transpose()

height, width = house_bin.shape
out = numpy.zeros((height, width), dtype=int)

q = Queue()
p = (0, 0)
vis = numpy.zeros(house_bin.shape, dtype=bool)
q.put(p)
vis[0][0] = True
bfs()

border = 50
out_ = Image.new('RGB', (width+2*border, height+2*border), 'white')
out_.paste(Image.fromarray(out), (border, border))
out = out_
out = numpy.asarray(out)
print(type(out))
for i in range(4):
    calcValue()
    out = numpy.rot90(out)
    outImage = Image.fromarray(numpy.rot90(numpy.array(out)))
    width, height = height, width

cv2.namedWindow('result')
cv2.imshow('result', out)
cv2.waitKey()
