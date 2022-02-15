from enum import Enum
from VisualController import VisualController
from GeneticAlgorithm import GeneticAlgorithm
import pygame

class GameState(Enum):
    INIT = 0
    RUNNING = 1

class Program:

    def __init__(self):
        self.VC = VisualController()
        self.currentStage = GameState.INIT
        self.GA = GeneticAlgorithm()
        self.nodes = []

    def run(self):
        self.VC.init()
        self.nodes = []
        while True:
            self.VC.drawBackground()

            self.checkInput()

            if self.currentStage == GameState.RUNNING:
                self.GA.calcFitness()
                self.GA.evolve()
                bestPath = self.GA.bestPath
                ev = self.GA.bestEv
                self.VC.updateCurrentScoreAndEvolution(bestPath.fitness,ev)
                self.VC.drawLinesBetweenNodes(bestPath.nodePath)
            else:
                self.VC.updatePointsText(len(self.nodes))

            self.VC.drawNodes(self.nodes)
            self.VC.updateScreen()


    def checkInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.currentStage == GameState.INIT:
                self.addNode()

            elif event.type == pygame.KEYDOWN:
                #run GA
                if event.key == pygame.K_RETURN and self.currentStage == GameState.INIT:
                    self.startGA()

                elif event.key == pygame.K_BACKSPACE and self.nodes and self.currentStage == GameState.INIT:
                    self.removeLastNode()

                elif event.key == pygame.K_r:
                    self.reset()

    def removeLastNode(self):
        self.nodes.pop()

    def addNode(self):
        node = self.VC.getMousePos()
        self.nodes.append(node)

    def startGA(self):
        if len(self.nodes) >= 3:
            self.currentStage = GameState.RUNNING
            self.GA.initNodeArray(self.nodes)
        else:
            print("You need more than 3 points")

    def reset(self):
        self.GA.reset()
        self.currentStage = GameState.INIT
        self.nodes = []


program = Program()

program.run()