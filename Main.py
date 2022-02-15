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

    def run(self):
        self.VC.init()
        nodes = []
        while True:
            self.VC.drawBackground()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    node = self.VC.getMousePos()
                    nodes.append(node)

            self.VC.drawNodes(nodes)
            self.VC.updateScreen()



program = Program()

program.run()