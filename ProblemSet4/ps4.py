# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *


# Helper functions

def createViruses(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for j in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    return viruses
    
import math

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # Simulation parameters
    maxPop = 1000
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    
    StepsBeforeDrug = [300, 150, 75, 0]
    StepsWithDrug = 150   
    timesteps = [x + StepsWithDrug for x in StepsBeforeDrug]
    virusesList = []
    guttagonolResVirusesList = []
    
    
    for i in range(len(StepsBeforeDrug)):
        # Initialize the running total and average lists to all zeros
        virusesAtTime = []
        guttagonolResistantViruses = []
        virusesAtTime = [0] * timesteps[i]
        guttagonolResistantViruses = [0] * timesteps[i]
  
        for j in range(numTrials):
        
            viruses = []

            # Create ResistantVirus intances
            viruses = createViruses(numViruses, maxBirthProb,
                clearProb, resistances, mutProb)
        
            # Create the patient
            patient = TreatedPatient(viruses, maxPop)
        
            # run the timesteps
            for t in range(timesteps[i]):
                if t == StepsBeforeDrug[i]:
                    patient.addPrescription("guttagonol")
                virusesAtTime[t] += patient.update()
                guttagonolResistantViruses[t] += patient.getResistPop(['guttagonol'])
         
        virusesList.append(virusesAtTime[:])
        guttagonolResVirusesList.append(guttagonolResistantViruses[:])
            
        numBins = math.ceil( numTrials**0.5 )
            
        pylab.subplot(len(StepsBeforeDrug), 2, 2*i+1)
        pylab.hist(virusesList[i], bins = numBins)
        pylab.xlabel('Total Virus Population')
        pylab.ylabel('Number of Trials')
            
        pylab.subplot(len(StepsBeforeDrug), 2, 2*i+2)
        pylab.hist(guttagonolResVirusesList[i], bins = numBins)
        pylab.xlabel('Guttagonol Resistant Virus Population')
        pylab.ylabel('Number of Trials')
 
    pylab.show()    
    
    return None





#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
