from random import sample
from math import dist

class Path:
    def __init__(self):
        self.fitness = 0
        self.nodePath = None

        self.mutationRate = 20
        self.crossoverRate = 80

    def setPath(self,path):
        self.nodePath = path

    def makePathRandomFromNodes(self, nodes):
        self.nodePath = sample(nodes, len(nodes))

    def calcFitness(self):
        self.fitness = 0
        for i in range(len(self.nodePath) - 1):
            currentNode = self.nodePath[i]
            nextNode = self.nodePath[i + 1]

            distance = dist(currentNode, nextNode)
            self.fitness += distance




