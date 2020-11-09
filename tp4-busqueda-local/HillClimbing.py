import random
import copy
import time

#Busca todos los estados vecinos de un tablero dado y devuelve el óptimo
def getNeighbour(state):
  optState = copy.deepcopy(state)
  optValue = calculateObjective(optState)
  NeighbourState = copy.deepcopy(optState)
  NeighbourValue = calculateObjective(NeighbourState)

  for i in range(0,N):
    for j in range(0,N):
      if (j != state[i]):
        NeighbourState[i] = j
        NeighbourValue = calculateObjective(NeighbourState)
        if NeighbourValue <= optValue:
          optValue = NeighbourValue
          optState = copy.deepcopy(NeighbourState)
        NeighbourState[i] = state[i]
  return optState

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

#Algoritmo Hill Climbing
def hillClimbing(state):
  cont = 0
  max_steps = 10
  current = state
  currentValue = calculateObjective(current)
  while (cont<=max_steps):
    neighbour = getNeighbour(current)
    neighbourValue = calculateObjective(neighbour)
    if neighbourValue < currentValue:
      current = neighbour
      currentValue = neighbourValue
      cont += 1
    else:
      return (current,currentValue,cont)

if __name__ == '__main__':
  start_time=time.time()

  #Cantidad de reinas
  N=8

  state1 = [random.randint(0,N-1) for i in range(0,N)]
  print("Estado inicial: ",state1)

  (solutionState,solutionValue,steps)=hillClimbing(state1)
  print("Estado solución Hill Climbing: ",solutionState,"\n","Cantidad de reinas amenazadas: ",solutionValue,"\n","Cantidad de pasos para llegar al objetivo: ",steps)

  end_time=time.time()

  ejec_time = end_time - start_time
  print("Tiempo de ejecución: ",ejec_time)
