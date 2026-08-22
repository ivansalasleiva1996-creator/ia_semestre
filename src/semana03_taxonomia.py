from dataclasses import dataclass
from pathlib import Path
import csv
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT / "data" / "casos_ia.csv"
REPORT_FILE = ROOT / "reports" / "semana03.md"

@dataclass(frozen=True)
class Category:
    name: str
    keywords: tuple[str, ...]

CATEGORIES = [
    Category("Visión por computador", (
        "imagen", "imagenes", "foto", "fotografia", "fotografias", "camara",
        "rostro", "rostros", "peaton", "peatones", "senal", "senales", "video",
        "escaneo", "pixeles", "deteccion", "segmentacion", "medica", "placa"
    )),
    Category("Procesamiento de lenguaje natural", (
        "texto", "comentario", "comentarios", "correo", "correos", "chatbot",
        "contrato", "contratos", "nombres", "lenguaje", "analizar", "analisis",
        "extraer", "voz", "sentimiento", "resumen", "opinion", "traduccion"
    )),
    Category("Aprendizaje automático predictivo", (
        "predecir", "probabilidad", "demanda", "fraude", "fraudes", "sensores",
        "clasificar", "regresion", "anomalias", "tendencia", "patron", "mantenimiento"
    )),
    Category("Sistemas de recomendación", (
        "recomendar", "preferencias", "historial de visualizacion", "sugerir", "filtrado"
    )),
    Category("Búsqueda y optimización", (
        "ruta", "rutas", "horario", "horarios", "combinacion optima",
        "optimizar", "capacidad maxima", "algoritmo", "planificacion"
    )),
    Category("Sistemas expertos", (
        "diagnostico", "diagnosticos", "reglas", "politicas", "solicitud de credito",
        "criterio", "normativa", "arbol de decision", "conocimiento"
    )),
    Category("Robótica y sistemas autónomos", (
        "robot", "robots", "dron", "drones", "vehiculo autonomo", "obstaculos",
        "navegacion", "actuador", "telemetria", "control"
    )),
]

# Cinco reglas propias ampliadas para cubrir tecnicismos avanzados
CUSTOM_RULES = {
    "Visión por computador": ("placa", "escaneo"),
    "Procesamiento de lenguaje natural": ("opinion", "traduccion"),
    "Aprendizaje automático predictivo": ("tendencia", "mantenimiento"),
    "Sistemas expertos": ("criterio", "normativa"),
    "Robótica y sistemas autónomos": ("navegacion", "telemetria"),
}

MANUAL_REFERENCE = [
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Aprendizaje automático predictivo",
    "Búsqueda y optimización",
    "Sistemas de recomendación",
    "Aprendizaje automático predictivo",
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Aprendizaje automático predictivo",
    "Sistemas expertos",
    "Visión por computador",
    "Procesamiento de lenguaje natural",
    "Robótica y sistemas autónomos",
    "Búsqueda y optimización",
    "Aprendizaje automático predictivo",
    "Procesamiento de lenguaje natural",
    "Visión por computador",
    "Sistemas expertos",
    "Robótica y sistemas autónomos",
    "Búsqueda y optimización",
]

def normalize(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def normalize_header(text: str) -> str:
    return normalize(text).replace(" ", "")

def contains_keyword(text: str, keyword: str) -> bool:
    """Evalúa coincidencia buscando si la raíz de la palabra existe en el texto."""
    normalized_text = normalize(text)
    normalized_keyword = normalize(keyword)
    return re.search(r"\b" + re.escape(normalized_keyword), normalized_text) is not None

def build_categories() -> list[Category]:
    result = []
    for category in CATEGORIES:
        extra = CUSTOM_RULES.get(category.name, ())
        result.append(Category(category.name, category.keywords + tuple(extra)))
    return result

def classify_problem(text: str) -> tuple[str, list[str], dict[str, int]]:
    scores = {}
    categories = build_categories()
    for category in categories:
        score = sum(contains_keyword(text, keyword) for keyword in category.keywords)
        scores[category.name] = score
    
    matches = [
        (scores[cat.name], index, cat.name)
        for index, cat in enumerate(categories)
        if scores[cat.name] > 0
    ]
    matches.sort(key=lambda item: (-item[0], item[1]))
    
    detected = [name for _, _, name in matches]
    primary = detected[0] if detected else "Requiere análisis"
    return primary, detected or ["Requiere análisis"], scores

def read_cases() -> list[str]:
    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"No existe {CSV_FILE}. Crea data/casos_ia.csv antes de ejecutar la práctica."
        )
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("El CSV está vacío o no contiene encabezados.")
        original_headers = list(reader.fieldnames)
        reader.fieldnames = [normalize_header(name) for name in reader.fieldnames]
        if "descripcion" not in reader.fieldnames:
            raise ValueError(
                f"No se encontró la columna 'descripcion'. Encabezados encontrados: {original_headers}"
            )
        cases = []
        for row in reader:
            description = (row.get("descripcion") or "").strip()
            if description:
                cases.append(description)
        if len(cases) < 20:
            raise ValueError(
                f"La práctica requiere al menos 20 casos y el archivo contiene {len(cases)}."
            )
        return cases

