# Juego de las Manadas

El juego de las manadas en Python con programación orientada a objetos.

## Normas
* Se juega en un tablero de 40x40 casillas
* Puede haber varios jugadores, mínimo dos jugadores que son:
 - Manada A
 - Manada B
* Los dos jugadores van moviéndose por el tablero alternando sus tiradas, primero la Manada A y luego la Manada B y así sucesivamente
* En cada tirada el jugador únicamente puede moverse a alguna de las casillas contíguas.
* Existe un máximo de 8 casillas contíguas a las que poder moverse. 
* Un jugador no puede ocupar la casilla donde se encuentre otro jugador.
* Cada manada está compuesta por una serie de miembros que inicialmente son 10 miembros para cada manada.
* En el tablero hay comida distribuida de forma aleatoria por las casillas.
 - Hay 20 casillas en las que aparecen una unidad de comida
 - Hay 16 casillas en las que aparecen dos unidades de comida
 _ Hay 9 casillas en las que aparecen tres unidades de comida
* Cuando una manada llega a una casilla de comida, come y se incrementa el número de miembros de la manada en tantos miembros nuevos como unidades de comida hubiera.
* Gana la manada que más miembros tenga cuando ya no quede comida en el tablero.

## Estrategia
* La clave para ganar el juego reside en trazar los caminos óptimos para llegar a las casillas que tienen comida antes de que lo logren las manadas rivales.
* También es importante tener en cuenta la posición de las manadas rivales
* Es importante tener en cuenta la cantidad de miembros de cada manada y tratar de aumentar el número de miembros de tu propia manada comiendo la mayor cantidad de comida posible.

## Código
* Codigo en Python utilizando programación orientada a objetos.
* Class Juego:
 - La gestión del juego se personaliza en un Juez con las siguientes funciones:
 - Inicia el juego
 - Crea un tablero vacío
 - Llena el tablero con las casillas que contienen la comida, ditribuidas de forma aleatoria
 - Las casillas de comida aparecen de forma aleatoria en el tablero en celdas vacías
 - La casilla que contien comida se identifica por un número entre 1 y 3 que indica la cantidad de comida existente
 - Se establece el número de manadas que jugarán, por defecto dos: manada A y manada B
 - Aparecen las manadas en el tablero distribuidas de forma aleatoria
 - Cada manada se representa por una letra, por ejemplo: A, B, C, D, ...
 - Las manadas no pueden aparecer en casillas que previamente no estuvieran vacías
 - Se imprime el tablero inicial y también se imprime después de cada moviento de cada manada
 - Cuando ya no quede comida en el tablero se proclama la manada que ha ganado el juego
* Class Manada
 - Cada manada tiene su código de optimización de sus propias jugadas y no puede ver el código de las manadas rivales
 - Cada manada se comunica con el Juez mediante una API 
* API
 - "Application Programming Interfaces" = "interfaz de programación de aplicaciones"
 - El juez se comunica con los jugadores mediante la **API**.
 - Cada uno de los jugadores tiene su propio código que utiliza la API proporcionada por el Juez.
 - El código de cada jugador no se comparte con los otros jugadores, esto es, cada manada tiene su propio código con su estrategia privada.
