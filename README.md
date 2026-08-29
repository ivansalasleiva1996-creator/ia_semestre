# Sistema Inteligente Híbrido Aplicado - IA 10.º Semestre

## Práctica Semana 2: Entorno de Trabajo y Primer Modelo Reproducible

---

### Descripción del Proyecto
Este proyecto constituye la línea base y punto de partida acumulativo para el desarrollo de un **Sistema Inteligente Híbrido Aplicado**, llevado a cabo en la asignatura de **Inteligencia Artificial (10.º Semestre)** del programa de **Ingeniería de Sistemas**.

En esta práctica inicial se estandariza el entorno de desarrollo, la estructura del proyecto y el control de versiones con Git, además de implementar y evaluar un primer clasificador supervisado reproducible (Regresión Logística sobre el conjunto de datos Iris) utilizando `scikit-learn`.

### 2. Actualización para el archivo `README.md`

Agrega el bloque correspondiente a la **Semana 4** en la sección de progreso o tabla de contenidos de tu `README.md`:

```markdown
### Semana 04: Marco Tecnológico de la IA (Búsqueda A* y Decisión Minimax)

* **Descripción:** Formulación de problemas en espacios de estados e implementación de algoritmos clásicos de búsqueda informada y toma de decisiones en entornos adversariales.
* **Módulos Desarrollados:**
  * `src/semana04_astar.py`: Algoritmo de búsqueda A* con heurística Manhattan y renderizador visual del camino en matriz.
  * `src/semana04_minimax.py`: Toma de decisiones óptima para Tres en Línea utilizando Minimax optimizado con **Poda Alfa-Beta ($\alpha$-$\beta$)**.
  * `reports/semana04.md`: Documentación teórica de estados, acciones, funciones de costo, admisibilidad y análisis de trade-offs.
* **Ejecución:**
  ```powershell
  python src/semana04_astar.py
  python src/semana04_minimax.py

---

### 👤 Autor del Proyecto
* **Estudiante:** Ivan Andres Salas Leiva
* **Programa:** Ingeniería de Sistemas (10.º Semestre)
* **Asignatura:** Inteligencia Artificial 
* **Instittución:** ETITC

---

###  Herramientas y Tecnologías Utilizadas
* **Lenguaje:** Python 3.13.x (64-bit)
* **Entorno de Desarrollo:** Visual Studio Code (Extensiones: Python, Jupyter)
* **Control de Versiones:** Git
* **Librerías Principales:**
  * `scikit-learn`: Para el preprocesamiento, canalización (pipeline) y entrenamiento del modelo de Regresión Logística.
  * `numpy` & `pandas`: Para manipulación y estructura de datos.
  * `matplotlib`: Para visualización gráfica y análisis.
  * `jupyterlab`: Para experimentación en entornos interactivos.

---

###  Estructura del Proyecto

```text
ia_semestre/
├── .venv/               # Entorno virtual de Python (ignorado por Git)
├── artifacts/          # Modelos guardados, binarios y artefactos generados
├── data/               # Conjuntos de datos del proyecto (crudos y procesados)
├── notebooks/          # Cuadernos Jupyter para análisis exploratorio y pruebas
├── reports/            # Informes técnicos, métricas y documentación
├── src/                # Código fuente del sistema inteligente
│   └── semana02_fundamentos.py  # Script de la línea base y primer modelo
├── tests/              # Pruebas unitarias e integración
├── .gitignore          # Archivos e índices excluidos del control de versiones
├── README.md           # Documentación principal del repositorio
└── requirements.txt    # Lista de dependencias del proyecto estandarizadas