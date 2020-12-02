

## Árboles de decisión

Un árbol de decisión es un método de aprendizaje supervisado para el reconocimiento y clasificación de patrones que permite crear un modelo para predecir el valor de una variable/atributo mediante el aprendizaje de reglas de decisión derivadas de las características de los datos.

Hay dos tipos básicos de árboles de decisión:

 - De clasificación
 - De regresión

| Tipo | Árboles de clasificación | Árboles de regresión |
|--|--|--|
| Variable dependiente | Categórica | Continua |
| Decisión de ramificación | Índice Gini - Chi cuadrado - Ganancia de información | Reducción en la varianza |
| Tipos de preguntas | ¿Es x perteneciente a C? (C es cualquier subconjunto {y1,y2,…,yn}) | ¿Es x <= r? (r perteneciente a R) |
| Valores de los nodos terminales | Se reducen a la moda de las observaciones del conjunto de entrenamiento que han “caído” en esa región | Se reducen a la media de las observaciones en esa región |


