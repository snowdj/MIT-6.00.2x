import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP > MAXRABBITPOP:
        pRabRepr = 0.0
    else:
        pRabRepr = 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)
    
    newRab = sum( random.random() < pRabRepr for _ in range(CURRENTRABBITPOP))
    if (CURRENTRABBITPOP+newRab) > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    else:
        CURRENTRABBITPOP += newRab
    
    return None
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    foxBirths = 0
    foxDeaths = 0

    # TO DO
    for i in range(CURRENTFOXPOP):
        pFoxEatsRabbit = CURRENTRABBITPOP/float(MAXRABBITPOP)
        huntSuccess = random.random() < pFoxEatsRabbit
        if CURRENTRABBITPOP <= 10:
            huntSuccess = False
        if huntSuccess:
            CURRENTRABBITPOP -= 1
            pFoxBirth = 1/3.0
            if random.random() < pFoxBirth:
                foxBirths += 1
        else:
            if CURRENTFOXPOP <= 10:
                continue
            pFoxDeath = 0.1
            if random.random() < pFoxDeath:
                foxDeaths += 1
    
    CURRENTFOXPOP = CURRENTFOXPOP + foxBirths - foxDeaths
    
    return None
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    rabbit_populations = []
    fox_populations = []
    
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        
    return (rabbit_populations, fox_populations)
    
def makePlots(numSteps):
    rabbit_populations, fox_populations = runSimulation(numSteps)
    pylab.plot(range(numSteps), rabbit_populations, '-b', label='Rabbits')
    pylab.plot(range(numSteps), fox_populations, '-r',
        label='Foxes ')
    pylab.xlabel('Time Step')
    pylab.ylabel('Population')
    pylab.title('Fox and Rabbit Population Vs. Time')
    pylab.legend(loc='upper left')

    coeffRab = pylab.polyfit(range(numSteps), rabbit_populations, 2)
    coeffFox = pylab.polyfit(range(numSteps), fox_populations, 2)
    
    pylab.plot(pylab.polyval(coeffRab, range(numSteps)), '+b')
    pylab.plot(pylab.polyval(coeffFox, range(numSteps)), '+r')
    
    pylab.show()  
    return None