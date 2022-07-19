import pygame.mixer
from pygame import *


pygame.mixer.init()
pygame.init()
size = (966, 658)
screen = display.set_mode(size)
ARIAL_50 = font.SysFont('arial', 50)

pygame.mixer.music.load("sound/Pixel_sound.mp3")
pygame.mixer.music.play(-1)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()


    def draw(self, surf, x, y, _option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * _option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)


menu = Menu()
menu.append_option("Start game", lambda: print("You plaing"))
menu.append_option("Score", lambda: print("You lock score"))
menu.append_option('Quit', quit)

runing = True
while runing:
    for e in event.get():
        if e.type == QUIT:
            runing = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                menu.switch(-1)
            elif e.key == K_DOWN:
                menu.switch(1)
            elif e.key == K_SPACE:
                menu.select()


    screen.fill((0, 0, 0))

    menu.draw(screen, 100, 100, 75)

    display.flip()
quit()