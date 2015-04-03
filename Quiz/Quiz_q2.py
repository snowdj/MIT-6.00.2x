import random
import pylab

def plotQuizzes():
    # Use the scores generated from supplied generateScores(numTrials)
    numTrials = 10000
    finalScores = generateScores(numTrials)
    pylab.hist(finalScores, bins = 7)
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.title('Distribution of Scores')
    pylab.show()