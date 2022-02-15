from Path import Path

class GeneticAlgorithm:
    def __init__(self):
        self.nodeArray = None

        self.populationAmount = 100
        self.populationArray = None

        self.evolutionNumber = 0
        self.averageFitness = 0

        self.bestFitness = None
        self.wortFitness = 0
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
