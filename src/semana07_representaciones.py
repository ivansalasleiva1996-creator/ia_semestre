import numpy as np

# 1) Representación numérica (Vector de características y distancia Euclidiana)
sample = np.array([72.0, 0.85, 3.0])  # temperatura, carga, errores
reference = np.array([70.0, 0.80, 2.0])
distance = np.linalg.norm(sample - reference)

print("=" * 50)
print("REPRESENTACIONES DEL RECONOCIMIENTO")
print("=" * 50)
print("1. REPRESENTACIÓN NUMÉRICA")
print("   Distancia numérica (Euclidiana):", round(float(distance), 3))

# 2) Representación simbólica (Conjunto de hechos y motor de reglas)
facts = {"temperatura_alta", "carga_alta", "errores_presentes"}

print("\n2. REPRESENTACIÓN SIMBÓLICA")
if {"temperatura_alta", "carga_alta"}.issubset(facts):
    print("   Conclusión simbólica: riesgo_termico")

# 3) Reconocimiento mediante autómata finito (Acepta cadenas que terminan en '01')
def accepts_01(text):
    state = "q0"
    transitions = {
        ("q0", "0"): "q1", ("q0", "1"): "q0",
        ("q1", "0"): "q1", ("q1", "1"): "q2",
        ("q2", "0"): "q1", ("q2", "1"): "q0",
    }
    for symbol in text:
        state = transitions[(state, symbol)]
    return state == "q2"

print("\n3. RECONOCIMIENTO MEDIANTE AUTÓMATA FINITO")
for seq in ("1101", "1110", "0001"):
    print(f"   Secuencia '{seq}' aceptada:", accepts_01(seq))