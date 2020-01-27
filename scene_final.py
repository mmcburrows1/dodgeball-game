import pygame
import random
from player_class import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
pygame.font.init()
pygame.font.SysFont("Arial",115)

pygame.mixer.init(48000, -16, 1, 1024)



from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
off_white = (200,200,200) 
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gameText = pygame.font.SysFont("Arial",115)

game_title = pygame.display.set_caption("DODGEBALL 2k20")

# Defining text objects?
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def black_text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# This is the text for the title on the intro screen
def message_display(text):
    gameText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/2)))
    screen.blit(TextSurf, TextRect)

# This is the message for the space key funcitonality on the intro screen
def continue_message_display(text):
    gameText = pygame.font.SysFont("Arial",25)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/1.5)))
    screen.blit(TextSurf, TextRect)

# Loading background graphics
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
background_rect = background.get_rect()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

pygame.init()

intro = True
while intro:
    screen.fill(black)
    message_display("DODGEBALL 2k20")
    continue_message_display("PRESS THE SPACE KEY TO CONTINUE")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                intro = False
                pygame.quit()
                quit()
                break
        elif event.type == QUIT:
            intro = False
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intro = False
                break

pygame.mixer.init()
in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
in_game_song.set_volume(0.1)
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
pygame.quit()
quit()
