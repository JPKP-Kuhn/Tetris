#coding:utf-8
import pygame as pyg
import pygame.locals as pyl

class SurfDados():
	def ControleTempo(self):
		self.tick =  self.clock.tick()
		self.time_check += self.tick		
		self.TempoTotalSeg = int(self.time_check/1000.)	
		if (self.time_check>=(60*1000)): #1 minuto passado
			self.time_check = 0
			self.TempoTotalSeg = 0
			self.TempoTotalMin+=1

	def SurfDadosRetRelogio(self):
		RetanguloRelogio = pyg.Rect((self.Dados.get_width()*0.1,self.Dados.get_height()*0.05),(self.Dados.get_width()*0.8,self.Screen.get_height()*0.12))
		self.RetanguloRelogio = pyg.draw.rect(self.Dados,(255,255,255), RetanguloRelogio )
		momento = "Tempo de uso: {0:02d}:{1:02d}".format(self.TempoTotalMin,self.TempoTotalSeg )
		momento = self.FontA15.render(momento, True, (0,0,0))
		x, y, w, h = self.RetanguloRelogio		
		self.Dados.blit(momento, (x*(1.2),y*1.2))
		
	def SurfDados(self):
		self.Dados = pyg.Surface([self.Screen.get_width()/2.5, self.Screen.get_height()*0.9])
		self.Dados= self.Dados.convert_alpha()
		self.Dados.fill((0,0,0,0)) 	#Deixa transparente a superficie. 
		self.ControleTempo()		#SurfDados.py
		self.SurfDadosRetRelogio()	#SurfDados.py


		
		
		
		


	
	
		
