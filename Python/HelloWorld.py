# print "Hello World!";

######################################1.1#####################
# Check if characters are unique with a string
def uniqueCheck(Character):
	hTable = {}
	for c in Character:
		if c in hTable:
			return False
		else:
			hTable[c] = 1


	return True	




#Check if characters are unique without using a folder structure

def unquieCheck2(Character):
	rs = Character
	count = 0
	for c in Character:
		count += 1
		for rc in Character[count:]:
			if (rc == c):
				return False

	return True			


			
# print uniqueCheck("aabd")
# print unquieCheck2("aabd")
######################################1.2#####################

# Reverse a string 

def reverseString(Char):
	
	if (len(Char) == 2):
		Char = Char[1] + Char[0]
		return Char
	elif (len(Char)== 1):
		return Char
	else:
			
		return Char[len(Char)-1] + reverseString(Char[1:len(Char)-1]) + Char[0]

# print reverseString("a")
# print reverseString("hello")
# print reverseString("accb")
# print reverseString("abc")




#####################################1.3

# Check if a string is a permutation of another string


def checkPermu(String1,String2):
	if (len(String1)!= len(String2)):
		return False

	hTable = {}	
	for i in xrange(0,len(String1)):
		if (String1[i] in hTable):
			hTable[String1[i]] += 1
		else:
			hTable[String1[i]] = 1

		if (String2[i] in hTable):
			hTable[String2[i]] -= 1
		else:
			hTable[String2[i]] = -1	

	for key in hTable:
		if (hTable[key] != 0):
			return False

			
	return True			

# print checkPermu("String2","String2")
# print checkPermu("","aaa")



# #####################################1.4
# REPLACE white space with "%20"

def WSmod(Str):
	last = -1
	first = -1
	newStr = ""


	for c in xrange(0,len(Str)):
		if (Str[c] == " "):
			if (first != -1):
				newStr += "%20"

		else:
			if (first == -1):
				first = 0
			newStr += Str[c]
			last = len(newStr)
	if (first == -1 and last == -1):
		return ""
	elif (first == last):
		return newStr[first]
	else:
		return newStr[:last]				
	
# print WSmod("Hello")

# print WSmod("Hello                     ")

# print WSmod("      Hello           ")

# print WSmod("      Hello joy to the workd             ohyeag          ")


Matrix= [[1,2],[2,3],[1,5]] 



print Matrix[0][0]



