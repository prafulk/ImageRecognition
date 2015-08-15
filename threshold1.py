from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            #print str(eachNum)+ '.'+ str(eachVer)
            imgFilePath = 'images/numbers/'+str(eachNum)+ '.'+ str(eachVer)+ '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist()) #saving arrays to a file

            # Now let us match all the numbers, as in we label each

            lineToWrite = str(eachNum)+ '::'+ eiar1 + '\n'
            numberArrayExamples.write(lineToWrite) 




def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


i = Image.open('images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

threshold(iar3)
threshold(iar4)
threshold(iar2)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan     =4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()