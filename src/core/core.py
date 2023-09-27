import pygame
import circleCollider
import collisionChecker



class Core:

    isRunning = True
    screen = None
    clock = None
    screenWidth = None
    screenHeight = None
    dt = 0 

    c1 = circleCollider.CircleCollider()
    c2 = circleCollider.CircleCollider()
    collisionChecker = collisionChecker.CollisionChecker()

    def __init__(self, width, height) -> None:
       self.screenWidth = width
       self.screenHeight = height
       self.init()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight)) 
        self.clock = pygame.time.Clock()
        self.c1.x = 10
        self.c1.y = 10
        self.c1.radius = 25
        self.c2.x = 100
        self.c2.y = 100
        self.c2.radius = 25


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
                pygame.quit()

    def input(self):
        speed = 100
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.c1.x -= speed * self.dt
        if keys[pygame.K_d]:
            self.c1.x += speed * self.dt
        if keys[pygame.K_w]:
            self.c1.y -= speed * self.dt
        if keys[pygame.K_s]:
            self.c1.y += speed * self.dt

    def update(self):
        if self.collisionChecker.circleCircleCheckCollsion(self.c1,self.c2):
            self.collisionChecker.circleCircleResolve(self.c1,self.c2)

    def render(self):
        pygame.draw.circle(self.screen,(255,0,0),(self.c1.x,self.c1.y),self.c1.radius)
        pygame.draw.circle(self.screen,(255,255,0),(self.c2.x,self.c2.y),self.c2.radius)

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
