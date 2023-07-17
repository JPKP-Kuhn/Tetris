#coding:utf-8
import pygame as pyg
import pygame.locals as pyl
import numpy as np
import sys

class Vassoura:	#Sem uso por enquanto
	flagEsq = False
	flatDir = False
	flagBaixo = False
	
class SurfMalha():
	#Dados estaticos
	def SurfMalhaConstantes(self):	#Define a matriz da malha, guarda BIF
		self.LinhasMalha= 20
		self.ColunasMalha = 10
		self.MalhaMatriz = []
		for i in range(self.LinhasMalha): 
			linha = []
			for j in range(self.ColunasMalha):
				linha.append(0)
			self.MalhaMatriz.append(linha)	
		self.MalhaMatriz[16][7]=2	
		self.BIF = '../Imagens/malha_quadriculada.png'
		
	
	#Dados Dinamicos
	def SurfMalha(self):		
		MalhaDim = [self.ScreenDim[0]/2, self.ScreenDim[1]*0.9]
		borda = self.ScreenDim[1]*0.05 
			#Borda tirada do eixo y, tem o objetivo de tirar a borda da malha. 	
		self.MalhaPos=(self.ScreenDim[0]/2-borda,borda)
		self.Malha = pyg.Surface(MalhaDim)
		self.Trama = (self.Malha.get_width()/10, self.Malha.get_height()/20)
			#Tamanho da trama (quadrado que guarda o bloco individual).				
		self.MalhaBIF = pyg.image.load(self.BIF).convert_alpha()
		self.MalhaBIF = pyg.transform.scale(self.MalhaBIF, MalhaDim)
		self.Malha.blit(self.MalhaBIF, (0,0))
		if self.FlagPosicaoInicial:	#Coloca saida inicial na metade da primeira linha da malha. 
								#Definicao em pygame_basics
			self.Posicao = self.ColunasMalha//2-1	#Posiciona tetramino inicial no meio. 
			self.FlagPosicaoInicial=False			

		self._Superficies_Blocos()	#SurfTetrominos.py
			#Em cada nova redimensionamento deve-se construir a superficie de cada bloquinho. 				
		#self._Teste_Blit_Blocos()	#Blit de teste dos tetrominos.
		
		self._Superficies_Tetrominos()	#Requer os blocos já montados em _Superficies_Blocos(self)			
										#_Superficies_Tetrominos() definido em SurfTetrominos.py		
		#self._Teste_blit_Tetrominos()	#Imprime os tetrominos com e suas rotacoes. 
		self._Blit_Tetrominos()

	def ImprimeMatrizMalha(self):
		for i in range(len(self.MalhaMatriz)):
			print(self.MalhaMatriz[i])

	
	def _Blit_Tetrominos(self):	
		colisao =self.DetectaColisao()
		if (colisao ==1):	#Colisao com a base da matriz. 	
			#Atualizacao da matriz da malha. 
			self.TetroAtual += 1
			print(self.Posicao, self.Altura)
			for i59 in range(4): #Atualiza a matriz da malha. Tem que fazer o blit da matriz da malha.
				for j60 in range(4):
					if self.TempMat[i59][j60]==1: 
						self.MalhaMatriz[i59+self.Altura][j60+self.Posicao]= (self.tetro_em_uso+1) 
						#Tinha iniciado os tetro em uso com zero. Aqui perde-se o sentido. 
						
			
			self.ImprimeMatrizMalha()
		else:  	
			self.Malha.blit(self.SurfTetro[self.tetro_em_uso][self.Rotacao%len(self._Tetros[self.tetro_em_uso])], (self.Posicao*self.Trama[0], self.Altura*self.Trama[1]))
			#Blit da malha. self.Malha.blit....
		for i in range(len(self.MalhaMatriz)):
			for j in range(len(self.MalhaMatriz[i])):
				if(self.MalhaMatriz[i][j]!=0):
					self.Malha.blit(self.SurfBlocos[self.MalhaMatriz[i][j]],(j*self.Trama[0],i*self.Trama[1]) )
					#print(self.MalhaMatriz[i][j], i, j)
					
					
			
