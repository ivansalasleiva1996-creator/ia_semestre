# Semana 04 - Marco Tecnológico de la IA: Búsqueda A* y Decisión Minimax

## 1. Formulación de Problemas en Espacios de Estados

### 1.1 Algoritmo A* (Navegación en Cuadrícula)
* **Estado:** Coordenada en formato de tupla `(fila, columna)` que representa la ubicación en la matriz.
* **Acción:** Moverse ortogonalmente en 4 direcciones (arriba, abajo, izquierda, derecha) verificando límites y evitando obstáculos (`#`).
* **Transición:** Cambio de la posición actual `(r, c)` a la celda adyacente `(r+dr, c+dc)`.
* **Meta:** Alcanzar la coordenada objetivo `GOAL = (4, 4)`.
* **Costo $g(n)$:** Acumulado unitario por cada paso ejecutado ($costo = 1$ por movimiento).
* **Heurística $h(n)$:** Distancia Manhattan $\vert{}r_1 - r_2\vert{} + \vert{}c_1 - c_2\vert{}$, admisible y consistente para cuadrículas ortogonales.
* **Prioridad $f(n)$:** $f(n) = g(n) + h(n)$, la cual garantiza la ruta óptima minimizando la exploración innecesaria.

### 1.2 Algoritmo Minimax con Poda Alfa-Beta (Tres en Línea)
* **Estado:** Vector lineal de 9 elementos que representa la configuración del tablero.
* **Acción:** Posicionar el símbolo del jugador activo (`X` o `O`) en una casilla disponible (`" "`).
* **Meta / Estado Terminal:** Tres marcas consecutivas alineadas o tablero lleno (empate).
* **Función de Utilidad:** $+1$ para victoria de `X` (MAX), $-1$ para victoria de `O` (MIN), $0$ para empates.
* **Criterio de Decisión:** Selección de la jugada que maximiza el beneficio de MAX anticipando la respuesta racional de MIN, optimizado mediante límites de poda $\alpha$ y $\beta$.

---

## 2. Mejoras Implementadas al Sistema

Con el objetivo de elevar la eficiencia computacional y la interpretabilidad de los resultados, se integraron las siguientes optimizaciones en los scripts:

* **Poda Alfa-Beta en Minimax (`src/semana04_minimax.py`):** Se incorporaron los parámetros $\alpha$ (mejor valor garantizado para MAX) y $\beta$ (mejor valor garantizado para MIN) para interrumpir la evaluación de ramas que no alteran la decisión final, reduciendo el costo computacional de $O(b^d)$ sin afectar la optimalidad.
* **Visualización de Mapa en A* (`src/semana04_astar.py`):** Se añadió la función `print_grid_with_path`, la cual proyecta en consola el mapa renderizado marcando el punto inicial (`S`), el destino (`G`) y el trayecto calculado con asteriscos (`*`).
* **Gestión Eficiente de Memoria y Estado:** Se optimizó el manejo del tablero en Minimax realizando modificaciones *in-place* con retroceso (*backtracking*) en lugar de clonar el vector de estado en cada llamada recursiva.
* **Renderizado Formateado de Tablero:** Se implementó una vista en matriz $3 \times 3$ accesible en terminal para inspeccionar visualmente los estados evaluados por el agente.

---

## 3. Resultados de Ejecución

### 3.1 Búsqueda A*
* **Ruta hallada:** `[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]`
* **Costo total:** `8` pasos.
* **Visualización:**
  ```text
  S * * * *
  . # # # *
  . . . # *
  . # . . *
  . . . . G