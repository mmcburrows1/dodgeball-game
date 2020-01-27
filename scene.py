# # ************************ = already commented (don't uncomment)

# # Simple pygame program ************************

# # Import and initialize the pygame library ************************
# import pygame
# import random
# from player_class import *
# from os import path

# img_dir = path.join(path.dirname(__file__), 'img')
# snd_dir = path.join(path.dirname(__file__), 'snd')
# # pygame.mixer.pre_init(44100, -16, 1, 512) ************************
# pygame.mixer.init(48000, -16, 1, 1024)


# # Load all game graphics ************************

# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )

# pygame.init()
# pygame.mixer.init()

# # Set up the drawing window ************************
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Loading background graphics ************************
# background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
# background_rect = background.get_rect()

# #Loading game sound ************************
# in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
# in_game_song.set_volume(0.1)
# player = Player()
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
# # Run until the user asks to quit ************************
# running = True
# while running:

#     # Did the user click the window close button? ************************
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#                 break
#         elif event.type == QUIT:
#             running = False
#             break

#     #Get all the keys currently pressed ************************
#     pressed_keys = pygame.key.get_pressed()
#     # Update the player sprite based on keypresses ************************
#     player.update(pressed_keys)
#         # Fill the background with white ************************
#     screen.fill((0, 0, 0))
#     screen.blit(background, background_rect)
#     in_game_song.play()
#     # pygame.draw.line(screen,(0,255,255),(790,600),(790,300),(20)) ************************
#     # line(surface, color, start_pos(tuple[x,y]), end_pos(tuple[x,y]), width) ************************

#     # pygame.draw.line(screen,(0,255,255),(790,600),(0,0),(20)) ************************


#     for entity in all_sprites:
#         screen.blit(entity.surf, entity.rect)

#     surf = pygame.Surface((50,50))
#     surf.fill((255,33,127))

#     surf_center = (
#         (SCREEN_WIDTH-surf.get_width())/2,
#         (SCREEN_HEIGHT -surf.get_height())/2,
#     )

#     screen.blit(player.surf, player.rect)
#     # Flip the display ************************
#     pygame.display.flip()

# # Done! Time to quit. ************************
# pygame.quit()


# ************************ = already commented (don't uncomment)

# Simple pygame program ************************

# Import and initialize the pygame library ************************
import pygame
import random
from player_class import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
font_dir = path.join(path.dirname(__file__), 'font')

# pygame.mixer.pre_init(44100, -16, 1, 512) ************************
pygame.mixer.init(48000, -16, 1, 1024)

#Test text ****************************
test_text = "Hello World"

# Load all game graphics ************************

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

# Set up the drawing window ************************
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Loading background graphics ************************
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
background_rect = background.get_rect()

# try_text = pygame.font.Font(path.join(font_dir, "BlackOpsOne-Regular.ttf"), 115)

# font_name sets up generic text, just trying to get some shit on the screen so fuck the other font for right now **************************
# https://www.youtube.com/watch?v=U8yyrpuplwc&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=10 minute mark - 2:28 for tutorial on printing text
# font_name = pygame.font.match_font('arial')
# gameText = pygame.font.Font("BlackOpsOne-Regular.ttf",115)
# def draw_text(surf, text, size, x, y):
#     font = pygame.font.Font(gameText,size)
#     # Surface that python prints text onto "text is just whatever the text typed is"
#     text_surface = font.render(text, True, white)
#     # Rectangle of the text
#     text_rect = text_surface.get_rect()
#     # Set point on rectangle of the x,y coordinate plane on the screen
#     text_rect.midtop = (x,y)
#     # Blit or paste the text onto the screen (text_surface) at the location of the text (text_rect)
#     surf.blit(text_surface, text_rect)

# def game_intro():
#     intro = True
#     while intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         screen.fill(black)
#         font = pygame.font.Font('arial',115)

#Loading game sound ************************
in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
in_game_song.set_volume(0.1)
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Run until the user asks to quit ************************
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