**Problema**

El problema consiste en implementar un agente basados en objetivos que dado un punto de inicio y un punto destino, este encuentre el camino óptimo.

**Enfoque**

Para resolver el problema he planteado 3 clases:

 - _Mapa_: Esta clase genera el ambiente del problema, donde el punto de inicio, el punto destino, el tamaño de la matriz y el porcentaje de obstáculos son definidos por el usuario. Una vez definidos estos parámetros, el ambiente se genera colocando los obstáculos de manera aleatoria. El mapa está representado por una matriz en la cual: el “0” corresponde a camino libre, el “1” a los lugares donde hay obstáculos, el “2” a la posición inicial y el “3” a la posición de destino.

 - _Nodo_: Esta clase asocia a cada posición que se quiere evaluar su nodo padre (para poder recordar de donde viene) y los valores de las funciones f, g y h donde h(n) es el costo estimado del nodo n al nodo objetivo, g(n) es el costo acumulado hasta el momento para llegar al nodo n y f(n) es la suma de ambos, es decir, el costo estimado total para llegar al nodo objetivo a través del nodo n.

 - _AEstrella_: Esta es la clase que lleva a cabo el algoritmo A* en sí. Lo que hace es dados un punto inicial y un punto destino, crear dos listas (abierta y cerrada) e incluir el nodo de inicio en la lista cerrada. Una vez hecho esto, se comienza por buscar los vecinos de ese nodo y aquellos que sean transitables se incluyen en la lista abierta. Mientras el objetivo no esté en la lista, se selecciona el nodo de menor costo de acuerdo a la función f(n) detallada anteriormente y nos movemos a ese lugar. El proceso se repite construyendo el camino hasta finalmente llegar al nodo objetivo (siempre que sea posible).

**Heurística**

La heurística que utilicé es el cálculo de la distancia entre dos puntos en valor absoluto: h = |Xinicial – Xfinal| + |Yinicial – Yfinal|

Esta heurística calcula la distancia desde el nodo actual hasta el nodo objetivo como si nos moviéramos en forma de “L”, es decir, trasladándose vertical y horizontalmente girando solo una vez, por esto es una heurística admisible y consistente, ya que nunca va a sobre estimar el costo real restante para llegar al objetivo porque es una relajación del problema que no tiene en cuenta los obstáculos.
