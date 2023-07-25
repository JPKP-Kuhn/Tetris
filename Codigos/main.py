#coding:utf-8
import sys
import pygame as pyg
import pygame.locals as pyl
from SurfScreen import*
from SurfMalha import*
from SurfDados import*
from pygame_basics import *
from Tetrominos import*
from SurfTetrominos import*

class MemoTetris(SurfScreen, SurfMalha, SurfDados, pygame_basics, Tetromino, SurfTetrominos):
	def __init__(self):
		self.ticks = 0
		self._pygame_basics()
		self._pygame_loop()
			
	
	def _pygame_loop(self): 
		while True: 
			for event in pyg.event.get():
				if event.type ==pyl.QUIT:
					pyg.quit(); sys.exit(1)
				
				if event.type==pyl.KEYDOWN: 
					if event.key==pyl.K_ESCAPE:
						pyg.quit(), 
						sys.exit()
					#Processos de rotacao		
					if event.key==pyl.K_UP:
						self.Rotacao-=1
					if event.key==pyl.K_DOWN:
						self.Rotacao+=1
					if event.key==pyl.K_LEFT:
						self.Posicao-=1
					if event.key==pyl.K_RIGHT:
						self.Posicao+=1		
					if event.key==pyl.K_SPACE:
						self.Altura+=1
					if event.key==pyl.K_t:	#Somente para testes. A mudança de tetromino
						self.TetroAtual+=1	#ocorre quando um tetromino pára de descer.
					if event.key==pyl.K_m:
						print("Tetromino ", self.TetroAtual%7, " rotacao:", self.Rotacao%7-3)
							
			self.Screen.fill((0,0,50))
			self.SurfScreen()		#SurfScreen.py
			self.SurfMalha()		#SurfMalha.py 
			self.SurfDados()		#SurfDados.py 		
			self.Screen.blit(self.Malha, self.MalhaPos)
			self.Screen.blit(self.Dados, (10,30))
			pyg.display.update()	

if __name__=="__main__": 
	MemoTetris()

