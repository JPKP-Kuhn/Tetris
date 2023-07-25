#coding:utf-8
import pygame as pyg
import pygame.locals as pyl
import sys


'''
Cria as superficies individuais de cada tetromino. 
self.SurfBlocos = [] é uma lista de cada um dos retângulos que formam os tetrominos.
self.Trama é uma tupla com a dimensão da trama (cada quadradinho) da malha. 
O método pega cada retângulo e altera as dimensoes para o tamanho da trama e faz o blit em SurfBlocos
'''

class SurfTetrominos():
	
	
	def _Superficies_Blocos(self):
		#Guarda as superficies para cada bloco individual. 
		#Esta funcao está com erro, ao alterar o tamanho da tela sucessivas vezes o bloco nao se atualiza.
		self.SurfBlocos = []	#Superficies individuais dos blocos.
		#Carrega as imagens, salva nas superficies. 
		self.BlocosCores = pyg.transform.scale(self.BlocosCores, (self.Trama[0]*7, self.Trama[1]) )
			#self.BlocosCores definido em _pygame_basics()
			#Em blocos.png há 7 quadrados. 
			#self.Trama definida em SurfMalha.py
		#Criação das superficies dos blocos
		
		for i in range(self.Nblocos ):	#São 7 blocos de cores diferentes. 
			self.SurfBlocos.append(pyg.Surface((self.Trama[0], self.Trama[1]))) #Tamanho da superficie.			
			RetBloco = pyg.Rect((i*self.Trama[0],0),self.Trama)					
			self.SurfBlocos[i].blit(self.BlocosCores, (0,0),RetBloco)	#Faz o blit do retangulo. 		

	
	
	def _Superficies_Tetrominos(self): 		
		self.SurfTetro = []	#Lista das superficies dos tetrominos. Posicao 0: tetromino, posicao 1:rotacao.  
		self.SurfTetroBase = pyg.Surface((self.Trama[0]*4,self.Trama[1]*4))#Cria superficie 4x4 blocos
		self.SurfTetroBase=self.SurfTetroBase.convert_alpha()	#Torna transparente a superficie. 
		self.SurfTetroBase.fill((0,0,0,0))#Deixa a superficie transparente, com alpha = 0	
		for i in range(len(self._Tetros)):	#Passa por todos os tetrominos.

			PadroesRotacaoTetromino = []	#Guarda as superficies i com as rotacoes j. 			
			for j in range(len(self._Tetros[i])):	#Passa por cada rotacao do tetromino i. 
													#Cada membro é uma matriz 4x4				
				Stetro = pyg.Surface.copy(self.SurfTetroBase)
				TempMat = self._Tetros[i][j]	#Matriz temporaria. 								
				for k in range(4):	#Varre a linha da matriz que guarda a sup i com a rot j
					for l in range(4):
						if TempMat[l][k]==1:							
							Stetro.blit(self.SurfBlocos[i],(self.Trama[0]*k, self.Trama[1]*l))			
				PadroesRotacaoTetromino.append(Stetro)
			self.SurfTetro.append(PadroesRotacaoTetromino)

		n = len(self.SurfTetro)	#Quantidade de tetrominos em uso.
		self.tetro_em_uso = self.TetroAtual%n
								#Permite diferente quantidades de tetrominos 
								#self.TetroAtual definido em _pygame_basics()				
								#Definido em _Superficies_Tetrominos(), SurfTetrominos.py			
					