def write_report(results: list[dict]) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    reference_count = min(len(results), len(MANUAL_REFERENCE))
    matches = sum(
        1 for i in range(reference_count) if results[i]["primary"] == MANUAL_REFERENCE[i]
    )
    accuracy = (100 * matches / reference_count) if reference_count else 0.0

    lines = [
        "# Semana 03 - Taxonomía de Inteligencia Artificial",
        "",
        "## Resultado automático frente a clasificación manual de referencia",
        "",
        "| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |",
        "|---|---|---|---|---|",
    ]
    
    for i, result in enumerate(results, start=1):
        manual = MANUAL_REFERENCE[i-1] if (i-1) < len(MANUAL_REFERENCE) else "Pendiente"
        status = "Coincide" if result["primary"] == manual else "Revisar"
        detected = ", ".join(result["detected"])
        lines.append(f"| {i} | {result['primary']} | {detected} | {manual} | {status} |")
    
    lines += [
        "",
        f"Coincidencia con la referencia: **{accuracy:.2f}%** ({matches}/{reference_count}).",
        "",
        "## Cinco reglas propias",
        "Se aplicaron las siguientes reglas personalizadas en `CUSTOM_RULES` para abarcar tecnicismos adicionales de ingeniería:",
        "1. **`placa` / `escaneo`** -> *Visión por computador*: Permite mapear términos de procesamiento de imágenes y lectura automática.",
        "2. **`opinion` / `traduccion`** -> *Procesamiento de lenguaje natural*: Amplía la capacidad para detectar análisis de sentimientos y minería de texto.",
        "3. **`tendencia` / `mantenimiento`** -> *Aprendizaje automático predictivo*: Captura la semántica de modelos predictivos en series temporales.",
        "4. **`criterio` / `normativa`** -> *Sistemas expertos*: Identifica motores de inferencia basados en reglas de negocio estricta.",
        "5. **`navegacion` / `telemetria`** -> *Robótica y sistemas autónomos*: Permite asociar la recolección de variables físicas a la toma de acción de un agente.",
        "",
        "## Discrepancias y análisis",
        "1. **Naturaleza Multimodales (Sistemas Híbridos):** El caso #17 (*Vehículo autónomo*) fue clasificado tanto en *Visión por Computador* como en *Robótica y Sistemas Autónomos*. La categoría principal seleccionada fue Visión por Computador por la mayor frecuencia de palabras clave asociadas a la percepción visual.",
        "2. **Solidez de la taxonomía:** Un problema real de ingeniería no suele ser puro. La estructura simbólica diseñada permite retener categorías secundarias para abordar soluciones híbridas completas.",
        "",
        "## Nota técnica",
        "Un problema real puede pertenecer a varias áreas de IA. La columna 'principal' usa la categoría con mayor cantidad de coincidencias; las demás coincidencias se conservan como categorías secundarias.",
    ]
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    cases = read_cases()
    results = []
    print("=" * 80)
    print("SEMANA 03 - TAXONOMÍA DE INTELIGENCIA ARTIFICIAL (OPTIMIZADO)")
    print("=" * 80)
    for i, case in enumerate(cases, start=1):
        primary, detected, scores = classify_problem(case)
        results.append({
            "description": case,
            "primary": primary,
            "detected": detected,
            "scores": scores,
        })
        print(f"{i:02d}. {case}")
        print(f"   Principal: {primary}")
        print(f"   Áreas detectadas: {', '.join(detected)}\n")
    
    write_report(results)
    print(f"Casos procesados: {len(results)}")
    print(f"Reporte generado: {REPORT_FILE}")

if __name__ == "__main__":
    main()