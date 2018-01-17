from scipy import misc
import numpy as np
import sys
np.set_printoptions(threshold=np.inf)

imgdata = misc.imread('cal_bw.png')
#imgdata = misc.imresize(imgdata, (146, 146))
imgdata = misc.imresize(imgdata, (110, 190))

imgdata2 = []

zeroCount, oneCount = 0, 0

# for each row in the image
for row in imgdata:
    arr = []
    for pixel in row:
        if pixel[0] == 0:
            arr.append(0)
            zeroCount += 1
        else:
            arr.append(1)
            oneCount += 1
    imgdata2.append(arr)



"""
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

print(imgdata2)
print( 2017 * 2 / (oneCount / zeroCount))
"""

print(oneCount, zeroCount)

for row in range(len(imgdata2)):
    for pixel in range(len(imgdata2[row][1::2])):
        imgdata2[row][pixel*2+1] = '+'

for row in imgdata2:
    for pixel in row:
        sys.stdout.write(str(pixel))
    print()
