import pygame
import random
import sys

pygame.init ()


Width, Height = 800, 400
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Bubble Animation")


BLACK = (0, 0, 0)
BUBBLE_COLORS = [(255, 255, 255), (173, 216, 230), (135, 206, 250), (0, 191, 255)]


class Bubble:
    def __init__(self):
        self.x = 0  
        self.y = Height
        self.radius = random.randint(5, 20)
        self.color = random.choice(BUBBLE_COLORS)
        self.speed_x = random.uniform(0.5, 1.5)
        self.speed_y = random.uniform(1, 2)

    def move(self):
        self.x += self.speed_x
        self.y -= self.speed_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius, 1)


bubbles = []


clock = pygame.time.Clock()


while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    if random.random() < 0.1:
        bubbles.append(Bubble())

    
    for bubble in bubbles[:]:
        bubble.move()
        bubble.draw(screen)

        
        if bubble.y + bubble.radius < 0 or bubble.x - bubble.radius > Width:
            bubbles.remove(bubble)

    pygame.display.flip()
    clock.tick(60)