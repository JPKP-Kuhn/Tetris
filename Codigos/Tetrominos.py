#coding:utf-8
import numpy as np
import pygame as pyg
import pygame.locals as pyl


def _mat_nula_4_4():
	mat=[None]*4	#Matriz 4x4 de termos nulos
	for i in range(4):
		mat[i]=[int]*4 
		for j in range(4):
			mat[i][j] = 0
	return mat		

'''
Melhor seria criaruma classe para o tetromino em que incluísse a matriz do tetromino e 
a base, que nada mais é do que a primeira linha nao nula da matriz. 
Evita que seja toda hora verificado na colisao com a matriz da malha. 
'''

class Tetromino: #Indica o tetromino e a rotacao que sofre.	
	'''
	Os tetrominos são indicados pelo tipo. 
	Cada Tetromino é elemento da lista 
	A rotação dos tetrominos segue o dicionario abaixo: 
	-3: -270^o
	-2: -180^o
	-1: -90^o
	 0:  0^o
	 1:  90^o
	 2:  180^o
	 3:  270^o		
	 
	 Todos os tetrominos devem começar na parte mais alta. 
	'''	
		
	
	def Tetros(self):
		self._Tetros = []
		self.Tetro1()				
		self.Tetro2()
		self.Tetro3()
		self.Tetro4()
		self.Tetro5()
		self.Tetro6()
		self.Tetro7()
		#self.Tetro8()				
		
	#Criação das matrizes dos tetrominos:	
	#Tetromino 8: Extra
	def Tetro8(self):
		Tetro = []	
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][1]=1
		Tetro1[1][0]=1
		Tetro1[1][2]=1
		Tetro1[2][1]=1
		Tetro.append(Tetro1)		
		self._Tetros.append(Tetro)

	#Tetromino 7: L - 4 rotacoes. 
	def Tetro7(self):
		Tetro = []	
		#Posicao 0
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[1][0]=1
		Tetro1[2][0]=1
		Tetro1[2][1]=1
		Tetro.append(Tetro1)
		#Posicao 1 - Rotacao 
		Tetro1 = _mat_nula_4_4()
		Tetro1[1][0]=1
		Tetro1[1][1]=1
		Tetro1[1][2]=1
		Tetro1[0][2]=1
		Tetro.append(Tetro1)
		#Posicao 2 - Rotacao
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[0][1]=1
		Tetro1[1][1]=1
		Tetro1[2][1]=1
		Tetro.append(Tetro1)
		#Posicao 3
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[1][0]=1
		Tetro.append(Tetro1)
		self._Tetros.append(Tetro)		
	
			
	#Tetromino 6: J
	def Tetro6(self):
		Tetro = []			
		#Posicao 0
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][1]=1
		Tetro1[1][1]=1
		Tetro1[2][1]=1
		Tetro1[2][0]=1
		Tetro.append(Tetro1)
		#Posicao 1 
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[0][1]=1
		Tetro1[0][2]=1
		Tetro1[1][2]=1
		Tetro.append(Tetro1)
		#Posicao 2
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[0][1]=1
		Tetro1[1][0]=1
		Tetro1[2][0]=1
		Tetro.append(Tetro1)
		#Posicao 3
		Tetro1 = _mat_nula_4_4()
		Tetro1[0][0]=1
		Tetro1[1][0]=1
		Tetro1[1][1]=1
		Tetro1[1][2]=1
		Tetro.append(Tetro1)
		self._Tetros.append(Tetro)	
		

		
	#Tetromino 5: 2 rotações
	def Tetro5(self):
		Tetro = []	
		#Posicao 0	
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][0] = 1
		Tetro1[0][1] = 1
		Tetro1[1][1] =1
		Tetro1[1][2] =1
		Tetro.append(Tetro1)
		#Posicao 1
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][1] = 1
		Tetro1[1][1] = 1
		Tetro1[1][0] = 1
		Tetro1[2][0] =1
		Tetro.append(Tetro1)		
		self._Tetros.append(Tetro)
		
	
	
	#Tetromino 4: #Quadrado
	def Tetro4(self):
		Tetro = []		
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][0] = 1
		Tetro1[0][1] = 1
		Tetro1[1][0] =1
		Tetro1[1][1] =1
		Tetro.append(Tetro1)
		self._Tetros.append(Tetro)	
	
		
	
	#Tetromino 3:		
	def Tetro3(self):
		Tetro = []		
		#Posicao 0:
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][1] = 1
		Tetro1[0][2] = 1
		Tetro1[1][0] =1
		Tetro1[1][1] =1
		Tetro.append(Tetro1)
		#Posicao 1
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][0] = 1
		Tetro1[1][0] = 1
		Tetro1[1][1] = 1
		Tetro1[2][1] =1
		Tetro.append(Tetro1)	
		self._Tetros.append(Tetro)
		
		
	
		
	#Tetromino 2:		
	def Tetro2(self):
		Tetro = []		
		#Posicao 0:
		Tetro1 = _mat_nula_4_4()		
		Tetro1[0][1] = 1#11
		Tetro1[1][1] = 1
		Tetro1[2][1] =1
		Tetro1[1][2] =1
		Tetro.append(Tetro1)
		#Posicao 1
		Tetro1 = _mat_nula_4_4()		
		Tetro1[2][1] = 1
		Tetro1[1][2] = 1
		Tetro1[1][0] = 1
		Tetro1[1][1] =1
		Tetro.append(Tetro1)
		#Posicao 2
		Tetro1 = _mat_nula_4_4()		
		Tetro1[1][1] = 1  #31
		Tetro1[0][1] = 1
		Tetro1[1][0] =1
		Tetro1[2][1] =1
		Tetro.append(Tetro1)
		#Posicao 3
		Tetro1 = _mat_nula_4_4()		
		Tetro1[1][0] = 1
		Tetro1[1][1] = 1
		Tetro1[1][2] = 1
		Tetro1[0][1] =1
		Tetro.append(Tetro1)	
		#Inserção dos tetrominos		
		self._Tetros.append(Tetro)
		
	#Tetromino 1. Formato I. Possui apenas 2 rotações. 		
	def Tetro1(self):
		Tetro = []				
		Tetro1 = _mat_nula_4_4()
		for i in range(4): 
			Tetro1[1][i] = 1
		Tetro.append(Tetro1)		
		Tetro2 = _mat_nula_4_4()
		for i in range(4): 
			Tetro2[i][1] = 1
		Tetro.append(Tetro2)			
		self._Tetros.append(Tetro)	
		



if __name__=="__main__": 
	A = Tetromino()
	
	
