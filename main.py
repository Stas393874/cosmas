import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FPV Drone Game")

drone_img = pygame.image.load('drone.png').convert_alpha()
tank_imgs = [
    pygame.image.load('tank1.png').convert_alpha(),
    pygame.image.load('tank2.png').convert_alpha(),
    pygame.image.load('tank3.png').convert_alpha(),
    pygame.image.load('tank4.png').convert_alpha(),
    pygame.image.load('tank5.png').convert_alpha()
]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = drone_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(tank_imgs)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4)

all_sprites = pygame.sprite.Group()
tanks = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    tank = Tank()
    all_sprites.add(tank)
    tanks.add(tank)

score = 0
level = 1

clock = pygame.time.Clock()
running = True
while running:

    clock.tick(FPS)

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

hits = pygame.sprite.spritecollide(player, tanks, True)
for hit in hits:
    tank = Tank()
    all_sprites.add(tank)
    tanks.add(tank)
    score += 1
    if score % 5 == 0:
        level += 1
        for tank in tanks:
            tank.speed_y += 1

    screen.fill(BLACK)
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    level_text = font.render(f'Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip()

pygame.quit()