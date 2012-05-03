__author__ = 'QMHA'
import re

####################
# String functions #
####################

# Extract words from a given string
# Returns an array of words
def extractWords(str):
    return re.findall('\w+',str)

# Convert string to lowercase
# Returns the lowered string
def toLower(str):
    return str.lower()

# Convert an array items to lowercase and removes the duplicated items
# Return the lowered case and unique items ARRAY
def arrayToLowerAndUnique(array):
    return set([x.lower() for x in array])

#####################
# File IO Functions #
#####################
def openFile(path, flag = 'r'):
    return open(path, flag)

def readFileLinesToArray(fp):
    return fp.readlines()

def readFileToString(fp):
    arr = ''
    for line in fp:
        arr += line
    return arr