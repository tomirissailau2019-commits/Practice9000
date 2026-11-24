import pygame
import math
import datetime

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
SKIN = (255, 210, 160)

center_x = WIDTH // 2
center_y = HEIGHT // 2

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (center_x - 115, center_y - 145), 90)
    pygame.draw.circle(screen, BLACK, (center_x + 115, center_y - 145), 90)

    pygame.draw.circle(screen, BLACK, (center_x, center_y), 180)

    pygame.draw.circle(screen, SKIN, (center_x, center_y + 35), 135)

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    second_angle = math.radians(seconds * 6 - 90)
    second_x = center_x + 145 * math.cos(second_angle)
    second_y = center_y + 145 * math.sin(second_angle)

    minute_angle = math.radians(minutes * 6 - 90)
    minute_x = center_x + 110 * math.cos(minute_angle)
    minute_y = center_y + 110 * math.sin(minute_angle)

    pygame.draw.line(
        screen, RED,
        (center_x, center_y),
        (second_x, second_y), 6
    )

    pygame.draw.line(
        screen, BLACK,
        (center_x, center_y),
        (minute_x, minute_y), 10
    )

    pygame.draw.circle(screen, RED, (center_x, center_y), 10)

    time_text = font.render(now.strftime("%H:%M:%S"), True, BLACK)
    screen.blit(time_text, (center_x - 65, 530))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
