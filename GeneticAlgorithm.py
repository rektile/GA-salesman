import random

from Path import Path
from enum import Enum
from random import choice

class SelectionMethod(Enum):
    ROULETTE = 0


class GeneticAlgorithm:
    def __init__(self):
        self.nodeArray = None

        self.populationAmount = 100
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

        if self.bestPath or path.fitness < self.bestPath.fitness:
            self.bestPath = path
            self.bestEv = self.evolutionNumber

        if self.wortPath or path.fitness > self.wortPath.fitness:
            self.wortPath = path


    def evolve(self,method=SelectionMethod.ROULETTE):

        self.matingPool = []

        if method == SelectionMethod.ROULETTE:
            self.evolveRoulette()

        self.mate()

    def mate(self):
        self.populationArray = []

        for i in range(self.populationAmount):
            parent1 = random.choice(self.matingPool)
            parent2 = random.choice(self.matingPool)
            child = parent1.crossover(parent2)
            child.mutate()
            self.populationArray.append(child)

        self.evolutionNumber += 1


    def evolveRoulette(self):

        for path in self.populationArray:

            #reverse minmax -> lower fitness = better
            procent = 100 - round((path.fitness - self.bestPath.fitness) / (self.wortPath.fitness - self.bestPath.fitness) * 100)

            for i in range(procent):
                self.matingPool.append(path)


    def calcFitness(self):
        self.averageFitness = 0

        for path in self.populationArray:

            path.calcFitness()

            self.averageFitness += path.fitness

            self.checkForBestAndWorst(path)

        self.averageFitness /= self.populationAmount
