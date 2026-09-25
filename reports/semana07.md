# Semana 07 - Representaciones del Reconocimiento

## 1. Descripción de la Práctica
En esta práctica se abordaron tres formas distintas de representar un mismo fenómeno para tareas de reconocimiento en Inteligencia Artificial: métricas numéricas en espacios vectoriales, inferencia lógica simbólica y reconocimiento secuencial mediante autómatas finitos.

## 2. Resultados de Ejecución

### 2.1 Representación Numérica
- **Entrada Muestra:** `[72.0, 0.85, 3.0]`
- **Entrada Referencia:** `[70.0, 0.80, 2.0]`
- **Distancia Euclidiana:** `2.291`

### 2.2 Representación Simbólica
- **Hechos observados:** `{"temperatura_alta", "carga_alta", "errores_presentes"}`
- **Regla aplicada:** SI `{"temperatura_alta", "carga_alta"}` están presentes, ENTONCES concluye `riesgo_termico`.
- **Resultado:** `riesgo_termico`

### 2.3 Autómata Finito
- **Secuencia `1101`:** Aceptada (`True`)
- **Secuencia `1110`:** Rechazada (`False`)
- **Secuencia `0001`:** Aceptada (`True`)