from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean
from collections import Counter

#  --> 
# function writes 64 pixel string array to file in parsable format
def createExamples():
    numberArrayExamples = open('num_ar_examples.txt', 'a')
    numbersWeHave = range(0, 10)
    numberOfNums = range(1, 10)
    for eachNum in numbersWeHave:
        for furtherNum in numberOfNums:
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

# array --> array
# function takes in an 8x8 pixel image array of any color and uses threshold algorithm to make pixels black or white (normalize)
def threshold(imageArray):
	balanceAr = []
	newAr = imageArray
	for eachRow in imageArray:
			for eachPix in eachRow:
					avgNum = mean(eachPix[:3])
					balanceAr.append(avgNum)
	balance = mean(balanceAr)
	for eachRow in newAr:
	  	for eachPix in eachRow:
	  			#white
	    		if mean(eachPix[:3]) > balance:
        			eachPix[0] = 255
        			eachPix[1] = 255
        			eachPix[2] = 255
        			eachPix[3] = 255
        	#black
	    		else:
       				eachPix[0] = 0
        			eachPix[1] = 0
        			eachPix[2] = 0
        			eachPix[3] = 255
	return newAr

# array --> array
# takes in image array of custom image made in gimp, converts it to a usable format
def makeUsable(imageArray):
	newAr = imageArray
	for eachRow in newAr:
		for eachPix in eachRow:
			if eachPix[3] == 0:
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
	return newAr


# --> array 
# return array of examples from 'numArEx1.txt' (a 90 element list, iterables in form  -- #:: 64 RGBA pixels --)
def get_examples():
	loadExamps = open('numArEx1.txt', 'r').read()
	loadExamps = loadExamps.split('\n') 
	return loadExamps

# string --> string
# return image array in str/list form 
def get_imageAr(filePath):
	#put image at filePath into RGBA string form (64 pixels) to ready for comparison
	i = Image.open(filePath)
	iar = np.array(i)
	iar = makeUsable(iar)
	iarl = iar.tolist()
	inQuestion = str(iarl)
	return inQuestion

# string --> array
# take in Image filePath and return Counter() Array for weights of nums 1-9 from reference set
def whatNumIsThis(filePath):

	matchedAr = []
	loadExamps = get_examples()

	inQuestion = get_imageAr(filePath)
	# print(inQuestion)


	#eachExample is a the RGBA pixel array for a num 0-9
	#loadExamps length = 90
	for eachExample in loadExamps: 
		splitEx = eachExample.split('::')
		currentNum = splitEx[0]
		currentAr = splitEx[1]

		# both each vars are an array (length of 64) of individual pixels
		eachPixEx = currentAr.split('],')

		eachPixInQ = inQuestion.split('],')

		x = 0
		while x < len(eachPixEx):
			if eachPixEx[x] == eachPixInQ[x]:
				matchedAr.append(int(currentNum))
			x=x+1

	x =  Counter(matchedAr)
	print(x)



whatNumIsThis('images/test_9.png')





















# i = Image.open('images/numbers/y0.5.png')
# iar = np.asarray(i)

# plt.imshow(iar)
# print(iar)
# plt.show()





# i = Image.open('images/test.png')
# iar = np.array(i)

# print(makeUsable(iar))


# createExamples()



# i = Image.open('images/numbers/0.1.png')
# iar = np.array(i)

# i2 = Image.open('images/numbers/y0.4.png')
# iar2 = np.array(i2)

# i3 = Image.open('images/numbers/y0.5.png')
# iar3 = np.array(i3)

# i4 = Image.open('images/sentdex.png')
# iar4 = np.array(i4)

# iar = threshold(iar)
# iar2 = threshold(iar2)
# iar3 = threshold(iar3)
# iar4 = threshold(iar4)

# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

# ax1.imshow(iar)
# ax2.imshow(iar2)
# ax3.imshow(iar3)
# ax4.imshow(iar4)


# plt.show()

# createExamples()