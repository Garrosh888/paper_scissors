import sys
import pygame
from game_pers import Game_pers
from random import randint
from  restart_button import Return
from score import Stat
new_game = True
def check_win():
    global my_object,pc_object,new_game
    if new_game == False:
        return
    resalt = None

    if my_object == "scissors":
        if pc_object == "paper":
            new_game = False
            game_statistics.points_my +=1
            resalt = "win"
        elif pc_object == "stone":
            new_game = False
            game_statistics.points_pc +=1
            resalt = "lose"
    elif my_object == "paper":
        if pc_object == "scissors":
            new_game = False
            game_statistics.points_pc +=1
            resalt = "lose"
        elif pc_object == "stone":
            new_game = False
            game_statistics.points_my +=1
            resalt = "win"
    elif my_object == "stone":
        if pc_object == "scissors":
            new_game = False
            game_statistics.points_my +=1
            resalt = "win"
        elif pc_object == "paper":
            new_game = False
            game_statistics.points_pc +=1
            resalt = "lose"
    if pc_object == my_object:
        resalt = "ne"
    my_object = None
    pc_object = None
    game_statistics.create_text()
    if resalt == "win":
        game_statistics.image = game_statistics.image_win
        game_statistics.show = True
    elif resalt == "lose":
        game_statistics.image = game_statistics.image_lose
        game_statistics.rect.centerx += 30
        game_statistics.show = True



def restart_game():
    print("restart")
    global  move_paper_pc,move_stone_pc,move_scissors_pc,\
        moving_pc,moving,move_paper,move_stone,move_scissors,my_object,pc_object,new_game
    for i in all_game_objects:
        i.default_position()
    new_game = True
    move_paper = False
    move_stone = False
    move_scissors = False
    moving = False
    move_paper_pc = False
    move_stone_pc = False
    move_scissors_pc = False
    moving_pc = False
    game_statistics.show = False
    pc_object = None
    my_object = None


def turn_pc():#начало хода компютера
    global move_paper_pc,move_stone_pc,move_scissors_pc,moving_pc,pc_object
    x = 4
    if moving_pc == False:
        x = randint(1,3)

        moving_pc = True
    if x == 1 and move_scissors_pc == False and move_stone_pc == False:
        move_paper_pc = True
        pc_object = "paper"
    elif x == 2 and move_paper_pc == False and move_stone_pc == False:
        move_scissors_pc = True
        pc_object = "scissors"
    elif x == 3 and move_paper_pc == False and move_scissors_pc == False:
        move_stone_pc = True
        pc_object = "stone"
    if moving_pc == True:
        if move_paper_pc == True:
            movving_object_pc(pc_paper,1)
        elif move_scissors_pc == True:
            movving_object_pc(pc_scissors,-1)
        elif move_stone_pc == True:
            movving_object_pc(pc_stone,0)
    check_win()

def movving_object_pc(object_pc,x):
    global moving_pc
    if object_pc.rect.y < 300:
        object_pc.rect.y += 1
        object_pc.rect.x  -=x
    else:
        moving_pc = False

def my_turn(object,limity,limitx):
    global moving
    turn_pc()
    if object.rect.y > limity:#это позиция до которой поднимаеться наш объект
        object.rect.y -= 1
        object.rect.x -= limitx
    else:
        moving = True


def left_click():#
    global my_object
    if move_paper == True:
        my_turn(user_paper,300,1)
        my_object = "paper"
    if move_stone == True:
        my_turn(user_stone,370,0)
        my_object ="stone"
    if move_scissors == True:
        my_turn(user_scissors,270,-1)
        my_object = "scissors"

def white_image():
    pos_mouse = pygame.mouse.get_pos()
    if user_paper.rect.collidepoint(pos_mouse):
        user_paper.image = pygame.image.load("white_paper.png")
        user_paper.small_image = pygame.transform.scale(user_paper.image,(user_paper.image.get_width()/2,user_paper.image.get_height()/2))
    else:
        user_paper.image = pygame.image.load("paper_png.png")
        user_paper.small_image = pygame.transform.scale(user_paper.image,(user_paper.image.get_width()/2,user_paper.image.get_height()/2))

    if user_stone.rect.collidepoint(pos_mouse):
        user_stone.image = pygame.image.load("white_stone.png")
        user_stone.small_image = pygame.transform.scale(user_stone.image, (user_stone.image.get_width() / 2, user_stone.image.get_height() / 2))
    else:
        user_stone.image = pygame.image.load("stone_png.png")
        user_stone.small_image = pygame.transform.scale(user_stone.image, (user_stone.image.get_width() / 2, user_stone.image.get_height() / 2))

    if user_scissors.rect.collidepoint(pos_mouse):
        user_scissors.image = pygame.image.load("white_scissors.png")
        user_scissors.small_image = pygame.transform.scale(user_scissors.image, (
        user_scissors.image.get_width() / 2, user_scissors.image.get_height() / 2))
    else:
        user_scissors.image = pygame.image.load("scissors_png.png")
        user_scissors.small_image = pygame.transform.scale(user_scissors.image, (
        user_scissors.image.get_width() / 2, user_scissors.image.get_height() / 2))

pygame.init()
window = pygame.display.set_mode((700,700))
image = pygame.image.load("fone.png")
image_fone = pygame.transform.scale(image,(700,700))
user_paper = Game_pers(window,pygame.image.load("paper_png.png"),530,600,"paper")
user_scissors = Game_pers(window, pygame.image.load("scissors_png.png"), 35, 560, "scissors")
user_stone = Game_pers(window,pygame.image.load("stone_png.png"),300,540,"stone")
pc_paper = Game_pers(window,pygame.image.load("pc_paper_png.png"),525,110,"paper")
pc_scissors = Game_pers(window,pygame.image.load("pc_scissors_png.png"),0,80,"scissors")
pc_stone = Game_pers(window,pygame.image.load("pc_stone_png.png"),270,80,"stone")
restart_button = Return(window)
all_game_objects = [user_paper,user_stone,user_scissors,pc_paper,pc_scissors,pc_stone]
game_statistics = Stat(window)
my_object = None
pc_object = None

move_paper = False
move_stone = False
move_scissors = False
moving = False
move_paper_pc = False
move_stone_pc = False
move_scissors_pc = False
moving_pc = False

while True:
    window.blit(image_fone,(0,0))
    user_paper.art_pers()
    user_scissors.art_pers()
    user_stone.art_pers()
    pc_stone.art_pers()
    pc_paper.art_pers()
    pc_scissors.art_pers()
    restart_button.art_return()
    game_statistics.art_text()
    white_image()
    left_click()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:#дз тут тут надо добавить еще 1 if для ристарта
            mouse_pos = pygame.mouse.get_pos()#тут хранится текущая позиция курсора(мышки)
            if user_paper.rect.collidepoint(mouse_pos) and move_paper == False and moving == False and move_stone == False and move_scissors == False:
                move_paper = True
            if user_stone.rect.collidepoint(mouse_pos) and move_stone == False and moving == False and move_paper == False and move_scissors == False:
                move_stone = True
            if user_scissors.rect.collidepoint(mouse_pos) and move_scissors == False and moving == False and move_stone == False and move_paper == False:
                move_scissors = True
            if restart_button.rect.collidepoint(mouse_pos):
                restart_game()
    pygame.display.flip()







