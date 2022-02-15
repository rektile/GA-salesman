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
                bestScore = self.GA.bestPath.fitness
                ev = self.GA.bestEv
                self.VC.updateCurrentScoreAndEvolution(bestScore,ev)
            else:
                self.VC.updatePointsText(len(self.nodes))

            self.VC.drawNodes(self.nodes)
            self.VC.updateScreen()


    def checkInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.currentStage == GameState.INIT:
                node = self.VC.getMousePos()
                self.nodes.append(node)

            elif event.type == pygame.KEYDOWN:
                #run GA
                if event.key == pygame.K_RETURN and self.currentStage == GameState.INIT:
                    self.currentStage = GameState.RUNNING
                    if len(self.nodes) >= 3:
                        self.GA.initNodeArray(self.nodes)

                elif event.key == pygame.K_BACKSPACE and self.nodes and self.currentStage == GameState.INIT:
                    self.nodes.pop()

program = Program()

program.run()