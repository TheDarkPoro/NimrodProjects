import pygame
import sys
import random
pygame.init()
apple = [random.randrange(0, 19), random.randrange(0, 19)]
WINSIZE = (500, 500)
BLOCKSIZE = 25
win = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption("Snake")
snake = [[10, 10], [10, 10], [10, 10]]
direc = [0, 0]
clock = pygame.time.Clock()
score = 0
timer = 0
pause = False


def addlist(list1: list, list2: list):
    return [list1[0] + list2[0], list1[1] + list2[1]]

def move():
    global snake
    global apple
    global score
    global direc
    if direc != [0, 0]:
        if (addlist(snake[0], direc)[0] == -1 or
            addlist(snake[0], direc)[0] == 20 or
            addlist(snake[0], direc)[1] == -1 or
            addlist(snake[0], direc)[1] == 20 or
                addlist(snake[0], direc) in snake):
            snake = [[9, 10], [9, 10], [9, 10]]
            direc = [0, 0]
            score = 0
            apple = [random.randrange(0, 19), random.randrange(0, 19)]
        else:
            pass
            if addlist(snake[0], direc) != apple:
                snake.pop()
            else:
                score += 1
                apple = [random.randrange(0, 19), random.randrange(0, 19)]
                while apple in snake:
                    apple = [random.randrange(0, 19), random.randrange(0, 19)]
            snake.insert(0, addlist(snake[0], direc))


while True:
    moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pause = False
            if event.key == pygame.K_ESCAPE:
                pause = True
                direc = [0, 0]
            if event.key == pygame.K_RIGHT:
                if addlist(snake[0], [1, 0]) != snake[1]:
                    if direc != [1, 0] and not moved:
                        direc = [1, 0]
                        move()
                        moved = True
                    direc = [1, 0]

            if event.key == pygame.K_LEFT:
                if addlist(snake[0], [-1, 0]) != snake[1]:
                    if direc != [-1, 0] and not moved:
                        direc = [-1, 0]
                        move()
                        moved = True
                    direc = [-1, 0]
            if event.key == pygame.K_UP:
                if addlist(snake[0], [0, -1]) != snake[1]:
                    if direc != [0, -1] and not moved:
                        direc = [0, -1]
                        move()
                        moved = True
                    direc = [0, -1]
            if event.key == pygame.K_DOWN:
                if addlist(snake[0], [0, 1]) != snake[1]:
                    if direc != [0, 1] and not moved:
                        direc = [0, 1]
                        move()
                        moved = True
                    direc = [0, 1]

    if not moved:
        move()
    pygame.draw.rect(win, (255, 0, 0), ((apple[0]*BLOCKSIZE, apple[1]*BLOCKSIZE), (BLOCKSIZE, BLOCKSIZE)))
    for block in snake:
        if 100 + score*3 > 255:
            if 100 - score * 3 < 50:
                pygame.draw.rect(win, (255, 50, 50), (block[0]*BLOCKSIZE, block[1]*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
            else:
                pygame.draw.rect(win, (255, 100 - score * 3, 100 - score * 3),
                                 (block[0] * BLOCKSIZE, block[1] * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
        else:
            pygame.draw.rect(win, (100 + score*3, 100, 100), (block[0] * BLOCKSIZE, block[1] * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))
        if addlist(block, [0, -1]) in snake:
            pieceindex = None
            blockindex = None
            for i in range(len(snake)):
                if snake[i] == addlist(block, [0, -1]):
                    pieceindex = i
                if snake[i] == block:
                    blockindex = i
            if abs(pieceindex - blockindex) > 1:
                pygame.draw.rect(win, (0, 0, 0), (block[0], block[1] - 2, BLOCKSIZE, 4))
        # if addlist(block):
        # if addlist(block):
        # if addlist(block):
    if pause:
        timer += 1
        if 6<timer:
            if timer<14:
                pygame.draw.rect(win, (170, 170, 170), (WINSIZE[0] / 2 + 15, WINSIZE[1] / 2 - 50, 50, 100))
                pygame.draw.rect(win, (170, 170, 170), (WINSIZE[0] / 2 - 65, WINSIZE[1] / 2 - 50, 50, 100))
            else:
                timer = 0
    text = pygame.font.Font("CHICKEN Pie.ttf", 50)
    textsurface = text.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(textsurface, (10, -5))
    clock.tick(9)
    pygame.display.update()
    win.fill((0, 0, 0))
