import random
import copy
import time

#Mutación
def mutate(Pob):
  Pmedia = []
  for i in range(0,len(Pob)):
    State=mutate2(Pob[i])
    Pmedia.append(State)
  return Pmedia

def mutate2(state):
  newState = copy.deepcopy(state)
  a = random.randint(0,N-1)
  b = random.randint(0,N-1)
  newState[a]=b
  while newState[a] == state[a]:
    b = random.randint(0,N-1)
    newState[a]=b
  return newState

#Cruzamiento en 1 punto aleatorio
def crossover(Pob):
  Pmedia = []
  for i in range(0,len(Pob),2):
    x = random.randint(1,N-1)
    (State1,State2)=crossover2(Pob[i],Pob[i+1],x)
    Pmedia.append(State1)
    Pmedia.append(State2)
  return Pmedia

def crossover2(state1,state2,x):
  newState1 = copy.deepcopy(state1)
  newState2 = copy.deepcopy(state2)
  for i in range(x,N):
    newState1[i] = state2[i]
    newState2[i] = state1[i]
  return (newState1,newState2)

#Selección por torneo: se eligen k soluciones al azar y se selecciona aquella con mayor valor de fitness.
def select(Pob,Fit):
  Pmedia = []
  k = 4
  for i in range(0,len(Pob)):
    n = random.randint(0,len(Pob)-1)
    best = Pob[n]
    bestFit = Fit[n]
    for j in range(0,k):
      n = random.randint(0,len(Pob)-1)
      if Fit[n] >= bestFit:
        bestFit = Fit[n]
        best = Pob[n]
    Pmedia.append(best)
  return Pmedia

#Función de Fitness: calcula la función objetivo para cada individuo de la población
def calculateFitness(Pob):
  Fit = []
  for i in range(0,len(Pob)):
    Fit.append(calculateObjective(Pob[i]))
  return Fit

#Función objetivo: contabiliza la cantidad de pares de reinas que NO se amenazan para un tablero (state)
def calculateObjective(state):
  maxAttack = (N*(N-1))/2
  cont = 0
  for i in range(0,N):
    for j in range(i+1,N):
      if state[j]==state[i]:
        cont += 1
      if state[j]+j==state[i]+i or state[j]-j==state[i]-i:
        cont += 1
  return (maxAttack - cont)

#Inicialización de la población
def initializePob():
  Pob = []
  for i in range(0,2**N):
    Ind = [random.randint(0,N-1) for i in range(0,N)]
    Pob.append(Ind)
  return Pob

#Algoritmo genético
def geneticAlgorithm():
  cont = 0
  t = 0
  max_steps = 10
  maxAttack = (N*(N-1))/2
  P = initializePob()
  F = calculateFitness(P)
  while t < max_steps and max(F)!=maxAttack:
    S = select(P,F)
    P_media = crossover(S)
    P = mutate(P_media)
    F = calculateFitness(P)
    t += 1
    cont += 1
  i = F.index(max(F))
  return (P[i],maxAttack-F[i],cont)

if __name__ == '__main__':
  start_time=time.time()

  #Cantidad de reinas
  N=8

  (solutionState,solutionValue,steps)=geneticAlgorithm()
  print("Estado solución Genetic Algorithm: ",solutionState,"\n","Cantidad de reinas amenazadas: ",solutionValue,"\n","Cantidad de pasos para llegar al objetivo: ",steps)

  end_time=time.time()

  ejec_time = end_time - start_time
  print("Tiempo de ejecución: ",ejec_time)