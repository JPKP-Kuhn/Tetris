import pygame as pyg
from pygame.locals import *
from sys import *
from PygameBasics import *
from Tetrominos import *

class PygameCtrl(PygameBasics, Tetrominos):
    def __init__(self):
        #Coordenadas para movimento
        self.y = 0

        self._pygame_basic() #Carregamento inicial
        self._tetromino()
        self._pygame_loop()  #Atualiza frame a frame


    def _pygame_loop(self):
        while True:
            self.ModoTela.fill(self.CorFundo)
            for event in pyg.event.get():
                if event.type == QUIT:
                    pyg.quit()
                    exit()
            
            self._movimento()
            self._colisao()
            pyg.display.flip()
            self.clock.tick(100)
            pyg.display.update()
