import random

def sampleQuizzes():
    # Monte Carlo simulation of grades
    yes = 0.0
    numTrials = 10000
    
    for i in range(numTrials):
        midTerm1 = random.randint(50, 80)
        midTerm2 = random.randint(60, 90)
        Final = random.randint(55, 95)
        Grade = 0.25*midTerm1 + 0.25*midTerm2 + 0.50*Final
        if Grade >= 70 and Grade <= 75:
            yes += 1
    
    return yes/numTrials