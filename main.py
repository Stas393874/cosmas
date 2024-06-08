import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_wigth, screen_height))
pygame.display.set_caption("Космическая Эра")

while = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRENN = (0, 255, 0)
class Resource:
    def __init__(self, name):
        self.name = name
        self.quantity = 0

class HumanSudtype:
    def __init__(self, name, efficiency):
        self.name = name
        self.efficiency = efficiency
        self.stage = 1
    def evolve(self):
        if self.stage < 4:
            self.stage += 1
            self.efficiency *= 1.5
        else:
            print("This subtype has reached the maximum evolutionry stage.")

class Planet:
    def __init__(self, name):
        self.name = name
        self.resoursec = {f"Resource {i}": Resource(f"Resource {i}") for i in range(1, 4)}
        self.human_subtypes = {
            "miners": HumanSudtype("Miners", 1.0),
            "builders": HumanSudtype("Builders", 1.0),
            "soldiers": HumanSudtype("Soldiers")
        }