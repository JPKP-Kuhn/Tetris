import pygame as pyg

class PygameBasics():
    def _pygame_basic(self):
        pyg.init() #Inicialização

        self.clock=pyg.time.Clock() #Controle de tempo

        #Informações da tela
        self._TamTela=(640, 760)
        self.CorFundo = (220,220,220)
        self.ModoTela=pyg.display.set_mode(self._TamTela)

        #Imagens do jogo
        self.BIF="../Figuras/back2.jpeg"
        self.Screen = pyg.display.set_mode(self._TamTela) #Tela principal

        self.PlanoFundo = pyg.image.load(self.BIF).convert_alpha()
        self.PlanoFundo = pyg.transform.scale(self.PlanoFundo, self.ModoTela.get_size())
        self.ModoTela.blit(self.PlanoFundo, (0,0))
        self.TelaFundo = pyg.Surface((self.ModoTela.get_width(),self.ModoTela.get_height()))

        pyg.display.set_caption("Tetris") #Título
