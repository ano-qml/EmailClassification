__author__ = 'QMHA'

import sqlHelper
import utils
import MySQLdb

############################
# Helpers function         #
# for this Naive Bayesian  #
# program                  #
############################

# update or insert new term
def saveTerms(term, v, score):
    entity = sqlHelper.sql_queryRows('terms',"WHERE `term` LIKE '%s' AND `v_j` = '%d'" %(term, v))
    if (len(entity) == 0):
        # insert)
        conn = sqlHelper.sqlConnect()
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO terms(term, v_j, score) VALUES(%s, %s, %s) """, (term, str(v), str(score)))
            conn.commit()
        except :
            conn.rollback()
        conn.close()
        cursor.close()
    else:
        conn = sqlHelper.sqlConnect()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """UPDATE terms set score = %s WHERE term LIKE %s AND v_j = %s """,
                (str(score), term, str(v))
            )
            conn.commit()
        except :
            conn.rollback()
        conn.close()
        cursor.close()
        # update
    return

# read all training data to array
def readTrainingDataToArray():
    return sqlHelper.sql_queryRows('training_data','')

# read all document in training_data
# returns the array of mysql data
def readDocsByClass(v):
    return sqlHelper.sql_queryRows('training_data','WHERE v = ' + v)

# get examples count
def getExamplesCount():
    return len(readTrainingDataToArray())

# get the vocabulary set of All documents in all values
# return an array of all terms in training_data
def getVocabulary():
    a = []
    items = readTrainingDataToArray()
    for item in items:
        word_array = utils.extractWords(item[5] + ' ' + item[6])
        a.extend(utils.arrayToLowerAndUnique(word_array))
    return a

# get the documents by class
# return array of documents based on mysql structure
def getDocsByClass(v):
    return sqlHelper.sql_queryRows('training_data','WHERE v = %s' %(v))

# get the documents terms by class
# return an array of all terms of all documents in class V
def getDocsTermsByClass(items):
    a = []
    # items = readDocsByClass(v)
    for item in items:
        word_array = utils.extractWords(item[5] + ' ' + item[6])
        a.extend(utils.arrayToLowerAndUnique(word_array))
    return a

# get all Values set of V
def getV():
    return [0,1,2,3]

# get the test file
def getTestFileToArray():
    str = ''
    fp = utils.openFile('test.txt')
    for line in fp:
        str += line
    str = utils.toLower(str)
    return utils.extractWords(str)

# get term score
def getTermScore(term, v):
    result = sqlHelper.sql_queryRows('terms',"WHERE term LIKE '%s' AND v_j='%s'" % (term,str(v)))
    return result[0][3]