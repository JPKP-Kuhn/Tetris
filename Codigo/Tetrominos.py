import pygame as pyg

import pygame as pyg


class Tetrominos():
    def _tetromino(self):
        #imagem
        self.bloco = "../Figuras/blocos.png"

        #Dados dos blocos
        self.bloco_largura, self.bloco_altura = 32, 32

        #Carregando a imagem
        self.Tetromino = pyg.image.load(self.bloco).convert_alpha()
        self.Tetromino = pyg.transform.scale(self.Tetromino,(self.bloco_largura*7,self.bloco_altura))
        self.bloco_rect = self.Tetromino.get_rect() #retângulo junto com a imagem

        #blit juntamente com o Retângulo
        self.ModoTela.blit(self.Tetromino, (220,0), self.bloco_rect)

    def _movimento(self):
        self.ModoTela.blit(self.Tetromino, (220,self.y) , self.bloco_rect)
        if self.y != 670:
            self.y += 1
            if self.y == 670:
                self.ModoTela.blit(self.Tetromino, (220,self.y) , self.bloco_rect)
                self._colisao()
        

    def _colisao(self):
        if self.y == 670:
            self.y2 = 0
            self.ModoTela.blit(self.Tetromino, (220,self.y2) , self.bloco_rect)
