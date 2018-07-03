import cv2
import numpy
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def checkEmptyLine(line):
    for i in line:
        if i==0:
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


def drawBorder(limit = 30):

    for line in out[50:mid_height]:
        start = 0
        end = out.shape[1] - 1
        while line[start].sum() != 0 and start < width-1:
            start = start + 1
        while line[end].sum() != 0 and start <= end:
            end = end - 1
        if out[0][start-limit:start+limit].sum() == 255 * 6 * limit: # RGB色域, 2*3=6
            for i in range(20):
                out[i][start-3:start+3] = 0
        if out[0][end - limit:end + limit].sum() == 255 * 6 * limit:
            for i in range(20):
                out[i][end-3:end+3] = 0

    for line in out[mid_height:height-1]:
        start = 0
        end = out.shape[1] - 1
        while line[start].sum() != 0 and start < width-1:
            start = start + 1
        while line[end].sum() != 0 and start <= end:
            end = end - 1
        if out[height-1][start-limit:start+limit].sum() == 255 * 6 * limit: # RGB色域, 2*3=6
            for i in range(20):
                out[height-1-i][start-3:start+3] = 0
        if out[height-1][end - limit:end + limit].sum() == 255 * 6 * limit:
            for i in range(20):
                out[height-1-i][end-3:end+3] = 0


def drawText(pos, value):
    draw = ImageDraw.Draw(outImage)
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

house_raw = cv2.imread('in/test.jpg')
house_gray = cv2.imread('in/test.jpg', 0)
_, house_bin = cv2.threshold(house_gray, 200, 255, cv2.THRESH_BINARY)

top, buttom = cutEdge(house_bin)
house_bin = house_bin[top:buttom]
house_bin = house_bin.transpose()
left, right = cutEdge(house_bin)
house_bin = house_bin[left:right]
house_bin = house_bin.transpose()

for line in house_bin:
    start = 0
    end = right-left-1
    while line[start] != 0 and start < house_bin.shape[1]-1:
        start = start + 1
    while line[end] != 0 and start <= end:
        end = end - 1
    for i in range(start, end):
        line[i] = 0

house_raw = house_raw[top:buttom, left:right]

border = 50
out = Image.new('RGB', (right-left+2*border, buttom-top+2*border), 'white')
out.paste(Image.fromarray(house_bin), (border, border))

bin_width, bin_height = out.size
out = numpy.asarray(out)
out.flags.writeable = True

width = out.shape[1]
height = out.shape[0]
print(width, height)
mid_width = int(width/2)
mid_height = int(height/2)

drawBorder()
out = numpy.transpose(out, (1, 0, 2))
print(out.shape)
width, height = height, width
drawBorder()
out = numpy.transpose(out, (1, 0, 2))
width, height = height, width
print(out.shape)
outImage = Image.fromarray(out)
outImage.paste(Image.fromarray(house_raw), (border, border))

for i in range(4):
    calcValue()
    out = numpy.rot90(out)
    outImage = Image.fromarray(numpy.rot90(numpy.array(outImage)))
    width, height = height, width

titles = ['raw', 'gray', 'binary', 'result']
images = [house_raw, house_gray, house_bin, outImage]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

# cv2.namedWindow('house')
# cv2.imshow('house', house_bin)
# cv2.waitKey()