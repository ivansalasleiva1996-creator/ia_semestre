# Reporte Técnico - Práctica Semana 2
**Asignatura:** Inteligencia Artificial (10.º Semestre)   
**Tema:** Entorno de Trabajo y Primer Modelo Reproducible  
 

---

## 1. Resumen de la Práctica

En esta primera práctica se estableció el entorno de trabajo estandarizado para la asignatura y se construyó la línea base ejecutable del **Sistema Inteligente Híbrido Aplicado**. El objetivo principal consistió en configurar el flujo completo de desarrollo en ingeniería de software e inteligencia artificial: estandarización del intérprete (Python 3.13.x), aislamiento de dependencias mediante entornos virtuales (`.venv`), control de versiones con Git y la creación de un primer modelo predictivo supervisado con Scikit-Learn.

---

## 2. Herramientas y Entorno de Desarrollo

Durante la sesión se configuraron las siguientes herramientas indispensables para garantizar reproducibilidad técnica:

* **Python 3.13.x (64 bits):** Lenguaje y runtime base estandarizado.
* **Visual Studio Code:** IDE de desarrollo integrando extensiones oficiales de Python y Jupyter.
* **Git:** Sistema de control de versiones distribuido para la gestión incremental del proyecto semestral.
* **PowerShell / Terminal:** Entorno de comandos para gestión del ciclo de vida del software.
* **Entorno Virtual (`.venv`):** Módulo para aislar las librerías del proyecto sin alterar el sistema operativo.
* **Librerías del Ecosistema de Datos:** `scikit-learn`, `numpy`, `pandas`, `matplotlib` y `jupyterlab`.

---

## 3. Desarrollo Paso a Paso Realizado

1. **Verificación e Instalación de Software Base:**
   * Instalación de Python 3.13 y Git, asegurando la inclusión de Python en las variables de entorno (`PATH`).
   * Desactivación de alias de ejecución de aplicaciones en Windows para prevenir conflictos de invocación a la tienda oficial.

2. **Creación del Proyecto y Entorno Virtual:**
   * Creación de la carpeta raíz del repositorio `ia_semestre`.
   * Generación e inicialización del entorno virtual aislado:
     ```powershell
     python -m venv .venv
     ```
   * Solución al bloqueo de políticas de ejecución en PowerShell mediante:
     ```powershell
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     .\.venv\Scripts\Activate.ps1
     ```

3. **Instalación y Congelamiento de Dependencias:**
   * Actualización del gestor de paquetes `pip`.
   * Instalación de las dependencias requeridas para el semestre.
   * Generación del archivo `requirements.txt` con el comando `python -m pip freeze > requirements.txt`.

4. **Estructuración del Repositorio:**
   * Creación de la arquitectura de directorios modular:
     * `src/`: Código fuente del sistema.
     * `data/`: Datos crudos y procesados.
     * `notebooks/`: Cuadernos exploratorios.
     * `artifacts/`: Binarios y modelos persistidos.
     * `reports/`: Documentación e informes técnicos.
     * `tests/`: Pruebas de software.

5. **Implementación del Primer Modelo Reproducible (`src/semana02_fundamentos.py`):**
   * Creación del script en Python cargando el dataset clásico *Iris*.
   * Construcción de un pipeline de Machine Learning con estandarización de datos y Regresión Logística.
   * Entrenamiento y evaluación sobre conjuntos diferenciados de prueba y entrenamiento.

6. **Control de Versiones:**
   * Creación del archivo `.gitignore` para omitir `.venv/` y cachés.
   * Elaboración del documento descriptivo `README.md`.
   * Inicialización del repositorio Git y realización del primer commit.

---

## 4. Explicación Técnica de Funcionamiento del Código

El script implementado en `src/semana02_fundamentos.py` ejecuta el siguiente flujo de aprendizaje automático supervisado:

1. **Carga de Datos:** Se importa el conjunto de datos Iris (`load_iris`), compuesto por 150 muestras con 4 características numéricas (longitud y ancho de sépalos y pétalos) distribuidas en 3 clases de flores.
2. **División de Datos (Train / Test Split):** Se dividen los datos en un 75% para entrenamiento (112 muestras) y un 25% para evaluación (38 muestras). Se utiliza `stratify=y` para asegurar que la proporción de clases se mantenga uniforme en ambos subconjuntos, y `random_state=42` para garantizar reproducibilidad exacta.
3. **Pipeline de Procesamiento:**
   * **`StandardScaler()`:** Escala las variables cuantitativas para que tengan media 0 y varianza 1, asegurando convergencia óptima en algoritmos basados en gradientes.
   * **`LogisticRegression()`:** Algoritmo lineal de clasificación supervisada con un límite máximo de 1000 iteraciones.
4. **Entrenamiento y Predicción:** Se entrena la canalización (`model.fit`) sobre los datos de entrenamiento y se realizan inferencias (`model.predict`) sobre los datos no vistos de prueba.
5. **Evaluación de Desempeño:** Se calculan las métricas de desempeño global mediante exactitud (*Accuracy*) y se construye la matriz de confusión para observar aciertos y desviaciones por clase.

---

## 5. Resultados Obtenidos y Métricas

Al ejecutar el script mediante el comando `python src/semana02_fundamentos.py`, la salida registrada en la terminal es:

```text
Muestras entrenamiento: 112
Muestras prueba: 38
Accuracy: 0.974
Matriz de confusión:
[[13  0  0]
 [ 0 12  1]
 [ 0  0 12]]