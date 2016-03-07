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

def isValidString(str1, alpha):#checks if string is valid  given an alphabet
	
	tORf = 0
	trueCount = 0;

	if(len(str1) == 0 or len(alpha) == 0):#checks if both string are given
		print "Alphabet or String is not indicated."
		return False
	else:
		for x in range(0, len(str1)):#checks each char in str1
			for y in range(0, len(alpha)):#checks char of alpha
				if(str1[x] == alpha[y]):# if the char of str1 matched in char of alpha
					tORf = 1#make tORf 1
			if(tORf == 0):#if tORf is 0, return false - str1 is not valid
				return False
			else:#check the next char
				trueCount +=1
				tORf = 0
		return True#retrun true if the checking  finished without a hitch

def getSkew(str1, jump):#gets the num of G on the given index
	
	skewNum = 0
	if(len(str1)==0):#if no str1 is given
		print "No string indicated."
		return None
	elif(jump == 0):#if no index num is given
		print "No integer indicated."
		return None
	elif(jump > len(str1)):#if index given is out of bounds
		print "Cannot compute. Integer is greater than length of string."
		return None
	else:
		getG = countSubstrPattern(str1[0:jump], "G")#gets the number of G in the given string
		getC = countSubstrPattern(str1[0:jump], "C")#gets the number of C in the given string
		
		skewNum = getG - getC#computes for the skew for the given index
		
		return skewNum#returns the skew on the given number

def getMaxSkewN(str1, jump):#computes each skew starting from 1 to the given jump then return maxSkew

	maxSkew = 0;
	
	if(len(str1)==0):#error handling
		print "No string indicated."
		return None
	elif(jump == 0):#error handling
		print "No integer indicated."
		return None
	elif(jump > len(str1)):#error handling
		print "Cannot compute. Integer is greater than length of string."
		return None
	else:
		for x in range(1, jump+1):#checks each index for their skew
			if(maxSkew < getSkew(str1[0:x], x)):#checks if maxSkew is less than the skew of str1[x]
				maxSkew = getSkew(str1[0:x], x)#if less than, assign new maxSkew
		return maxSkew

def getMinSkewN(str1, jump):#computes each skew starting from 1 to the given jump then return maxSkew
	
	minSkew = float("inf")#assigns infinite number to minSkew to make sure it is greater than skew of others 

	if(len(str1)==0):#error handling
		print "No string indicated."
		return None
	elif(jump == 0):#error handling
		print "No integer indicated."
		return None
	elif(jump > len(str1)):#error handling
		print "Cannot compute. Integer is greater than length of string."
		return None
	else:
		for x in range(1, jump+1):#checks each index for their skew
			if(minSkew > getSkew(str1[0:x], x)):#checks if minSkew is greater than the skew of str1[x]
				minSkew = getSkew(str1[0:x], x)#if greater than, assign new minSkew
		return minSkew
