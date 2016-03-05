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
