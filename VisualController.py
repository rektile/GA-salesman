import pygame


class VisualController:

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.screen = None
        self.font = None

        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)

        self.circleRad = 10
        self.lineWidth = 3

    def init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Salesman problem")
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def updateCurrentScoreAndEvolution(self,score,ev):
        currentScore = self.font.render("Distance: {}".format(round(score)), False, (0, 0, 0))
        evolutionNumber = self.font.render("ev: {}".format(round(ev)), False, (0, 0, 0))
        self.screen.blit(currentScore, (20, 20))
        self.screen.blit(evolutionNumber, (300, 20))

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def drawBackground(self):
        self.screen.fill(self.white)

    def drawNodes(self,nodes):
        for node in nodes:
            pygame.draw.circle(self.screen, self.black, node, self.circleRad)

    def updateScreen(self):
        pygame.display.flip()

    def drawLinesBetweenNodes(self,nodes):
        for i in range(len(nodes) - 1):
            pygame.draw.line(self.screen, self.black, (nodes[i][0], nodes[i][1]), (nodes[i + 1][0], nodes[i + 1][1]), self.lineWidth)
