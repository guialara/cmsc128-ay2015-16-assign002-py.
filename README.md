CMSC 128 Assignment AB-7L 
-------------
## Bioinformatics Library written in Python
> This Library contains specific functions that will be explained below
> To run the library, run python in the terminal and import bioLib

### To Run the Library:
```
//Type this on your terminal when python is open
>>> import bioLib
```

#### 1. def getHammingDistance(String1, String2)
> Given two strings str1 and str2 of same length (length must never be 0 or negative!), the Hamming Distance of those two strings are the number of inversions per character need to transform str1 to str2 or vise-versa. Simply put, the Hamming Distance of two strings is the number of characters that differ in ith position from position 1 to strlen(str1).

##### To Run this function:
```
>>>bioLib.getHammingString(String1,String2)
```
####2. def countSubstrPattern(String original, String pattern)
> Given a string original and pattern, we will count the number of occurrence of pattern in original.

##### To Run this function:
```
>>>bioLib.countSubstrPattern(String1,String2)
```
####3. def isValidString(String str, String alphabet)
> Given an alphabet string where all letters are assumed to be unique, this function returns true if the string str is a valid string based on the letters of alphabet.

##### To Run this function:
```
>>>bioLib.isValidString(String1,alphabet)
```

####4. def getSkew(String str, int index)
> Given a genome str of some length q (where q>0), it returns the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations.

##### To Run this function:
```
>>>bioLib.getSkew(String,index)
```
####5. def getMaxSkewN(String str, int index)
> Given a genome str of some length q (where q>0), it returns the maximum value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations.

##### To Run this function:
```
>>>bioLib.getMaxSkewN(String,index)
```
####6. def getMinSkewN(String str, int index)
> Given a genome str of some length q (where q>0), it returns the minimum value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations.

##### To Run this function:
```
>>>bioLib.getMinSkewN(String,index)
```

