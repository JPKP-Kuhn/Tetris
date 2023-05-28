import pygame as pyg


class Tetrominos():
    def _tetromino(self):
        #imagem
        self.bloco = "../Figuras/blocos.png"

        #Dados dos blocos
        self.bloco_largura, self.bloco_altura = 32, 32

        self.Tetromino = pyg.image.load(self.bloco).convert_alpha()
        self.Tetromino=pyg.transform.scale(self.Tetromino,(self.bloco_largura*7,self.bloco_altura))
        self.ModoTela.blit(self.Tetromino,(220, 0))
