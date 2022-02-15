from enum import Enum
from VisualController import VisualController

class GameState(Enum):
    INIT = 0
    RUNNING = 1

class Program:

    def __init__(self):
        self.VC = VisualController
        self.currentStage = GameState.INIT