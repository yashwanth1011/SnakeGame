import pygame
import time
import random

pygame.init()
width = 600
height = 500

dis = pygame.display.set_mode((width, width))
pygame.display.update()
pygame.display.set_caption("Snake Game")
blue = (0, 0 , 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)


clock = pygame.time.Clock()
snake_speed = 10
snake_block = 10

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)

def your_score(score):
    value = score_font.render("Your Score :" + str(score), True, white)
    dis.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg,[width/2 - 200, height/2])

def gameloop():
    game_over = False
    game_close = False
    x1 = width/2
    y1 = height/2

    x1_changed = 0
    y1_changed = 0
    snake_list = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0,width - snake_block)/ 10.0) * 10.0
    foody = round(random.randrange(0,height - snake_block)/ 10.0) * 10.0
    
    
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_changed = -snake_block
                    y1_changed = 0
                elif event.key == pygame.K_RIGHT:
                    x1_changed = snake_block
                    y1_changed = 0
                elif event.key == pygame.K_UP:
                    y1_changed = -snake_block
                    x1_changed = 0
                elif event.key == pygame.K_DOWN:
                    y1_changed = snake_block
                    x1_changed = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

                    
        x1 += x1_changed
        y1 += y1_changed
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[: -1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        your_score(Length_of_snake - 1)

    
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,width - snake_block)/ 10.0) * 10.0
            foody = round(random.randrange(20,height - snake_block)/ 10.0) * 10.0
            Length_of_snake+= 1
            
            print("Need more!!!")
        clock.tick(snake_speed)
    time.sleep(2)
    pygame.quit()
    quit()


gameloop()


