#translate.py by David Chou
#used as part of my Kaggle submission.
#Python 2.7
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals #this makes it so that every string is in unicode, which is important for working with languages #turns out this wasn't needed
import sys
import csv
import io #unicode file opening

def createDict(left, right):
	with io.open(left, "rb") as leftpointer: #io.open instead of open since it's unicode stuff.  Otherwise languages other than English won't be properly translated.
    		l = leftpointer.readlines()

	with io.open(right, "rb") as rightpointer:
    		r = rightpointer.readlines() 
    
	l = [x.rstrip() for x in l] #strip newline chars (rstrip strips many kinds of returns including the default Windows, Mac, and *nix ones.)
	r = [x.rstrip() for x in r] #strip newline chars

	for x in range(0, len(l)):
		l[x] = "\"" + l[x] + "\""
	for x in range(0, len(r)):
                r[x] = "\"" + r[x] + "\""
	#l = ', '.join('"{0}"'.format(w) for w in l) #so that the dictionary looks like {"word":"definition"} instead of {word:definition}
	#r = ', '.join('"{0}"'.format(w) for w in r)
	
	list_tuple = zip(l,r) #zips the two lists into a list of 2-tuples
	dictionary = dict(list_tuple)
	return dictionary

def main():
    if len(sys.argv) != 5: #makes sure correct amount of arguments are inputted.
    	print "The correct syntax is: ./translate <leftDictFilename> <rightDictFilename> <filenameToTranslate.csv> <outputFilename.csv>\nDon't forget your filetypes!"
    	sys.exit() 

    dictionary = createDict(sys.argv[1], sys.argv[2])
    print dictionary
    inputFile = open(sys.argv[3], "rb")
    outputFile = open(sys.argv[4], "wb")
    reader = inputFile.readlines()
    reader = [x.strip('\n') for x in reader] #strip newline chars
    rownum = 0
    header = ""
    for row in reader:
    	if rownum == 0:
    		header = row
    		outputFile.write("%s\n" % row)
    	else:
    		rowtok = row.split(',', 1) #tokenize each row, delimiter = ","
    		
    		fixedstring = rowtok[1]
		print(fixedstring)
    		if fixedstring in dictionary: fixedstring = dictionary[rowtok[1]]
    		outputFile.write("%d,%s\n" % (rownum,  fixedstring))
        rownum += 1
    inputFile.close()
    outputFile.close()


main()  #this isn't the normal python convention, I'm pretty sure.
