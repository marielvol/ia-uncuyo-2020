import random
import numpy as np

class Mapa:
  def __init__ (self,sizeX,sizeY,obs_rate):
    #Número de filas
    self.fil = sizeX
    #Número de columnas
    self.col = sizeY
    #Coordenadas punto inicio
    self.init_posX = pos_init[0]
    self.init_posY = pos_init[1]
    #Coordenadas punto destino
    self.fin_posX = pos_fin[0]
    self.fin_posY = pos_fin[1]
    #Tamaño de la matriz
    tamaño = sizeX*sizeY
    #Cantidad de obstáculos
    self.obsSlotsAmount = (obs_rate * tamaño)/100
    #Creo la matriz donde:
    #0=camino libre
    #1=camino obstruido
    #2=punto inicio
    #3=punto destino
    self.matriz = np.zeros((sizeX,sizeY))
    self.matriz[self.init_posX][self.init_posY] = 2
    self.matriz[self.fin_posX][self.fin_posY] = 3
    i = 0
    while (i < self.obsSlotsAmount):
      slotX = random.randint(0,self.fil-1)
      slotY = random.randint(0,self.col-1)
      if (self.matriz[slotX][slotY] == 0):
        self.matriz[slotX][slotY] = 1
        i = i + 1

  #Función que muestra la matriz
  def print_environment(self):
        for a in range(0,self.fil):
            for b in range(0,self.col):
                print("|",int(self.matriz[a][b]),end=' ')
            print("|")

class Nodo:
	def __init__(self, pos=[0, 0], padre=None):
		self.pos = pos
		self.padre = padre
		self.h = distancia(self.pos, pos_fin)
		if self.padre == None:
			self.g = 0
		else:
			self.g = self.padre.g + 1
		self.f = self.g + self.h

#Función que calcula la distancia entre dos puntos en valor absoluto
def distancia(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

class AEstrella:
	def __init__(self, mapa):
		self.mapa = mapa
		#Nodos de inicio y fin
		self.inicio = Nodo([self.mapa.init_posX,self.mapa.init_posY])
		self.fin = Nodo([self.mapa.fin_posX,self.mapa.fin_posY])
		#Creo las listas abierta y cerrada
		self.abierta = []
		self.cerrada = []
		#Añado el nodo inicial a la lista cerrada
		self.cerrada.append(self.inicio)
		#Añado vecinos a la lista abierta
		self.abierta += self.vecinos(self.inicio)
		#Busco mientras el objetivo no esté en la lista cerrada y haya un camino posible
		while self.objetivo():
			if self.buscar()==False:
				self.camino=[]
				print("No hay camino posible")
				break
		#Armo el camino
		if self.objetivo()==0:
			self.camino = self.camino()
	
	#Función que devuelve una lista con los nodos vecinos transitables
	def vecinos(self, nodo):
		vecinos = []
		if (nodo.pos[0]+1)<self.mapa.fil:
			if self.mapa.matriz[nodo.pos[0]+1][nodo.pos[1]] != 1:
				vecinos.append(Nodo([nodo.pos[0]+1, nodo.pos[1]], nodo))
		if (nodo.pos[0]-1)>=0:
			if self.mapa.matriz[nodo.pos[0]-1][nodo.pos[1]] != 1:
				vecinos.append(Nodo([nodo.pos[0]-1, nodo.pos[1]], nodo))
		if (nodo.pos[1]-1)>=0:
			if self.mapa.matriz[nodo.pos[0]][nodo.pos[1]-1] != 1:
				vecinos.append(Nodo([nodo.pos[0], nodo.pos[1]-1], nodo))
		if (nodo.pos[1]+1)<self.mapa.col:
			if self.mapa.matriz[nodo.pos[0]][nodo.pos[1]+1] != 1:
				vecinos.append(Nodo([nodo.pos[0], nodo.pos[1]+1], nodo))
		return vecinos
	
	#Función que pasa el elemento de menor costo "f" de la lista abierta a la cerrada
	def f_menor(self):
		if self.abierta != []:
			a = self.abierta[0]
			n = 0
			for i in range(1, len(self.abierta)):
				if self.abierta[i].f < a.f:
					a = self.abierta[i]
					n = i
			self.cerrada.append(self.abierta[n])
			del self.abierta[n]
			return True
		else:
			return False
	
	#Función que comprueba si un nodo está en una lista	
	def en_lista(self, nodo, lista):
		for i in range(len(lista)):
			if nodo.pos == lista[i].pos:
				return 1
		return 0
	
	#Función que gestiona los vecinos del nodo seleccionado	
	def ruta(self):
		for i in range(len(self.nodos)):
			if self.en_lista(self.nodos[i], self.cerrada):
				continue
			elif not self.en_lista(self.nodos[i], self.abierta):
				self.abierta.append(self.nodos[i])
			else:
				if self.select.g+1 < self.nodos[i].g:
					for j in range(len(self.abierta)):
						if self.nodos[i].pos == self.abierta[j].pos:
							del self.abierta[j]
							self.abierta.append(self.nodos[i])
							break
	
	#Función que analiza el último elemento de la lista cerrada
	def buscar(self):
		if self.f_menor()==True:
			self.select = self.cerrada[-1]
			self.nodos = self.vecinos(self.select)
			self.ruta()
			return True
		else:
			return False
	
	#Funución que comprueba si el objetivo está en la lista abierta
	def objetivo(self):
		for i in range(len(self.abierta)):
			if self.fin.pos == self.abierta[i].pos:
				return 0
		return 1
	
	#Función que retorna una lista con las posiciones del camino a seguir
	def camino(self):
		for i in range(len(self.abierta)):
			if self.fin.pos == self.abierta[i].pos:
				objetivo = self.abierta[i]
				
		camino = []
		while objetivo.padre != None:
			camino.append(objetivo.pos)
			objetivo = objetivo.padre
		camino.reverse()
		return camino

if __name__ == '__main__':
  globals()["pos_init"]=[1,2]
  globals()["pos_fin"]=[9,8]
  mapa = Mapa(10,10,30)
  print("Mapa:")
  mapa.print_environment()
  A = AEstrella(mapa)
  print("Camino:")
  print(A.camino)