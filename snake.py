import pygame
import random

from pygame import color
from pygame import draw
from pygame.constants import K_DOWN, K_KP_ENTER, K_LEFT, K_RIGHT, K_UP, KEYDOWN, MOUSEBUTTONDOWN, K_a, K_d, K_s, K_w
from pygame.key import name
from pygame.time import Clock
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
purple = (102,0,102)
light_red = (150,0,0)
light_green = (0,150,0)
light_blue = (0,0,150)

leader = open('leaderboard.txt','w')
leader.write(str(1))
leader.write('\n')
leader.close()

leaderNames = open('leaderboardNames.txt','w')
leaderNames.write('User')
leaderNames.write('\n')
leaderNames.close()

food_color = white
snake_color = black
bg_color = blue

movement_speed = 15
snake_sq_size = 15

clock = pygame.time.Clock()
fps = 10
leaderScore = 1
name = 'User'

WIDTH = 900
HEIGHT = 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake Project')


def snake(snake_sq_size,snake_list):
    for i in snake_list:
        pygame.draw.rect(win,snake_color,(i[0],i[1],snake_sq_size,snake_sq_size))

def draw_window(bg_color):
    win.fill(bg_color)
    pygame.display.update()

def optionsMenu():
    global fps
    global bg_color
    global snake_color
    run = True
    draw_window(black)
    while run:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if 240 > mouse[0] > 180 and 125 > mouse[1] > 95:
            pygame.draw.rect(win,green,(180,95,60,30))
            if click[0] == 1:
                fps = 10
        else:
            pygame.draw.rect(win,light_green,(180,95,60,30))

        if 330 > mouse[0] > 270 and 125 > mouse[1] > 95:
            pygame.draw.rect(win,red,(270,95,60,30))
            if click[0] == 1:
                fps = 30
        else:
            pygame.draw.rect(win,light_red,(270,95,60,30))

        if 360 > mouse[0] > 300 and 220 > mouse[1] > 190:
            if click[0] == 1:
                bg_color = red
        if 460 > mouse[0] > 400 and 220 > mouse[1] > 190:
            if click[0] == 1:
                bg_color = green
        if 560 > mouse[0] > 500 and 220 > mouse[1] > 190:
            if click[0] == 1:
                bg_color = blue
        if 660 > mouse[0] > 600 and 220 > mouse[1] > 190:
            if click[0] == 1:
                bg_color = purple

        if 360 > mouse[0] > 300 and 320 > mouse[1] > 290:
            if click[0] == 1:
                snake_color = red
        if 460 > mouse[0] > 400 and 320 > mouse[1] > 290:
            if click[0] == 1:
                snake_color = green
        if 560 > mouse[0] > 500 and 320 > mouse[1] > 290:
            if click[0] == 1:
                snake_color = blue
        if 660 > mouse[0] > 600 and 320 > mouse[1] > 290:
            if click[0] == 1:
                snake_color = purple

        pygame.draw.rect(win,purple,(600,190,60,30))
        pygame.draw.rect(win,blue,(500,190,60,30))
        pygame.draw.rect(win,red,(300,190,60,30))        
        pygame.draw.rect(win,green,(400,190,60,30))

        pygame.draw.rect(win,purple,(600,290,60,30))
        pygame.draw.rect(win,blue,(500,290,60,30))
        pygame.draw.rect(win,red,(300,290,60,30))        
        pygame.draw.rect(win,green,(400,290,60,30))        


        
        draw_text('Background Color:',100,200,blue,20)
        draw_text('Speed: ',100,100,blue,20)
        draw_text('Normal',185,100,black,15)
        draw_text('Fast',280,100,black,15)
        draw_text('Snake Color: ',100,300,blue,20)
        pygame.display.update()
    


def draw_text(msg,x,y,color,size):
    sFont = pygame.font.Font('freesansbold.ttf',size)
    sText = sFont.render(msg,True,color)
    win.blit(sText,(x,y))

def spawnFood():
    random_x = random.randint(0,WIDTH - snake_sq_size)                     # snake travels by increments of 15, so have to round to the nearest 15 so they can intersect
    random_y = random.randint(0,HEIGHT - snake_sq_size)
    random_x_rounded = round(random_x/snake_sq_size) * snake_sq_size
    random_y_rounded = round(random_y/snake_sq_size) * snake_sq_size          # rounds random_(x/y)/15 to nearest integer, then multiplies by 15 
    pygame.draw.rect(win,food_color,(random_x_rounded,random_y_rounded,snake_sq_size,snake_sq_size))
    pygame.display.update()       
    return (random_x_rounded,random_y_rounded)

