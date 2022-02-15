class GeneticAlgorithm:
    def __init__(self):
        self.nodeArray = None

        self.population = 100

        self.evolutionNumber = 0
        self.averageFitness = 0

        self.bestFitness = None
        self.wortFitness = 0
        self.bestPath = None
        self.bestEv = 0

        self.newBestPath = False

