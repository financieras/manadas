# Juego de las Manadas

El juego de las manadas en Python con programación orientada a objetos.

## Normas
1. Se juega en un tablero de 40x40 casillas
2. Puede haber varios jugadores, mínimo dos jugadores que son A y B, llamados:
   * Manada A
   * Manada B
3. Los jugadores van moviéndose por el tablero alternando sus tiradas, primero la Manada A y luego la Manada B y así sucesivamente
4. En cada tirada cada manada solo puede moverse a una de estas cuatro casillas contíguas:
   * arriba
   * abajo
   * derecha
   * izquierda 
5. Cada manada está compuesta por una serie de miembros que inicialmente son 10 miembros para cada manada.
6. En el tablero hay comida distribuida de forma aleatoria por las casillas.
   * Hay 20 casillas en las que aparecen una unidad de comida
   * Hay 16 casillas en las que aparecen dos unidades de comida
   * Hay 9 casillas en las que aparecen tres unidades de comida
7. Cuando una manada llega a una casilla de comida, come y se incrementa el número de miembros de la manada en tantos miembros nuevos como unidades de comida hubiera.
8. Una manada no puede ocupar la casilla donde se encuentre otra manada rival, pero si puede intentar chocar con ella.
9. Si una manada choca con otra decimos que se produce una pelea y que la manada con la que se ha chocado recibe un daño.
10. El daño se traduce en un número de miembros de la manada que mueren.
11. El daño se genera con un número aleatorio, por lo que los muertos pueden oscilar entre un mínimo de 1 y un cierto porcentaje de la población existente en esa manada.
12. Gana la manada que más miembros tenga cuando ya no quede comida en el tablero.
13. Al final se elabora un ranking con el número de miembros que quedan en cada manada cuando el juego termina.

## Estrategia
1. La clave para ganar el juego reside en trazar los caminos óptimos para llegar a las casillas que tienen comida antes de que lo logren las manadas rivales.
2. También es importante tener en cuenta la posición de las manadas rivales
3. Es importante tener en cuenta la cantidad de miembros de cada manada y tratar de aumentar el número de miembros de tu propia manada comiendo la mayor cantidad de comida posible.

## Código
Codigo en Python utilizando programación orientada a objetos.  
1. Class Juego:
   * La gestión del juego se personaliza en un Juez con las siguientes funciones:
   * Inicia el juego
   * Crea un tablero vacío
   * Llena el tablero con las casillas que contienen la comida, ditribuidas de forma aleatoria
   * Las casillas de comida aparecen de forma aleatoria en el tablero en celdas vacías
   * La casilla que contien comida se identifica por un número entre 1 y 3 que indica la cantidad de comida existente
   * Se establece el número de manadas que jugarán, por defecto dos: manada A y manada B
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
