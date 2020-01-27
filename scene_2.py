# Simple pygame program

# Import and initialize the pygame library
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

pygame.mixer.pre_init(44100, -16, 1, 512)
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

pygame.init()
pygame.mixer.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gameText = pygame.font.SysFont("Arial",115)

game_title = pygame.display.set_caption("Operation Dodgeball")

# Game clock
clock = pygame.time.Clock()

# Defining text objects?
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# Defining the text display type (font)
def message_display(text):
    gameText = pygame.font.SysFont("Arial",115)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/2)))
    screen.blit(TextSurf, TextRect)

# This is to display the option to continue into the game (testing for rn to see if i can transition from main menu screen to game)
def continue_message_display(text):
    gameText = pygame.font.SysFont("Arial",50)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/4)))
    screen.blit(TextSurf, TextRect)

    
    # time.sleep(10)

    # game_loop()

    # pygame.display.update()

# when game over print "game over" *******************************************************************************************************
# def hit():
#     message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")

# Display start screen
# show_start_screen = *********************************************************************************************************************

# Display game over screen
# show_go_screen = *********************************************************************************************************************

# eliminated = False *********************************************************************************************************************
# while not eliminated:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             eliminated = True

#         print(event)
    
    # pygame.display.update()

    # clock.tick(60)
            # pygame.quit()
            # quit()

    # screen.fill(0,0,0)
    # gameText = pygame.font.Font("BlackOpsOne-Regular.ttf",115)

# Loading background graphics
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
background_rect = background.get_rect()



#Loading game sound
in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
in_game_song.set_volume(0.1)
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Running hit() as a crash() (like crashing a video game car) function for right now bc dont have collision functionality at the moment
def hit():
    message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")

# def game_loop():
x = (SCREEN_WIDTH * 0.45)
#     y = (SCREEN_HEIGHT * 0.8)

    # Run until the user asks to quit
intro = True
while intro:
    # for event in pygame.event.get():
    #     if event.type == KEYDOWN:
    #         if event.key == K_SPACE:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # hit()
                # message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
                pygame.quit()
                quit()
                break
        elif event.type == QUIT:
            message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
            pygame.quit()
            quit()

    screen.fill(black)
    message_display("DODGEBALL 2k20")
    continue_message_display("PRESS THE SPACE KEY TO CONTINUE")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intro = False
                break
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

    # Putting the draw_text function after the sprites makes it print over the sprite so it looks like sprite is moving behind text, N/A to the test text
    # (screen) = surface you want, (test_text) = text you want, (18) = font size, (SCREEN_WIDTH/2) = x coordinate of screen... in this case it is centered since it is divided by 2, (10) = y coordinate of screen
    # draw_text(screen, test_text, 18, SCREEN_WIDTH/2, 10)

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
pygame.quit()


























# running = True
# while running:

#     # Did the user click the window close button?
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 # hit()
#                 # message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#                 running = False
#                 break
#         elif event.type == QUIT:
#             message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#             running = False

#             pygame.display.update()

#             # clock.tick(60)
#             # break
#         # elif event.type = hit(): ******************************************************************************************************
#         #     running = False            
#         #     break
    
#     screen.blit(background, background_rect)
#     pygame.display.update()

#     in_game_song.play()

# # show_start_screen ********************************************************************************************************************

#     for entity in all_sprites:                  
#         screen.blit(entity.surf, entity.rect)

#     # entity_width = 25

#     surf = pygame.Surface((50,50))
#     surf.fill((255,33,127))
    
#     surf_center = (
#         (SCREEN_WIDTH-surf.get_width())/2,
#         (SCREEN_HEIGHT -surf.get_height())/2,
#     )

#                 # if x > SCREEN_WIDTH - entity_width or x < 0:
#                 #     hit()
                        
#     pygame.display.update()
#                 # clock.tick(60)

#     screen.blit(player.surf, player.rect)
#                 # Flip the display
#     pygame.display.flip()
#         # if event.type == KEYDOWN:
#         #     if event.key == K_ESCAPE:
#         #         # hit()
#         #         # message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#         #         running = False
#         #         break
#         # elif event.type == QUIT:
#         #     message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#         #     running = False

#         #     pygame.display.update()

# # Where i commented the rest of shit out after else statement above
#     #Get all the keys currently pressed
#     # pressed_keys = pygame.key.get_pressed()
#     #  # Update the player sprite based on keypresses
#     # player.update(pressed_keys)
#     #     # Fill the background with white
#     # screen.fill(black)
#     # message_display("OPERATION: DODGEBALL")
#     # continue_message_display("PRESS THE SPACE KEY TO CONTINUE")
#     # for event in pygame.event.get():
#     #     if event.type == KEYDOWN:
#     #         if event.key == K_SPACE:
#     #             screen.blit(background, background_rect)
#     #             pygame.display.update()

#     #             in_game_song.play()
          
#     # # show_start_screen ********************************************************************************************************************

#     #     for entity in all_sprites:                  
#     #         screen.blit(entity.surf, entity.rect)

#     #     # entity_width = 25

#     #     surf = pygame.Surface((50,50))
#     #     surf.fill((255,33,127))
        
#     #     surf_center = (
#     #         (SCREEN_WIDTH-surf.get_width())/2,
#     #         (SCREEN_HEIGHT -surf.get_height())/2,
#     #     )

#     #                 # if x > SCREEN_WIDTH - entity_width or x < 0:
#     #                 #     hit()
                            
#     #     pygame.display.update()
#     #                 # clock.tick(60)

#     #     screen.blit(player.surf, player.rect)
#     #                 # Flip the display
#     #     pygame.display.flip()
#     #         # if event.type == KEYDOWN:
#     #         #     if event.key == K_ESCAPE:
#     #         #         # hit()
#     #         #         # message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#     #         #         running = False
#     #         #         break
#     #         # elif event.type == QUIT:
#     #         #     message_display("GAME OVER : ALL ALLIED PLAYERS ELIMINATED")
#     #         #     running = False

#     #         #     pygame.display.update()
# # Done! Time to quit.
# pygame.quit()