# Reporte Semana 09 - Reconocimiento de Imágenes

## 1. Selección de Imagen y Relación con el Proyecto
- **Imagen utilizada:** `data/imagen_proyecto.png` (Señal octagonal / Objeto de prueba visual)
- **Descripción:** Representa la imagen de entrada para probar la canalización de procesamiento e inspección visual automatizada.

## 2. Extracción de Características
- **Intensidad:** Conversión a escala de grises para aislar niveles de brillo y contraste sin interferencia del canal de color.
- **Bordes:** Detección de los límites octagonales y la tipografía mediante el operador Canny.
- **Geometría y Contorno:** Identificación de bordes geométricos claros y tipografía central.

## 3. Detección de Contornos (Canny)
- **Configuración utilizada:** \(\sigma = 1.0\)
- **Resultado:** Delimitación clara del borde del marco octagonal y las letras interiores.

## 4. Segmentación mediante Umbral (Otsu)
- **Valor de umbral obtenido:** `0.6113`
- **Máscara binaria:** Segmenta exitosamente el fondo claro del cuerpo del objeto.

## 5. Análisis de Regiones Conectadas
- **Número de regiones encontradas:** `9`
- **Interpretación:** Las regiones corresponden a los componentes conexos detectados (el marco exterior, el fondo y las letras de la señal).

## 6. Evidencia Generada
- **Artefacto:** `artifacts/semana09_vision.png`