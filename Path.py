from random import sample, randint
from math import dist
from enum import Enum


class MutationMethod(Enum):
    INVERSION = 0
    SWAP_POSITIONS = 1


class CrossoverMethod(Enum):
    ORDERED_CROSSOVER = 0
    CYCLE_CROSSOVER = 1


class Path:
    def __init__(self):
        self.fitness = 0
        self.nodePath = None

        self.mutationRate = 15
        self.crossoverRate = 70

    def setPath(self, path):
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

    def mutate(self, method=MutationMethod.INVERSION):

        if method == MutationMethod.INVERSION:
            self.mutateInversion()
        elif method == MutationMethod.SWAP_POSITIONS:
            self.mutateSwap()

    def mutateSwap(self):
        while True:
            r1 = randint(0,len(self.nodePath) - 1)
            r2 = randint(0,len(self.nodePath) - 1)
            if r1 != r2:
                temp = self.nodePath[r1]
                self.nodePath[r1] = self.nodePath[r2]
                self.nodePath[r2] = temp
                break


    def mutateInversion(self):
        randomNum = randint(0, 100)

        if randomNum < self.mutationRate:
            a = 0
            b = 0

            while a == b:
                a = randint(0, len(self.nodePath) - 1)
                b = randint(0, len(self.nodePath) - 1)

            if a < b:
                start = self.nodePath[:a]
                middle = list(reversed(self.nodePath[a:b]))
                end = self.nodePath[b:]
            else:
                start = self.nodePath[:b]
                middle = list(reversed(self.nodePath[b:a]))
                end = self.nodePath[a:]

            self.nodePath = start + middle + end

    def crossover(self, partner, method=CrossoverMethod.CYCLE_CROSSOVER):

        if method == CrossoverMethod.ORDERED_CROSSOVER:
            return self.orderedCrossover(partner)
        elif method == CrossoverMethod.CYCLE_CROSSOVER:
            return self.cycleCrossover(partner)

    def cycleCrossover(self,partner):
        y1 = [-1] * len(self.nodePath)
        y2 = [-1] * len(partner.nodePath)

        y1[0] = self.nodePath[0]
        y2[0] = partner.nodePath[0]
        i = 0

        while partner.nodePath[i] not in y1:
            j = self.nodePath.index(partner.nodePath[i])
            y1[j] = self.nodePath[j]
            y2[j] = partner.nodePath[j]
            i = j

        for i in range(len(self.nodePath)):
            if y1[i] == -1:
                y1[i] = self.nodePath[i]
                y2[i] = partner.nodePath[i]

        newPath = Path()
        newPath.setPath(y1)

        return newPath

    def orderedCrossover(self, partner):
        child = []

        sectionStart = randint(0, len(self.nodePath) - 1)
        sectionEnd = randint(0, len(self.nodePath) - 1)
        sectionIndex = range(sectionStart,sectionEnd)
        section = self.nodePath[sectionStart:sectionEnd]

        childIndex = 0
        partnerIndex = 0
        while childIndex < len(self.nodePath):
            if childIndex in sectionIndex:
                for num in section:
                    child.append(num)
                    childIndex += 1
            else:
                curNum = partner.nodePath[partnerIndex]

                if curNum not in section:
                    child.append(curNum)
                    childIndex += 1

                partnerIndex += 1


        newPath = Path()
        newPath.setPath(child)

        return newPath