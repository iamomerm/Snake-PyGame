# ╔═╗╔╗╔╔═╗╦╔═╔═╗
# ╚═╗║║║╠═╣╠╩╗║╣
# ╚═╝╝╚╝╩ ╩╩ ╩╚═╝

import pygame
from random import choice, randint

# Init
pygame.init()

# Spec
WIN = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake.py')
FONT = pygame.font.SysFont('consolas', 15)
HORIZONTAL_STEPS = [i for i in range(25, 575) if i % 10 == 0]
VERTICAL_STEPS = [i for i in range(25, 375) if i % 10 == 0]

def draw_window():
    WIN.fill((255, 255, 255))

    if globals()['gameover']:
        WIN.blit(FONT.render('Game Over !', False, (0, 0, 0)), (10, 10))
        WIN.blit(FONT.render('Press "R" to Retry ..', False, (0, 0, 0)), (10, 30))

    else:
        WIN.blit(FONT.render(f'Score: %d' % globals()['score'], False, (0, 0, 0)), (10, 10))

        # Timer
        if globals()['timer'] < 60:
            timer_color = (255, 0, 0)
        elif globals()['timer'] < 120:
            timer_color = (255, 165, 0)
        else:
            timer_color = (0, 0, 0)

        WIN.blit(FONT.render(f'Timer: %d' % globals()['timer'], False, timer_color), (10, 30))

        # Snake
        pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(*globals()['snake'].values()))

        # Snack
        pygame.draw.rect(WIN, (randint(0, 255), randint(0, 255), randint(0, 255)), pygame.Rect(*globals()['snack'].values()))

    pygame.display.update()  # Update Display

def move():
    if globals()['direction'] == 'R':
        globals()['snake']['x'] += 10
    elif globals()['direction'] == 'L':
        globals()['snake']['x'] -= 10
    elif globals()['direction'] == 'U':
        globals()['snake']['y'] -= 10
    elif globals()['direction'] == 'D':
        globals()['snake']['y'] += 10

def main():
    directions = {pygame.K_LEFT: 'L', pygame.K_RIGHT: 'R', pygame.K_UP: 'U', pygame.K_DOWN: 'D'}

    globals()['gameover'] = False
    globals()['timer'] = 180
    globals()['score'] = 0
    globals()['direction']  = 'R'
    globals()['snake'] = {'x': 300, 'y': 200, 'width': 10, 'height': 10}
    globals()['snack'] = {'x': choice(HORIZONTAL_STEPS), 'y': choice(VERTICAL_STEPS), 'width': 10, 'height': 10}


    # Game
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)  # FPS

        move()
        globals()['timer'] -= 1

        # Events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:  # Keydown for Single Click = Single Event
                if event.key in directions:
                    globals()['direction'] = directions[event.key]
                elif event.key == pygame.K_r:
                    globals()['gameover'] = False
                    globals()['timer'] = 180
                    globals()['score'] = 0
                    globals()['snake'] = {'x': 300, 'y': 200, 'width': 10, 'height': 10}

        # Eat Snack
        if [globals()['snake']['x'], globals()['snake']['y']] == [globals()['snack']['x'], globals()['snack']['y']]:
            globals()['snack']['x'] = choice(HORIZONTAL_STEPS)
            globals()['snack']['y'] = choice(VERTICAL_STEPS)
            globals()['score'] += 10
            globals()['timer'] = 180

        # Game Over
        if globals()['timer'] == 0:
            print('Timeout - Game Over!')
            globals()['gameover'] = True

        if globals()['snake']['x'] in [0, 600] or globals()['snake']['y'] in [0, 400]:
            print('Game Over!')
            globals()['gameover'] = True

        draw_window()
    pygame.quit()

if __name__ == '__main__':
    main()