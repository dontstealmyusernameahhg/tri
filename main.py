import pygame
import random
from pygame import mixer

# Initialize Pygame and the mixer
pygame.init()
mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # New color for power-ups
# Load assets
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
jet_image = pygame.image.load("jet.jpg")
jet_image = pygame.transform.scale(jet_image, (50, 50))
explosion_sound = mixer.Sound("explosion.wav")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jet_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5  # Initial speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def speed_up(self):
        self.speed = 10  # Increase speed
        pygame.time.set_timer(pygame.USEREVENT, 5000, loops=1)  # Reset speed after 5 seconds

    def reset_speed(self):
        self.speed = 5  # Reset to initial speed

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Power-up class
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jet Game")

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
powerups = pygame.sprite.Group()  # Group for power-ups
player = Player()
all_sprites.add(player)

# Spawn obstacles
for i in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Spawn power-up
power_up = PowerUp()
all_sprites.add(power_up)
powerups.add(power_up)

# Score
score = 0
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            player.reset_speed()  # Reset speed after power-up duration

    all_sprites.update()

    # Check for obstacle collisions
    obstacle_hits = pygame.sprite.spritecollide(player, obstacles, True)
    if obstacle_hits:
        score -= 50  # Decrease score for hitting obstacles
        explosion_sound.play()
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)
        if score <= 0:
            running = False  # Game over if score is zero or less

    # Check for power-up collisions
    powerup_hits = pygame.sprite.spritecollide(player, powerups, True)
    if powerup_hits:
        score += 50  # Increase score for collecting power-ups
        player.speed_up()  # Activate speed-up
        power_up = PowerUp()
        all_sprites.add(power_up)
        powerups.add(power_up)

    # Drawing
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)

    # Draw score
    draw_text(screen, "Score: " + str(score), 18, SCREEN_WIDTH // 2, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()