#		for i in range(self.Nblocos):
#			self.Malha.blit(self.SurfBlocos[i],(i*self.Trama[0],i*self.Trama[1]) )



	def DetectaColisaoBordaLateral(self): 
		#Verifica colisao com o limite lateral da malha.
		self.TempMat = self._Tetros[self.tetro_em_uso][self.Rotacao%len(self._Tetros[self.tetro_em_uso])]
		ExtEsq = 4	#Define valores impossíveis para extrema esquerda e extrema direita. 
		ExtDir = -4
		for i in range(len(self.TempMat)):
			for j in range(len(self.TempMat[i])):
				if (self.TempMat[i][j]==1): 
					if (ExtDir < j):
						ExtDir=j
					if (ExtEsq>j):
						ExtEsq=j		
		if self.Posicao<=ExtEsq:	#Posicao maxima a esquerda é -ExtEsq
			self.Posicao=ExtEsq
			print("Houve Colisao a esquerda")			
		if self.Posicao>=9-ExtDir:	#Posicao maxima à direita é 10	
			self.Posicao=9-ExtDir	
			print("Houve Colisao a direita")
			
	def DetectaColisaoMatriz(self):
		self.TempMat = self._Tetros[self.tetro_em_uso][self.Rotacao%len(self._Tetros[self.tetro_em_uso])]
		self.base = 0 #Base de self.TempMat (superficie do tetramino)
		#Esta conta está sendo feita várias vezes, so precisa uma, fazer classe tetromino com self.base na classe (sem o self).
		for i in range(len(self.TempMat)):
			for j in range(len(self.TempMat[i])):
				if (self.TempMat[i][j]==1): 
					if i>self.base:
						self.base = i
		#Faz a varredura sob a matriz da malha. 				
						
						
		
	def DetectaColisaoBase(self):
		self.TempMat = self._Tetros[self.tetro_em_uso][self.Rotacao%len(self._Tetros[self.tetro_em_uso])]
		self.base = 0 #Base de self.TempMat (superficie do tetramino)
		topo = 4		
		for i in range(len(self.TempMat)):
			for j in range(len(self.TempMat[i])):
				if (self.TempMat[i][j]==1): 
					if i>self.base:
						self.base = i
					if i<topo:
						topo = i
		if (self.Altura+self.base)>=(self.LinhasMalha-1):
			self.Altura =self.LinhasMalha-self.base-1
			print("Houve Colisao com a base")
			print("ALtura = ", self.Altura, ", posicao = ", self.Posicao, " Tetro = ", self.tetro_em_uso)
			return True #Houve Colisao
		else:
			return False #Não houve colisao. 			
	
	def DetectaColisaoRotacao(self): #Testar com tetromino piramide no canto da base. 
		return False

	def DetectaColisao(self):
		flagColisao = False
		#Verifica colisao com a lateral da matriz
		if (self.AuxPosicao!=self.Posicao):			
			self.DetectaColisaoBordaLateral()
			self.AuxPosicao = self.Posicao
		
		self.DetectaColisaoMatriz()	
			
		#Verifica colisao com a base da matriz. 
		if (self.AuxAltura!=self.Altura):			
			if self.DetectaColisaoBase(): 
				flagColisao =1
			self.AuxAltura=self.Altura
		#Verifica colisao na rotacao
		if(self.AuxRotacao!=self.Rotacao):
			if self.DetectaColisaoRotacao(): 
				flagRotacao = 2			
			self.AuxRotacao=self.Rotacao	
			self.AuxPosicao = self.Posicao-1	#Força a verificacao da posicao. 		
		if(self.MalhaMatriz[(self.AuxAltura+self.base+1)][7] != 0):
			flagColisao = 1
			print('contato')
		return flagColisao #Nao houve colisao. 
		


	#Rotinas de teste. 
	#Se os blocos estão corretos deverá aparecer em diagonal os retangulos. 		
	'''
	def _Teste_Blit_Blocos(self):
		for i in range(self.Nblocos):
			self.Malha.blit(self.SurfBlocos[i],(i*self.Trama[0],i*self.Trama[1]) )
	
	def _Teste_blit_Tetrominos(self):
		n = len(self.SurfTetro)	#Quantidade de tetrominos em uso.
								#Definido em _Superficies_Tetrominos(), SurfTetrominos.py
		tetro_em_uso = self.TetroAtual%n #Permite diferente quantidades de tetrominos 
								#self.TetroAtual definido em _pygame_basics()
		#Verifica choque com a parede.		
		self.Malha.blit(self.SurfTetro[tetro_em_uso][self.Rotacao%len(self._Tetros[tetro_em_uso])], (self.Posicao*self.Trama[0], 0*self.Trama[1])) 
	'''

