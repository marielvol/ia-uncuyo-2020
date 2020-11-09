import random
import copy
import math
import time

#Función objetivo: contabiliza la cantidad de pares de reinas amenazadas para un tablero (state)
def calculateObjective(state):
  cont = 0
  for i in range(0,N):
    for j in range(i+1,N):
      if state[j]==state[i]:
        cont += 1
      if state[j]+j==state[i]+i or state[j]-j==state[i]-i:
        cont += 1
  return cont

#Devuelve un estado vecino aleatorio
def getRandomNeighbour(state):
  newState = copy.deepcopy(state)
  a = random.randint(0,N-1)
  b = random.randint(0,N-1)
  newState[a]=b
  while newState[a] == state[a]:
    b = random.randint(0,N-1)
    newState[a]=b
  return newState

#Algoritmo Simulated Annealing
def simulatedAnnealing(state):
  alpha = 0.01
  T = 1
  cont = 0
  current = state
  while T > 0 and calculateObjective(current)!=0:
    neighbour = getRandomNeighbour(current)
    delta_e = calculateObjective(current)-calculateObjective(neighbour)
    if (delta_e > 0) or (random.uniform(0,1) < math.exp(delta_e / T)):
      current = neighbour
    T -= alpha
    cont += 1
  return (current,calculateObjective(current),cont)


if __name__ == '__main__':
  start_time=time.time()

  #Cantidad de reinas
  N=8

  state1 = [random.randint(0,N-1) for i in range(0,N)]
  print("Estado inicial: ",state1)

  (solutionState,solutionValue,steps)=simulatedAnnealing(state1)
  print("Estado solución Simulated Annealing: ",solutionState,"\n","Cantidad de reinas amenazadas: ",solutionValue,"\n","Cantidad de pasos para llegar al objetivo: ",steps)

  end_time=time.time()

  ejec_time = end_time - start_time
  print("Tiempo de ejecución: ",ejec_time)
