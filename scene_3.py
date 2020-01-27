import pygame
# import time
import random
from player_class import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
# font_dir = path.join(path.dirname(__file__), 'font')
pygame.font.init()
pygame.font.SysFont("Arial",115)

# pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init(48000, -16, 1, 1024)


# Load all game graphics

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# pygame.init()
# pygame.mixer.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
off_white = (200,200,200) #shoutout virgil
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gameText = pygame.font.SysFont("Arial",115)

game_title = pygame.display.set_caption("DODGEBALL 2k20")

# Game clock
clock = pygame.time.Clock()

# Defining text objects?
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def black_text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Defining the text display type (font)
def message_display(text):
    gameText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/2)))
    screen.blit(TextSurf, TextRect)

# This is to display the option to continue into the game (testing for rn to see if i can transition from main menu screen to game)
def continue_message_display(text):
    gameText = pygame.font.SysFont("Arial",25)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/1.5)))
    screen.blit(TextSurf, TextRect)

# def button(msg, x, y, w, h, ic, ac, action = None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()

#     if x + w > mouse[0] > x and y + h > mouse[1] > y:
#         pygame.draw.rect(screen, ac,(x,y,w,h))
#         if click[0] == 1 and action != None:
#             if action == "single player":
#                 intro = False
#                 # game_loop()
#             elif action == "two player":
#                 intro = False
#                 # game_loop()
#             elif action == "quit":
#                 pygame.quit()
#                 quit()
            
#     else: 
#         pygame.draw.rect(screen, ic,(x,y,w,h))
    
    # smallText = pygame.font.SysFont("Arial",15)
    # textSurf, textRect = black_text_objects(msg, smallText)
    # textRect.center = ((x + (w/2)), y + (h/2))
    # screen.blit(textSurf, textRect)

# Loading background graphics
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
background_rect = background.get_rect()



#Loading game sound
# in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
# in_game_song.set_volume(0.1)
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Running hit() as a crash() (like crashing a video game car) function for right now bc dont have collision functionality at the moment
def hit():
    message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
pygame.init()
# def game_loop():
x = (SCREEN_WIDTH * 0.45)
#     y = (SCREEN_HEIGHT * 0.8)

    # Run until the user asks to quit
intro = True
while intro:
    # for event in pygame.event.get():
    #     if event.type == KEYDOWN:
    #         if event.key == K_SPACE:
    screen.fill(black)
    message_display("DODGEBALL 2k20")
    continue_message_display("PRESS THE SPACE KEY TO CONTINUE")

    # def button(msg, x, y, w, h, ic, ac, action = None):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()

    #     if x + w > mouse[0] > x and y + h > mouse[1] > y:
    #         pygame.draw.rect(screen, ac,(x,y,w,h))
    #         if click[0] == 1 and action != None:
    #             if action == "single player":
    #                 # intro = False
    #                 # return
    #                 game_loop()
    #             elif action == "two player":
    #                 # intro = False
    #                 # return
    #                 game_loop()
    #             elif action == "quit":
    #                 pygame.quit()
    #                 quit()
    #     else: 
    #         pygame.draw.rect(screen, ic,(x,y,w,h))    
            
        
        # intro = False

        # smallText = pygame.font.SysFont("Arial",15)
        # textSurf, textRect = black_text_objects(msg, smallText)
        # textRect.center = ((x + (w/2)), y + (h/2))
        # screen.blit(textSurf, textRect)

    # button("SINGLE PLAYER", 250,350,100,50, white, off_white, "single player")
    # button("TWO PLAYER", 450,350,100,50, white, off_white, "two player")
    # button("EXIT GAME", 350,450,100,50, bright_red, red, "quit")
    # intro = False

    
   

    # if 450 + 100 > mouse[0] > 450 and 350 + 50 > mouse[1] > 350:
    #     pygame.draw.rect(screen, off_white,(450,350,100,50))
    # else:
    #     pygame.draw.rect(screen, white,(450,350,100,50))
    
    # smallText = pygame.font.SysFont("Arial",15)
    # textSurf, textRect = black_text_objects("TWO PLAYER", smallText)
    # textRect.center = ((450 + (100/2)), 350 + (50/2))
    # screen.blit(textSurf, textRect)

    # if 350 + 100 > mouse[0] > 350 and 450 + 50 > mouse[1] > 450:
    #     pygame.draw.rect(screen, red,(350,450,100,50))
    # else:
    #     pygame.draw.rect(screen, bright_red,(350,450,100,50))

    # smallText = pygame.font.SysFont("Arial",15)
    # textSurf, textRect = black_text_objects("EXIT GAME", smallText)
    # textRect.center = ((350 + (100/2)), 450 + (50/2))
    # screen.blit(textSurf, textRect)

    

    pygame.display.update()
    for event in pygame.event.get():
        # if event.type == KEYDOWN:
        #     if event.key == K_SPACE:
        #         intro = False
        #         break
    # for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # hit()
                # message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
                intro = False
                pygame.quit()
                quit()
                break
        elif event.type == QUIT:
            message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
            intro = False
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intro = False
                break

    # screen.fill(black)
    # message_display("DODGEBALL 2k20")
    # continue_message_display("PRESS THE SPACE KEY TO CONTINUE")
    # pygame.display.update()
    # for event in pygame.event.get():
    #     if event.type == KEYDOWN:
    #         if event.key == K_SPACE:
    #             intro = False
    #             break

# pygame.mixer.pre_init(44100, -16, 1, 512)
# pygame.mixer.init(48000, -16, 1, 1024)
def game_loop():
    pygame.mixer.init()
    in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
    in_game_song.set_volume(0.1)
# def game loop():
    running = True
    while running:

        # Did the user click the window close button? ************************
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    break
            elif event.type == QUIT:
                running = False
                break

        #Get all the keys currently pressed ************************
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on keypresses ************************
        player.update(pressed_keys)
            # Fill the background with white ************************
        screen.fill(black)
        screen.blit(background, background_rect)
        in_game_song.play()

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        surf = pygame.Surface((50,50))
        surf.fill((255,33,127))

        surf_center = (
            (SCREEN_WIDTH-surf.get_width())/2,
            (SCREEN_HEIGHT -surf.get_height())/2,
        )

        screen.blit(player.surf, player.rect)
        # Flip the display ************************
        pygame.display.flip()

    # Done! Time to quit. ************************
game_loop()
pygame.quit()
quit()