def gameOver(length):
    global leaderScore
    global leaderName
    overprompt = True
    leaderScore = open('leaderboard.txt','a')
    leaderScore.write(str(length))
    leaderScore.write('\n')
    leaderScore.close()
    leaderName = open('leaderboardNames.txt','a')
    leaderName.write(name)
    leaderName.write('\n')
    leaderName.close()
    while overprompt:
        win.fill(black)
        draw_text('Final score:',390,100,white,20)
        draw_text(str(length),520,100,white,20)
        draw_text("'X' to play again or 'M' to return to main menu", 240,200,red,20)   #button?
        pygame.display.update()
        for event in pygame.event.get():
            if event.key == pygame.K_x:
                main()
            if event.key == pygame.K_m:
                start_screen()
                overprompt = False



def inputScreen():
    global name
    name = ''
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
                if event.key == pygame.K_RETURN:
                    run = False
                    start_screen()

        win.fill(purple)
        draw_text('Enter Username',320,100,black,30)
        pygame.draw.rect(win,white,(240,200,400,40))
        draw_text(name,400,210,black,20)
        pygame.display.update()

def start_screen():
    f = open('leaderboard.txt','r')
    f2 = open('leaderboardNames.txt','r')

    rScores = f.readlines()
    rNames = f2.readlines()
    scores = []
    names = []

    for i in rScores:
        scores.append(int(i.strip()))
    for i in rNames:
        names.append(i.strip())
    l = []
    for i in zip(names,scores):   
        l.append(i)
    m = max(l)
    maxscore = m[1]
    maxname = m[0]

    global leaderScore
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        win.fill(black)
        font = pygame.font.Font('freesansbold.ttf',90)
        text = font.render('Snake Game',True,green)
        win.blit(text,(155,15))
        subfont = pygame.font.Font('freesansbold.ttf',40)
        subtext = subfont.render('by Nick',True,white)
        win.blit(subtext,(370,110))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((WIDTH/2)-100)+200 > mouse[0] > WIDTH/2 - 100 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(win,green,((WIDTH/2)-100,200,200,50))
            if click[0] == 1:
                main()
        else:
            pygame.draw.rect(win,light_green,((WIDTH/2)-100,200,200,50))

        if  ((WIDTH/2)-100)+200 > mouse[0] > WIDTH/2 - 100 and 350 > mouse[1] > 300:
            pygame.draw.rect(win,blue,((WIDTH/2)-100,300,200,50))
            if click[0] == 1:
                optionsMenu()
        else:
            pygame.draw.rect(win,light_blue,((WIDTH/2)-100,300,200,50))
        if ((WIDTH/2)-100)+200 > mouse[0] > WIDTH/2 - 100 and 450 > mouse[1] > 400:
            pygame.draw.rect(win,red,((WIDTH/2)-100,400,200,50))
            if click[0] == 1:
                quit()
        else:
            pygame.draw.rect(win,light_red,((WIDTH/2)-100,400,200,50))

        draw_text('Top Score:',100,250,white,20)
        draw_text(maxname + ':',100,300,white,20)
        draw_text(str(maxscore),170,300,white,20)
        draw_text('Start Game',WIDTH/2 - 60,215,white,20)
        draw_text('Options',WIDTH/2 - 50,315,white,20)
        draw_text('QUIT',WIDTH/2 - 35, 415,white,20)


        pygame.display.update()

def main():
    
    snake_list = []
    length = 1
    head_x = WIDTH/2      
    head_y = HEIGHT/2 - 10   #make sure the snake starts on a multiple of 15 so food lines up       # super diagnol mode? get rid of the other lead_change into 0
    head_x_change = 0
    head_y_change = 0
    draw_window(bg_color)
    apple_x,apple_y = spawnFood()
    run = True
    while run:
        keys = pygame.key.get_pressed()                             #https://www.youtube.com/watch?v=ldh13IP8GAY&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=8
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_x_change = -movement_speed
                    head_y_change = 0
                if event.key == pygame.K_RIGHT:
                    head_x_change = movement_speed
                    head_y_change = 0
                if event.key == pygame.K_DOWN:
                    head_y_change = movement_speed
                    head_x_change = 0
                if event.key == pygame.K_UP:                   
                    head_y_change = -movement_speed
                    head_x_change = 0

        if head_x > WIDTH-snake_sq_size or head_x < 0:
            head_x_change = 0
            overprompt = True
            while overprompt:
                gameOver(length)


        if head_y > HEIGHT or head_y <0-snake_sq_size:
            head_y_change = 0
            overprompt = True
            while overprompt:
                gameOver(length)



        head_x += head_x_change
        head_y += head_y_change


        win.fill(bg_color)
        draw_text("Score: ",0,0,white,20)
        draw_text(str(length),80,0,white,20)
        pygame.draw.rect(win,food_color,(apple_x,apple_y,snake_sq_size,snake_sq_size))
        snake_head = []
        snake_head.append(head_x)
        snake_head.append(head_y)                                                             #https://www.youtube.com/watch?v=4MUcUhL0tMw&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=20
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                gameOver(length)

        snake(snake_sq_size,snake_list)
        pygame.display.update()
        clock.tick(fps)
        if (apple_x,apple_y) == (head_x,head_y):
            apple_x,apple_y = spawnFood()
            length += 1


inputScreen()
