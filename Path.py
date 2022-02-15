from random import shuffle
from math import dist

class Path:
    def __init__(self):
        self.fitness = 0
        self.nodePath = None

    def setPath(self,path):
        self.nodePath = path

    def makePathRandomFromNodes(self,nodes):
        self.nodePath = shuffle(nodes)

    def calcFitness(self):
        self.fitness = 0
        for i in range(len(self.nodePath) - 1):
            currentNode = self.nodePath[i]
            nextNode = self.nodePath[i + 1]

            distance = dist(currentNode, nextNode)
            self.fitness += distance




