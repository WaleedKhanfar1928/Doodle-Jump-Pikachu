import pygame
import random

pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
background = white
player = pygame.transform.scale(pygame.image.load('Pickachu.png'), (90, 70))
spf = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False



waleed_xv_al = 170
waleed_y_val = 400
jumps = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
change_y = 0
change_x = 0
player_speed = 3
score_last = 0
super_jumps = 2
jump_last = 0




screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Lost In Space')


def check_collisions(rect_list, j):
    global waleed_xv_al
    global waleed_y_val
    global change_y
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([waleed_xv_al + 20, waleed_y_val + 60, 35, 5]) and jump == False and change_y > 0:
            j = True
    return j




def update_player(y_pos):
    global jump
    global change_y
    height_jump = 10
    gravity = .4
    if jump:
        change_y = -height_jump
        jump = False
    y_pos += change_y
    change_y += gravity
    return y_pos



def update_jumps(my_list, y_pos, change):
    global score
    if y_pos < 250 and change < 0:
        for i in range (len(my_list)):
            my_list[i][1] -= change

    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10) , 70, 10]
            score += 1
    return my_list

running = True
while running == True:
    timer.tick(spf)
    screen.fill(background)
    screen.blit(player, (waleed_xv_al, waleed_y_val))
    blocks = []
    score_text = font.render('High Score: ' + str(high_score), True, black, background)
    screen.blit(score_text, (280, 0))
    high_score_text = font.render('Score: ' + str(score), True, black, background)
    screen.blit(high_score_text, (320, 20))

    score_text = font.render('Air Jumps: (Spacebar)' + str(super_jumps), True, black, background)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render('Game Over: Spacebar to restart', True, black, background)
        screen.blit(game_over_text, (80, 80))

    
    for i in range(len(jumps)):
        block = pygame.draw.rect(screen, black, jumps[i], 0, 3)
        blocks.append(block)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                waleed_xv_al = 170
                waleed_y_val = 400
                background = white
                score_last = 0
                super_jumps = 2
                jump_last = 0
                jumps = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]

            if event.key == pygame.K_SPACE and not game_over and super_jumps > 0:
                super_jumps -= 1
                change_y = -15
            if event.key == pygame.K_a:
                change_x = - player_speed
            if event.key == pygame.K_d:
                change_x =  player_speed    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                change_x = 0
            if event.key == pygame.K_d:
                change_x =  0       

    
    jump = check_collisions(blocks, jump)
    waleed_xv_al += change_x 


    if waleed_y_val < 440:

        waleed_y_val = update_player(waleed_y_val)
    else: 
        game_over = True
        change_y = 0
        change_x = 0



    jumps = update_jumps(jumps, waleed_y_val, change_y)

    if waleed_xv_al < -20:
        waleed_xv_al = -20
    elif waleed_xv_al > 330:
        waleed_xv_al = 330

    if change_x > 0:
        player = pygame.transform.scale(pygame.image.load('Pickachu.png'), (90, 70))
    elif change_x < 0:
        player = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Pickachu.png'), (90, 70)) , 1, 0)

    if score > high_score:
        high_score = score

    if score - score_last > 15:
        score_last = score
        background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),)


    if score - jump_last > 50:
        jump_last = score
        super_jumps += 1

    pygame.display.flip()
pygame.quit

