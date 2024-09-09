# **Juego de las Manadas**

* Es un juego de tablero por turnos, programado en Python utilizando Programación Orientada a Objetos (POO).
* El objetivo es que los jugadores, representados por letras, acumulen puntos moviéndose por el tablero y recogiendo comida distribuida de forma aleatoria.

---

## **Normas del Juego**

### **1. Tablero**
- El tablero es un cuadrado, por defecto de 10x10 casillas.
- Cada casilla puede estar vacía, contener comida o un jugador.

### **2. Jugadores**
- El número de jugadores puede variar entre 2 y 26. Por defecto son dos jugadores.
- Cada jugador es representado por una letra mayúscula (A, B, C, ... Z).
- La posición inicial de cada jugador se asigna aleatoriamente en una casilla vacía del tablero.
- Los jugadores no pueden compartir casilla.

### **3. Movimiento de los Jugadores**
- Los jugadores se mueven por turnos en orden alfabético: primero A, luego B, y así sucesivamente.
- Cada jugador se puede mover en una de las cuatro direcciones (arriba, abajo, izquierda, derecha) a una casilla adyacente.
- Un jugador no puede moverse a una casilla ocupada por otro jugador.
- Si todas las casillas adyacentes están ocupadas o son bordes del tablero, el jugador pierde su turno.

### **4. Comida**
- Algunas casillas contienen comida, representada por un número del 1 al 9, que indica la cantidad de comida.
- La comida se distribuye aleatoriamente en casillas vacías y no puede aparecer en una casilla ocupada por un jugador o comida previa.
- Los jugadores recogen la comida de la casilla a la que se muevan, sumando la cantidad correspondiente a su puntuación.
- En el código se establece la cantidad de comida que se generará en posiciones aleatorias.
- Por ejemplo, el diccionario {9:1, 8:2, 7:2, 6:2, 5:2, 4:3, 3:3, 2:4, 1:5} representa que existirán 24 casillas con comida destribuidos así:
  - de nivel de comida 9 existirá 1 casilla
  - de nivel de comida 8 existirán 2 casillas
  - de nivel de comida 7 existirán 2 casillas
  - de nivel de comida 6 existirán 2 casillas
  - de nivel de comida 5 existirán 2 casillas
  - de nivel de comida 4 existirán 3 casillas
  - de nivel de comida 3 existirán 3 casillas
  - de nivel de comida 2 existirán 4 casillas
  - de nivel de comida 1 existirán 5 casillas  
### **5. Condiciones de Victoria**
  - El juego finaliza cuando todos los jugadores han completado su turno tras haberse recogido la última comida del tablero.
  - Gana el jugador con más puntos acumulados.
  - Si hay empate en puntos, se declaran varios ganadores.


---

## **Estrategia de los Jugadores**

1. **Optimización del Movimiento**: La clave para ganar es trazar caminos estratégicos hacia las casillas con mayor cantidad de comida antes que los rivales.
2. **Observación de Rivales**: Los jugadores deben tener en cuenta las posiciones y movimientos de sus oponentes para anticipar sus jugadas.

---

## **Estructura del Código**

### **1. Clase `Juego`**
- Se encarga de gestionar la lógica del juego y las interacciones entre jugadores y el tablero.
- Funciones principales:
   - Iniciar el juego y el tablero.
   - Generar los jugadores y posicionarlos.
   - Distribuir la comida en el tablero.
   - Gestionar los turnos y el movimiento de los jugadores.
   - Determinar el ganador y mostrar el ranking final.

### **2. Clase `Tablero`**
- Representa el tablero de juego.
- Funciones principales:
   - Crear el tablero vacío.
   - Las celdas vacías se representan por el símbolo punto medio "·" (middle dot).
   - Colocar jugadores y comida en posiciones válidas.
   - Imprimir el estado del tablero después de cada turno.

### **3. Clase `Manada`**
- Representa a cada jugador individual.
- Funciones principales:
   - Controlar los movimientos y la estrategia de cada jugador.
   - Acumular puntos al recoger comida.
   - Comunicar las decisiones al Juez del juego.

### **4. Clase `Juez`**
- Media la comunicación entre el tablero y los jugadores.
- Funciones principales:
   - Validar los movimientos.
   - Aplicar las reglas del juego.
   - Mantener el orden de turnos y la puntuación.

---

## **API de Comunicación**
- Los jugadores interactúan con el Juez mediante una API, que les permite obtener información del estado del tablero y realizar movimientos.
- Cada jugador tiene su propio código y estrategia, que no pueden ver ni modificar el resto de jugadores.

