#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl
from SurfScreen import*
import sys

'''
Define os dados iniciais do jogo e as constantes usadas. 

Define as variaveis que sao modificadas em um laço específico mas que precisa permanecer 
existindo em outros laços mantendo o valor alterado, até que outra alteração ocorra. 
Inicializa o contador de tempo. 
'''
class pygame_basics:
	def _pygame_basics(self):		
		pyg.init()
		#Criacao dos valores estáticos usados. 
		self.SurfScreen_abertura()
		self.SurfMalhaConstantes()	#Define a matriz da malha, guarda BIF da malha. 
		self.Ntetros = 8 	#Numero de tetrominos usados. Padrão é 7
		self.Nblocos = 7	#Numero de blocos em blocos.png
		self.Tetros()		#Cria os tetrominos, guardando-os em uma lista(matriz e superficie).
							#Tetrominos.py
		#self.PrintTetros()	#Impressao para teste. 
		self.flag = True
		self.flagVarredura = False	#Utilizado quando se inicia um tetromino para verificar colisao. 
		self.flagTrocaTetromino = False	#flag para trocar tetromino. 
		
		#Inicializacao do relogio:
		self.ControleInicialTempo()	#_pygame_basics()
		
		#Fontes usadas
		self.FontA15=pyg.font.SysFont("Arial", 15)		
		
		#Carregamento de imagens fixas
		BlocosCoresPath = "../Imagens/blocos.png"
		self.BlocosCores = pyg.image.load(BlocosCoresPath).convert()	
			#Uso em _Superficie_Blocos()
		
		#Controle de movimento dos tetrominos
		self.Rotacao = 0
		self.Posicao = 0
		self.Altura = 0
		self.FlagPosicaoInicial = True
		self.TetroAtual = 0
		self.TetroProximo = 0	#Tetromino impresso na superficie de dados que sucede o próximo.
		
		#Auxiliares de controladores 
		self.AuxAltura = self.Altura	#Serve para verificar se houve ou nao variacao de altura. 
		self.AuxRotacao = self.Rotacao	#Serve para verificar se houve ou nao colisao na rotacao
		self.AuxPosicao = self.Posicao
		self.AuxBase = 0				#Serve para determinar a base da matriz do tetromino.
										#Uso na colisao com a base.
	
	#Valores constantes aplicados às superficies.				
	def SurfScreen_abertura(self):
		self.Screen = pyg.display.set_mode((500,500),pyg.RESIZABLE, 32)
		self.ScreenAspectRatio = (16,9)	#Orienta no futuro as dimensoes. 
		self.SurfScreen()

		
	def ControleInicialTempo(self):
		self.clock = pyg.time.Clock()
		self.time_check = 0	#Verifica se passou 60 seg;
		self.TempoTotalSeg = 0
		self.TempoTotalMin = 0
		self.tick = self.clock.tick()

			
		
		
				
				
		
		
		


