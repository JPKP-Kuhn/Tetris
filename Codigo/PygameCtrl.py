import pygame as pyg
from pygame.locals import *
from sys import *
from PygameBasics import *
from Tetrominos import *

class PygameCtrl(PygameBasics, Tetrominos):
    def __init__(self):
        self._pygame_basic() #Carregamento inicial
        self._tetromino()
        self._pygame_loop()  #Atualiza frame a frame


    def _pygame_loop(self):
        while True:
            for event in pyg.event.get():
                if event.type == QUIT:
                    pyg.quit()
                    exit()
                    
            pyg.display.flip()
            self.clock.tick(60)
            pyg.display.update()
