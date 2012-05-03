import nbc
import utils
import helpers

def run():
    nbc.classifyNaiveBayesText()
    return 0

def run2():
    test()
    print '======= Email Ranking Program ======= \n'
    print 'What do you want to do? \n'
    print '1. Learn the text \n'
    print '2. Classify a document \n'
    print '3. Exit \n'
    print '===================================== \n'
    choose = input('You choose: ')

    if (choose == 1):
        nbc.learnNaiveBayesText()
    if (choose == 2):
        nbc.classifyNaiveBayesText()
    if (choose == 3):
        exit()
    return 0

def test():
    fp = utils.openFile('test.txt')
    str = utils.readFileToString(fp)
    n = utils.extractWords(str)
    array = ['Hello', 'hello', 'heLLO', 'Minh']
    # print utils.arrayToLowerAndUnique(array)
    # print n
    # print helpers.getExamples()[1]
    # print helpers.getDocsByClass(2)
    # helpers.saveTerms("hello world", 1, 4.0)
    # print len(helpers.getVocabulary())
    return

# Run
run2()