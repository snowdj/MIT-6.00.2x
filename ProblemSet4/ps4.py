# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *


# Helper functions

import math
random.seed(12345)

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
    
    
    for i in range(len(StepsBeforeDrug)):
        virusesAtTrial = [0] * numTrials
  
        for j in range(numTrials):
            
            virusesAtTime = [0] * timesteps[i]
        
            viruses = []

            # Create ResistantVirus intances
            for k in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        
            # Create the patient
            patient = TreatedPatient(viruses, maxPop)
        
            # run the timesteps
            for t in range(timesteps[i]):
                if t == StepsBeforeDrug[i]:
                    patient.addPrescription("guttagonol")
                virusesAtTime[t] = patient.update()
            
            virusesAtTrial[j] = virusesAtTime[-1]
            
        numBins = math.ceil( numTrials**0.5 )
        
        percentCured = sum(x<=50 for x in virusesAtTrial)/float(sum(x>=0 for x in virusesAtTrial))*100
        print('Percent cured for delay = ' + str(StepsBeforeDrug[i]) + ': %.2f' % percentCured)
            
        pylab.subplot(len(StepsBeforeDrug)/2, 2, i+1)
        pylab.hist(virusesAtTrial, bins = numBins)
        pylab.xlabel('Total Virus Population, Delay = ' + str(StepsBeforeDrug[i]))
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
    
    # Simulation parameters
    maxPop = 1000
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    
    StepsBetweenDrugs = [300, 150, 75, 0]
    InitialStepsWithoutDrug = 150
    StepsWithSecondDrug = 150   
    timesteps = [x + StepsWithSecondDrug + InitialStepsWithoutDrug for x in StepsBetweenDrugs]
    
    for i in range(len(StepsBetweenDrugs)):
        virusesAtTrial = [0] * numTrials
  
        for j in range(numTrials):
            
            virusesAtTime = [0] * timesteps[i]
        
            viruses = []

            # Create ResistantVirus intances
            for k in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        
            # Create the patient
            patient = TreatedPatient(viruses, maxPop)
        
            # run the timesteps
            for t in range(timesteps[i]):
                if t == InitialStepsWithoutDrug:
                    patient.addPrescription('guttagonol')
                if t == InitialStepsWithoutDrug + StepsBetweenDrugs[i]:
                    patient.addPrescription('grimpex')
                virusesAtTime[t] = patient.update()
            
            virusesAtTrial[j] = virusesAtTime[-1]
            
        numBins = math.ceil( numTrials**0.5 )
        
        percentCured = sum(x<=50 for x in virusesAtTrial)/float(sum(x>=0 for x in virusesAtTrial))*100
        varianceViruses = numpy.var(virusesAtTrial)
        print('Percent cured for time between drugs = ' + \
            str(StepsBetweenDrugs[i]) + ': %.2f' % percentCured)
        print('Simulation variance for time between drugs = ' + \
            str(StepsBetweenDrugs[i]) + ': %.2f' % varianceViruses)
            
        pylab.subplot(len(StepsBetweenDrugs)/2, 2, i+1)
        pylab.hist(virusesAtTrial, bins = numBins)
        pylab.xlabel('Total Virus Population, Time Between Drugs = ' + str(StepsBetweenDrugs[i]))
        pylab.ylabel('Number of Trials')
 
    pylab.show()    
    
    return None