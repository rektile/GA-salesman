from Path import Path

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





    def calcFitness(self):
        self.averageFitness = 0

        for path in self.populationArray:

            path.calcFitness()

            self.averageFitness += path.fitness

            self.checkForBestAndWorst(path)

        self.averageFitness /= self.populationAmount
