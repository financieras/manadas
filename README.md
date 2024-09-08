# Juego de las Manadas

El juego de las manadas en Python con programación orientada a objetos.

## Normas
1. Se juega en un tablero cuadrado que se puede establecer por defecto en un tamaño de 10x10 casillas.
2. El número de jugadores se establece inicialmente y puede variar entre 2 y 26 jugadores.
   * El nombre de cada jugador se otorga mediante una letra mayúscula correlativa del alfabeto.
   * Si son dos jugadores se asignarán las letras A y B, denominándose:
     1. A: representa al jugador A o Manada A
     2. B: representa al jugador B o Manada B
   * La posición de los jugadores en el tablero se genera aleatoriamente y no pueden aparecer nuevos jugadores donde ya existiera otro previamente. No pueden ocupar dos jugadores la misa casilla. 
3. Los jugadores van moviéndose por el tablero alternando sus tiradas, primero la Manada A y luego la Manada B y así sucesivamente.
4. En cada tirada cada jugador puede moverse en cruz a una casilla contígua. Los movimientos del jugador son de una en una casilla alguna de estas direcciones:
   * arriba
   * abajo
   * derecha
   * izquierda
5. En el tablero hay comida distribuida de forma aleatoria por las casillas.
   * Inicialmente se genera comida en algunas casillas.
   * Las casillas que tienen comida se representan por un número entero entre 1 y 9, ese número indica la cantidad de comida que hay en esa casilla.
   * Se establece en el programa el número de celdas que tendrán comida y la cantidad de comida que habrá en ellas.
   * Las casillas con comida se generan de forma aletoria en el tablero y no pueden aparecer donde exista un jugador o donde previamente ya exista comida.
7. Cuando un jugador llega a una casilla que contiene comida, come e incorpora el valor de la comida de esa casilla a su puntuación.
8. Un jugador en sus movimientos por el tablero no puede ocupar la casilla donde se encuentre otro jugador.
   * Esto pudiera dar lugar a que en algún momento un jugador no pudiera moverse al estar ocupadas por otros jugadores las casillas contíguas o por el borde del tablero. En este caso, el jugador efectuará esa tirada sin hacer movimiento alguno, pero esto no interrumpe el juego.
9. Gana el jugador que haya acumulado más puntos de comida al finalizar el juego.
10. El juego termina cuando ya no queda comida sobre el tablero.
11. Al final se elabora un ranking con los puntos obtenidos por cada jugadora y se proclama al gandador o a los ganadores en caso de empate.

## Estrategia
1. La clave para ganar el juego reside en trazar los caminos óptimos para llegar a las casillas que tienen más comida antes de que lo logren los jugadores rivales.
2. También es importante tener en cuenta la posición de los jugadores rivales.

## Código
Codigo en Python utilizando programación orientada a objetos.  
1. Class Juego:
   * La gestión del juego se personaliza en un Juez con las siguientes funciones:
   * Inicia el juego.
   * Crea un tablero vacío.
   * Genera los jugadores.
     - Se establece el número de jugadores, como mínimo son dos: A y B.
     - Aparecen los jugadores en el tablero distribuidos de forma aleatoria
     - Cada jugador se representa por una letra mayúscula, por ejemplo: A, B, C, D, ..., Z.
     - Los jugadores no pueden aparecer en casillas que previamente no estuvieran vacías.
   * Genera la comida.
     - Se establece cúantas celdas tendremos con comida y la cantidad de comida que existirá en cada una de ellas.  
     - La casilla que contenga comida se identificará por un número entre 1 y 9 que indica la cantidad de comida existente en esa celda. 
     - Las celdas que contienen la comida se ditribuyen de forma aleatoria.
     - Las celdas con comida no pueden aparecer en otras celdas previamente ocupadas por jugadores o por otra comida.     
   * Se imprime el tablero inicial y también se imprime después del moviento efectuado por cada jugador.
   * En el momento en el que ya no quede comida en el tablero finaliza el juego, se proclama el ganador o ganadores y se mustra el ranking.
2. Class Manada
   * Cada jugador tiene su código de optimización de sus propias jugadas y no puede ver el código de los jugadores rivales.
   * Cada jugador se comunica con el Juez mediante una API 
3. API
   * "Application Programming Interfaces" = "interfaz de programación de aplicaciones"
   * El juez se comunica con los jugadores mediante la **API**.
   * Cada uno de los jugadores tiene su propio código que utiliza la API proporcionada por el Juez.
4. Ganar el juego 
   * El código de cada jugador no se comparte con los otros jugadores. Cada jugador tiene su propio código con su estrategia privada.
   * Si algún jugador efectúa sus movimientos de forma aleatoria posiblemente no será el más rápido en llegar a las celdas con comida y por lo tanto perderá en juego.
   * Es posible que algún otro jugador establezca una mejor estrategia para llegar a las celdas con comida antes que sus competidores.
   * Esto supone que la clave para ganar el juego reside en la **estrategia** (código) que tenga cada jugador para acumular el mayor número de puntos de comida, antes que sus rivales.
