# Semana 05 - Sistema Híbrido Traducible

## Consulta 1
- **Entrada:** El equipo esta muy caliente y el ventilador hace ruido
- **Reglas disparadas:** revisar_ventilacion
- **Evidencia recuperada:** Un equipo caliente o con temperatura alta requiere revisar el ventilador y disipador.
- **Similitud coseno (TF-IDF):** 0.564
- **Clase predicha:** hardware

## Consulta 2
- **Entrada:** Se cayo el internet y aparece error de DNS
- **Reglas disparadas:** revisar_conectividad
- **Evidencia recuperada:** La caida de internet o falla de DNS se resuelve verificando el router o interfaz de red.
- **Similitud coseno (TF-IDF):** 0.497
- **Clase predicha:** red

## Consulta 3
- **Entrada:** No puedo iniciar sesion porque mi cuenta esta bloqueada
- **Reglas disparadas:** revisar_acceso
- **Evidencia recuperada:** Una cuenta bloqueada o con error de inicio de sesion requiere validar credenciales y permisos de usuario.
- **Similitud coseno (TF-IDF):** 0.477
- **Clase predicha:** seguridad
