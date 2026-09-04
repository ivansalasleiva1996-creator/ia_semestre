from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Rutas de archivos
DATA_DIR = Path("data")
REPORTS_DIR = Path("reports")
KB_PATH = DATA_DIR / "base_conocimiento.txt"
REPORT_PATH = REPORTS_DIR / "semana05.md"

# Documentos por defecto en caso de que el archivo no exista
DEFAULT_DOCS = [
    "Un equipo caliente o con temperatura alta requiere revisar el ventilador y disipador.",
    "La caida de internet o falla de DNS se resuelve verificando el router o interfaz de red.",
    "El consumo alto de CPU o memoria lentifica las aplicaciones del sistema.",
    "Una cuenta bloqueada o con error de inicio de sesion requiere validar credenciales y permisos.",
    "Los errores en la base de datos o almacenamiento se solucionan liberando espacio en disco.",
    "La falta de acceso a servicios web se asocia a bloqueos en el firewall o configuraciones de red.",
    "Las fallas en pantalla o artefactos visuales indican problemas en el controlador de video o hardware.",
    "Las interrupciones en conexiones inalambricas ocurren por interferencia de señal Wi-Fi.",
]

# Reglas expertas (Sistemas Expertos)
RULES = [
    (lambda q: "temperatura" in q or "caliente" in q, "revisar_ventilacion"),
    (lambda q: "red" in q or "internet" in q or "dns" in q, "revisar_conectividad"),
    (lambda q: "sesion" in q or "cuenta" in q or "bloqueada" in q, "revisar_acceso"),
    (lambda q: "cpu" in q or "memoria" in q or "lenta" in q, "revisar_rendimiento"),
    (lambda q: "disco" in q or "espacio" in q or "almacenamiento" in q, "revisar_almacenamiento"),
]

# Datos de entrenamiento para el clasificador (15 ejemplos)
TRAIN_X = [
    "equipo muy caliente y sobrecalentado",
    "el procesador subio de temperatura",
    "se cae el internet a cada rato",
    "error de resolucion de nombres dns",
    "no hay conexion a la red local",
    "no puedo iniciar sesion en mi cuenta",
    "usuario bloqueado en la plataforma",
    "credenciales invalidas al ingresar",
    "el sistema esta muy lento y trabado",
    "alto consumo de memoria ram y cpu",
    "el disco duro esta lleno sin espacio",
    "falla al guardar archivos en almacenamiento",
    "sin acceso a la pagina web por firewall",
    "pantalla parpadea con lineas extrañas",
    "la señal de wifi es inestable",
]

TRAIN_Y = [
    "hardware", "hardware", "red", "red", "red",
    "seguridad", "seguridad", "seguridad", "rendimiento", "rendimiento",
    "almacenamiento", "almacenamiento", "red", "hardware", "red"
]

def load_documents() -> list[str]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not KB_PATH.exists():
        KB_PATH.write_text("\n".join(DEFAULT_DOCS), encoding="utf-8")
    docs = [line.strip() for line in KB_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(docs) < 8:
        raise ValueError("data/base_conocimiento.txt debe contener al menos 8 entradas.")
    return docs

DOCS = load_documents()
vectorizer = TfidfVectorizer()
doc_matrix = vectorizer.fit_transform(DOCS)

classifier = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000, random_state=42)
)
classifier.fit(TRAIN_X, TRAIN_Y)

def answer(query: str) -> dict:
    q = query.lower()
    fired = [name for condition, name in RULES if condition(q)]
    similarities = cosine_similarity(vectorizer.transform([q]), doc_matrix)[0]
    best_index = int(similarities.argmax())
    label = str(classifier.predict([q])[0])
    
    return {
        "reglas": fired,
        "evidencia": DOCS[best_index],
        "similitud": float(similarities[best_index]),
        "clase": label,
    }

def write_report(rows: list[tuple[str, dict]]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# Semana 05 - Sistema Híbrido Traducible", ""]
    for i, (query, result) in enumerate(rows, start=1):
        lines += [
            f"## Consulta {i}",
            f"- **Entrada:** {query}",
            f"- **Reglas disparadas:** {', '.join(result['reglas']) or 'ninguna'}",
            f"- **Evidencia recuperada:** {result['evidencia']}",
            f"- **Similitud coseno (TF-IDF):** {result['similitud']:.3f}",
            f"- **Clase predicha:** {result['clase']}",
            ""
        ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    test_queries = [
        "El equipo esta muy caliente y el ventilador hace ruido",
        "Se cayo el internet y aparece error de DNS",
        "No puedo iniciar sesion porque mi cuenta esta bloqueada"
    ]
    
    results = []
    print("=" * 60)
    print("SISTEMA HÍBRIDO DE SOPORTE TÉCNICO")
    print("=" * 60)
    
    for q in test_queries:
        res = answer(q)
        results.append((q, res))
        print(f"\nConsulta: '{q}'")
        print(f"  └─ Reglas: {res['reglas']}")
        print(f"  └─ Evidencia: {res['evidencia']}")
        print(f"  └─ Similitud: {res['similitud']:.3f}")
        print(f"  └─ Clase: {res['clase']}")

    write_report(results)
    print("\n" + "=" * 60)
    print("Reporte generado exitosamente en reports/semana05.md")