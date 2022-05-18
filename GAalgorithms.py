from enum import Enum

class SelectionMethod(Enum):
    ROULETTE = 0
    TOURNAMENT = 1

class MutationMethod(Enum):
    INVERSION = 0
    SWAP_POSITIONS = 1
    SCRAMBLE = 2

class CrossoverMethod(Enum):
    ORDERED_CROSSOVER = 0
    CYCLE_CROSSOVER = 1