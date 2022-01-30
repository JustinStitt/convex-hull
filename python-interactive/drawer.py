import pygame
import sys
from convexHull import Point, convexHull

WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = (44, 50, 41)
points = []
convex_hull_points = []

def init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Convex Hull - Justin Stitt')
    return screen

def check_quit(e):
    if e.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def check_mouse(e):
    m_pos = None
    if e.type == pygame.MOUSEBUTTONUP:
        m_pos = pygame.mouse.get_pos()
    return m_pos

def check_keypress(e):
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_UP:
            return True
    return False

def create_point(m_pos):
    global points
    np = Point(m_pos[0], m_pos[1])
    points.append(np)

def draw_points(screen):
    global points
    for p in points:
        pygame.draw.rect(screen, (255,0,0), (p.x, p.y, 10, 10))


def get_convex_hull(screen):
    global points, convex_hull_points
    convex_hull_points = convexHull(points)

def draw_convex_hull(screen):
    global convex_hull_points
    for line_segment in convex_hull_points:
        pygame.draw.line(screen, (0,255,0), (line_segment[0].x, 
                                            line_segment[0].y),
                                            (line_segment[1].x,
                                                line_segment[1].y), width = 2)

def update(screen):
    global convex_hull_points
    for event in pygame.event.get():
        check_quit(event)
        k = check_keypress(event)
        if k is True: 
            get_convex_hull(screen)
        m_pos = check_mouse(event)
        if m_pos is not None:
            create_point(m_pos)
            convex_hull_points = []


def render(screen):
    screen.fill(BACKGROUND_COLOR)
    # stuff
    draw_points(screen)
    if len(convex_hull_points) > 2:
        draw_convex_hull(screen)
    pygame.display.update()

def main():
    screen = init()
    while True:
        update(screen)
        render(screen)

if __name__ == '__main__':
    main()
