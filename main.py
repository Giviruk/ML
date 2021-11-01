import random
import pygame
import numpy as np
from pygame.time import wait


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.group = 0
        self.is_border = False


def get_dist(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


colors = {
    0: (0, 255, 0),
    1: (0, 0, 255),
    2: (255, 0, 255),
    3: (0, 200, 255),
    4: (230, 230, 250),
    5: (240, 255, 240),
    6: (132, 112, 255)
}
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
radius_random = 30
k = 1


def init_pygame():
    WIDTH = 360  # ширина игрового окна
    HEIGHT = 480  # высота игрового окна
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    screen.fill(BLACK)
    return screen


def generate_point(point):
    count_points = random.randint(5, 10)
    for i in range(count_points):
        new_x = random.randrange(point.x - radius_random + 30, point.x + radius_random + 30, 1)
        new_y = random.randrange(point.y - radius_random + 30, point.y + radius_random + 30, 1)
        points.append(Point(new_x, new_y, point.color))
    return points


def get_neighbours(point, points):
    neighbours = []
    sorted_points = sort_points(points, point)
    for i in range(5):
        neighbours.append(sorted_points[i])

    return neighbours


def sort_points(points, point):
    for i in range(len(points) - 1):
        for j in range(len(points)):
            if get_dist(point, points[i]) < get_dist(point, points[j]):
                a = points[j]
                points[j] = points[i]
                points[i] = a
    return points


def draw_points(points, screen):
    for point in points:
        draw_point(point, screen)


def draw_point(point, screen):
    pygame.draw.circle(screen, point.color, (point.x, point.y), 3)


def init_points(screen):
    points = []
    for i in range(5):
        new_points = generate_point(Point(100*i, 100*i, colors[i]))
        for p in new_points:
            points.append(p)
    draw_points(points, screen)


def clustering(points, point):
    pass



def test_algorithm(points, new_point):
    global k
    for k in range(len(points)):
        pass



def calculate_k(points):
    pass


if __name__ == '__main__':
    points = []
    FPS = 30  # частота кадров в секунду
    clock = pygame.time.Clock()
    screen = init_pygame()
    running = True
    init_points(screen)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    draw_point(Point(event.pos[0], event.pos[1], WHITE), screen)
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pass
        pygame.display.update()


