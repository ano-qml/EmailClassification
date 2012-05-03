__author__ = 'QMHA'

import helpers
import utils

def learnNaiveBayesText():
    print '... Learning Text ... \n'

    vocabulary = helpers.getVocabulary()
    vocabulary_count = len(vocabulary);
    examples = helpers.getExamplesCount()

    counter = 0

    # Start learning
    for v in helpers.getV():
        docs = helpers.getDocsByClass(v)
        docs_count = len(docs)
        docs_terms = helpers.getDocsTermsByClass(docs)
        # probability of class v
        p_v = (float)(docs_count) / (float)(examples)
        # total of distinct word in docs
        n = len(docs_terms)

        # foreach word wk in Vocabulary
        for w in vocabulary:
            nk = docs_terms.count(w)
            p_w_v = (float)(nk + 1) / (float)(n + vocabulary_count)
            print '#' + str(counter) + ':' + str(p_w_v)
            counter += 1
            # save term
            helpers.saveTerms(w,v,p_w_v)
    # End learning

    print '!!!! Finished !!!!\n'
    return

def classifyNaiveBayesText():
    print '... Classifying document ... \n'

    # start classification
    vocabulary = helpers.getVocabulary()
    words = helpers.getTestFileToArray()
    positions = set(vocabulary) & set(words)

    results = []

    for v in helpers.getV():
        vnb = 1
        for i in positions:
            vnb *= helpers.getTermScore(i,v)
        results.append(vnb)
        print str(v) + ':' + str(vnb)

    print 'The result is : ' + str(max(results))
    # end classification

    print '!!!! Finished !!!!\n'
    print '===== Result =====\n'
    print '==================\n'
    return