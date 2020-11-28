import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Zoom')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    points = list()
    max_mod = 2.5
    min_mod = 0.1
    modifier = 1
    with open('points.txt') as file:
        for i in file.read().split('),')[:-1]:
            points.append(tuple(map(float, i.strip()[1:].replace(',', '.').split(';'))))
    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:
                    modifier = min(modifier + 0.1, max_mod)
                elif event.button == 5:
                    modifier = max(modifier - 0.1, min_mod)
        points_drawn = [(i[0] * 15 * modifier + width // 2,
                         height - (i[1] * 15 * modifier + height // 2)) for i in points]
        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, pygame.Color('white'), points_drawn, 1)
        pygame.display.flip()
    pygame.quit()
