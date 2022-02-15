from Path import Path
from random import choice
from GAalgorithms import *

class GeneticAlgorithm:
    def __init__(self):
        ###Params###############################################
        self.selectionMethod = SelectionMethod.TOURNAMENT
        self.mutationMethod = MutationMethod.INVERSION
        self.crossoverMethod = CrossoverMethod.CYCLE_CROSSOVER

        self.mutationRate = 15
        self.crossoverRate = 85

        self.populationAmount = 100
        self.selectionSize = round(self.populationAmount / 10)
        #######################################################

        self.populationArray = None

        self.evolutionNumber = 0
        self.averageFitness = 0

        self.wortPath = None
        self.bestPath = None
        self.bestEv = 0
        self.newBestPath = False

        self.matingPool = []

    def reset(self):
        self.nodeArray = None

        self.populationArray = None

        self.evolutionNumber = 0
        self.averageFitness = 0

        self.wortPath = None
        self.bestPath = None
        self.bestEv = 0

        self.newBestPath = False

        self.matingPool = []


    def initNodeArray(self,nodes):
        self.nodeArray = nodes
        paths = []
        for i in range(self.populationAmount):
            newPath = Path()
            newPath.makePathRandomFromNodes(nodes)
            paths.append(newPath)

        self.populationArray = paths

    def checkForBestAndWorst(self,path):

        if self.bestPath:
            if path.fitness < self.bestPath.fitness:
                self.bestPath = path
                self.bestEv = self.evolutionNumber
        else:
            self.bestPath = path
            self.bestEv = self.evolutionNumber

        if self.wortPath:
            if path.fitness > self.wortPath.fitness:
                self.wortPath = path
        else:
            self.wortPath = path


    def evolve(self):

        self.matingPool = []

        if self.selectionMethod == SelectionMethod.ROULETTE:
            self.evolveRoulette()

        elif self.selectionMethod == SelectionMethod.TOURNAMENT:
            self.evolveTournament()

        self.breed()

    def breed(self):
        self.populationArray = []

        for i in range(self.populationAmount):
            parent1 = choice(self.matingPool)
            parent2 = choice(self.matingPool)
            child = parent1.crossover(parent2, self.crossoverMethod, self.crossoverRate)
            child.mutate(self.mutationMethod, self.mutationRate)
            self.populationArray.append(child)

        self.evolutionNumber += 1

    def evolveTournament(self):
        for i in range(self.populationAmount):
            selection = []
            for j in range(self.selectionSize):

                while True:
                    randomChoice = choice(self.populationArray)
                    if randomChoice not in selection:
                        selection.append(randomChoice)
                        break

            selection = sorted(selection, key=lambda path: path.fitness)
            self.matingPool.append(selection[0])



    def evolveRoulette(self):

        for path in self.populationArray:

            #reverse minmax -> lower fitness = better
            percentage = 100 - round((path.fitness - self.bestPath.fitness) / (self.wortPath.fitness - self.bestPath.fitness) * 100)

            for i in range(percentage):
                self.matingPool.append(path)


    def calcFitness(self):
        self.averageFitness = 0

        for path in self.populationArray:

            path.calcFitness()

            self.averageFitness += path.fitness

            self.checkForBestAndWorst(path)

        self.averageFitness /= self.populationAmount

