#!/usr/bin/env python

#Author: Guia Carmella B. Lara
#Section: CMSC 128 AB-7L
#Program Description: Bioinformatics Library
#Due on: March 12, 2016

def getHammingDistance(str1, str2):
	#returns the number of different characters from same length of string		
	dist = 0	
	
	if(len(str1) == 0 and len(str2)==0):
		print "Both of the string length is 0"
		return -1 #returns -1 if error
	elif(len(str1) != len(str2)):
		print "Error! Strings are not equal!"
		return -1 #returns -1 if error
	else:
		for x in range(0, len(str1)):#checks each character of str1 and str2
			if(str1[x] != str2[x]):#if not equal characters, add 1 to dit
				dist+=1
		return dist #returns the hamming distance of the two strings

def countSubstrPattern(orig, pattern):#counting the pattern in the orig string
	
	numPattern = 0;
	tORf = 1;	
	
	if(len(pattern)==0):#if there is not pattern given
		print "There is no pattern indicated."
		return -1#returns -1 if there is no pattern	
	elif(len(orig) < len(pattern)):#if pattern length is bigger than the length of the orig string 
		return numPattern#returns 0 because no pattern found	
	else:
		for x in range(0, len(orig)):#loops through each char of the orig string
			if(x+len(pattern)-1 != len(orig)):#countermeasure for array index out of bounds error
				if(orig[x]==pattern[0]):#checks the first pattern char to the current orig char
					for y in range(0, len(pattern)):#checks each char in pattern to the orig string 
						if(orig[x+y] != pattern[y]):#pattern not exhausted and not eaqual to char of orig
							tORf = 0#make tORf 0					
					if(tORf != 0):#after pattern loop, check tORf, if 1, add 1 to numPattern
						numPattern += 1
					else:#else, change tORf to 1
						tORf = 1
		return numPattern
