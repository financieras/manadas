# Juego de las Manadas

El juego de las manadas en Python con programación orientada a objetos.

## Normas
1. Se juega en un tablero cuadrado, por ejemplo de 10x10 casillas
2. Puede haber varios jugadores, mínimo dos jugadores y máximo 26 jugadores, que se denominan por las letras mayúsculas del alfabetoson A y B, llamados:
   * A: manada A
   * B: manada B
3. Los jugadores van moviéndose por el tablero alternando sus tiradas, primero la Manada A y luego la Manada B y así sucesivamente
4. En cada tirada cada manada puede moverse en cruz, a una de estas cuatro casillas contíguas, de una en una casillas:
   * arriba
   * abajo
   * derecha
   * izquierda
5. En el tablero hay comida distribuida de forma aleatoria por las casillas.
   * Se indica el número de casillas en las que hay comida
   * La cantidad de comida que hay en una casilla varía aleatoriamente entre 1 y 9
6. Cuando una manada llega a una casilla de comida, come e incorpora el valor de la comida de esa casilla a su puntuación.
7. Una manada no puede ocupar la casilla donde se encuentre otra manada rival.
8. Gana la manada que haya acumulado más puntos de comida al finalizar el juego.
9. El juego termina cuando ya no queda comida sobre el tablero o cuando todos los jugadores estuvieran bloqueados (ahoragos) y no pudieran moverse
10. Al final se elabora un ranking con los puntos obtenidos por cada manada y se proclama al gandador o a los ganadores en caso de empate.

## Estrategia
1. La clave para ganar el juego reside en trazar los caminos óptimos para llegar a las casillas que tienen más comida antes de que lo logren las manadas rivales.
2. También es importante tener en cuenta la posición de las manadas rivales

## Código
Codigo en Python utilizando programación orientada a objetos.  
1. Class Juego:
   * La gestión del juego se personaliza en un Juez con las siguientes funciones:
   * Inicia el juego
   * Crea un tablero vacío
   * Llena el tablero con las casillas que contienen la comida, ditribuidas de forma aleatoria
   * Las casillas de comida aparecen de forma aleatoria en el tablero en celdas vacías
   * La casilla que contien comida se identifica por un número entre 1 y 9 que indica la cantidad de comida existente
   * Se establece el número de manadas que jugarán, como mínimo son dos: manada A y manada B
   * Aparecen las manadas en el tablero distribuidas de forma aleatoria
   * Cada manada se representa por una letra, por ejemplo: A, B, C, D, ...
   * Las manadas no pueden aparecer en casillas que previamente no estuvieran vacías
   * Se imprime el tablero inicial y también se imprime después de cada moviento de cada manada
   * Cuando ya no quede comida en el tablero se proclama la manada que ha ganado el juego
2. Class Manada
   * Cada manada tiene su código de optimización de sus propias jugadas y no puede ver el código de las manadas rivales
   * Cada manada se comunica con el Juez mediante una API 
3. API
   * "Application Programming Interfaces" = "interfaz de programación de aplicaciones"
   * El juez se comunica con los jugadores mediante la **API**.
   * Cada uno de los jugadores tiene su propio código que utiliza la API proporcionada por el Juez.
   * El código de cada jugador no se comparte con los otros jugadores, esto es, cada manada tiene su propio código con su estrategia privada.
