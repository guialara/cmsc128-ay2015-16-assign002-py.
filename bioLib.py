#!/usr/bin/env python

import sys
import re

def getHammingDistance(str1, str2):
			
	dist = 0	
	
	if(len(str1) == 0 and len(str2)==0):
		print "One or Both of the string length is equal to 0"
	elif(len(str1) != len(str2)):
		print "Error! Strings are not equal!"
	else:
		for x in range(0, len(str1)-1):
			if(str1[x] != str2[x]):
				dist+=1
		print dist	
