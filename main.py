import random
import pygame


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
radius_random = 10

def init_pygame():
    WIDTH = 360  # ширина игрового окна
    HEIGHT = 480  # высота игрового окна
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    screen.fill(WHITE)
    return screen


def generate_points(point):
    count_points = random.randint(1, 4)
    points = []
    for i in range(count_points):
        new_x = random.randrange(point.x - radius_random + 3, point.x + radius_random + 3, 1)
        new_y = random.randrange(point.y - radius_random + 3, point.y + radius_random + 3, 1)
        points.append(Point(new_x, new_y, point.color))
    return points


def clustering(points):
    pass


if __name__ == '__main__':
    points = []
    FPS = 30  # частота кадров в секунду
    clock = pygame.time.Clock()
    screen = init_pygame()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_points = generate_points(Point(event.pos[0], event.pos[1], BLACK))
                    for point in new_points:
                        pygame.draw.circle(screen, point.color, (point.x, point.y), 3)
                    points.append(new_points)
        pygame.display.update()


