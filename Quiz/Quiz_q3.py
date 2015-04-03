def probTest(limit):
    ''' compute the maximum number of consecutive die rolls before rolling 1 with
    probability less than limit
    '''
    numRolls = 1
    
    def calcProb(numRolls):
        return float(1.0/5.0*(5.0/6.0)**numRolls)
        
    while True:
        prob = calcProb(numRolls)
        if prob > limit:
            numRolls +=1
            continue
        return numRolls