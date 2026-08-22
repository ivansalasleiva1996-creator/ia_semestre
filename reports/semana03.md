# Semana 03 - Taxonomía de Inteligencia Artificial

## Resultado automático frente a clasificación manual de referencia

| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |
|---|---|---|---|---|
| 1 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 2 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 3 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 4 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 5 | Sistemas de recomendación | Sistemas de recomendación | Sistemas de recomendación | Coincide |
| 6 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 7 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 8 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 9 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 10 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 11 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 12 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural, Aprendizaje automático predictivo | Procesamiento de lenguaje natural | Coincide |
| 13 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 14 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 15 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 16 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 17 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 18 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 19 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 20 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |

Coincidencia con la referencia: **100.00%** (20/20).

## Cinco reglas propias
Se aplicaron las siguientes reglas personalizadas en `CUSTOM_RULES` para abarcar tecnicismos adicionales de ingeniería:
1. **`placa` / `escaneo`** -> *Visión por computador*: Permite mapear términos de procesamiento de imágenes y lectura automática.
2. **`opinion` / `traduccion`** -> *Procesamiento de lenguaje natural*: Amplía la capacidad para detectar análisis de sentimientos y minería de texto.
3. **`tendencia` / `mantenimiento`** -> *Aprendizaje automático predictivo*: Captura la semántica de modelos predictivos en series temporales.
4. **`criterio` / `normativa`** -> *Sistemas expertos*: Identifica motores de inferencia basados en reglas de negocio estricta.
5. **`navegacion` / `telemetria`** -> *Robótica y sistemas autónomos*: Permite asociar la recolección de variables físicas a la toma de acción de un agente.

## Discrepancias y análisis
1. **Naturaleza Multimodales (Sistemas Híbridos):** El caso #17 (*Vehículo autónomo*) fue clasificado tanto en *Visión por Computador* como en *Robótica y Sistemas Autónomos*. La categoría principal seleccionada fue Visión por Computador por la mayor frecuencia de palabras clave asociadas a la percepción visual.
2. **Solidez de la taxonomía:** Un problema real de ingeniería no suele ser puro. La estructura simbólica diseñada permite retener categorías secundarias para abordar soluciones híbridas completas.

## Nota técnica
Un problema real puede pertenecer a varias áreas de IA. La columna 'principal' usa la categoría con mayor cantidad de coincidencias; las demás coincidencias se conservan como categorías secundarias.

## Mejoras realizadas al sistema

Con el fin de elevar la precisión del clasificador y alinearlo con los estándares de ingeniería de software para IA, se implementaron las siguientes optimizaciones técnicas en el script `src/semana03_taxonomia.py`:

* **Stemming ligero con Expresiones Regulares:** Se sustituyó la búsqueda estricta de palabras completas por un motor basado en `re.search` que detecta raíces léxicas. Esto elimina falsos negativos causados por variaciones de plurales, géneros o conjugaciones (por ejemplo, emparejando automáticamente *fotografía*, *fotografías* y *fotográfico* sin duplicar reglas).
* **Ampliación del Vocabulario Técnico:** Se expandió el diccionario base de categorías con términos de ingeniería avanzados (`video`, `segmentación`, `análisis de sentimiento`, `series temporales`, `mantenimiento predictivo`, `algoritmos de planificación`, `árboles de decisión` y `telemetría`).
* **Reglas de Dominio Personalizadas (`CUSTOM_RULES`):** Se integraron 5 pares de reglas específicas orientadas a captura de infraestructura y datos industriales (como *placa/escaneo* en Visión y *criterio/normativa* en Sistemas Expertos).
* **Soporte Multimodal y Preservación de Categorías Secundarias:** Se ajustó la lógica de ordenamiento para que la categoría principal se determine por frecuencia de coincidencias, manteniendo una lista de categorías secundarias para abordar el análisis de Sistemas Inteligentes Híbridos.

