import pygame



class Core:

    isRunning = True
    screen = None
    clock = None
    screenWidth = None
    screenHeight = None
    dt = 0 

    def __init__(self, width, height) -> None:
       self.screenWidth = width
       self.screenHeight = height
       self.init()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight)) 
        self.clock = pygame.time.Clock()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
                pygame.quit()

    def input(self):
        keys = pygame.key.get_pressed()

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while self.isRunning == True:
            self.event()
            self.input()
            self.update()
            self.screen.fill("pink")
            self.render()
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()
