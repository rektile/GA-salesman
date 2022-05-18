from enum import Enum
from VisualController import VisualController
from GeneticAlgorithm import GeneticAlgorithm
from GAalgorithms import *
import pygame

class GameState(Enum):
    INIT = 0
    RUNNING = 1
    FINISHED = 2

class Program:

    def __init__(self):

        # Initialize the Genetic Algorithm
        self.GA = GeneticAlgorithm(
            SelectionMethod.TOURNAMENT,
            MutationMethod.INVERSION,
            CrossoverMethod.CYCLE_CROSSOVER
        )
        
        
        self.VC = VisualController(1200, 800)
        self.currentStage = GameState.INIT
        self.nodes = []

        self.maxGenerationsNoImprovement = 10
        self.prevBest = 0
        self.iterationCount = 0
        self.selfPath = None

    def run(self):
        self.VC.init()
        while True:
            self.VC.drawBackground()

            self.checkInput()

            if self.currentStage == GameState.INIT:
                # Draw the amount of points
                self.VC.updatePointsText(len(self.nodes))

            elif self.currentStage == GameState.RUNNING:
                self.bestPath, ev = self.GA.run();

                if self.prevBest == self.bestPath.fitness:
                    self.iterationCount += 1
                    
                    # Check if we haven't improved for a while to stop the GA
                    if self.iterationCount == self.maxGenerationsNoImprovement:
                        self.currentStage = GameState.FINISHED   
                else:
                    self.prevBest = self.bestPath.fitness
                    self.iterationCount = 0
                    
                    # Draw the current best path
                    self.VC.updateCurrentScoreAndEvolution(self.bestPath.fitness, ev)
                    self.VC.drawLinesBetweenNodes(self.bestPath.nodePath)

            elif self.currentStage == GameState.FINISHED:
                # Draw the stats of the best found path
                self.VC.updateCurrentScoreAndEvolution(self.bestPath.fitness, ev)
                self.VC.drawLinesBetweenNodes(self.bestPath.nodePath)

            # Draw the nodes and update the screen
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

        self.iterationCount = 0
        self.prevBest = 0


program = Program()

program.run()