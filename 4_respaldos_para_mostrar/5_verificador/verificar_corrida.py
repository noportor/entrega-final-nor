"""Verificación de las corridas entregadas contra el manifiesto expurgado.

Se guarda FUERA del repositorio (si se copia dentro, git lo ve como archivo nuevo
y el árbol deja de estar limpio). Uso, desde la carpeta motor-pronostico de un
clon del repositorio en el commit de las corridas, con los insumos bajo
custodia en datos/crudo y las salidas de cada corrida en su carpeta:
    git checkout 472b891
    python -X utf8 <ruta>/verificar_corrida.py .              (corrida publicada)
    python -X utf8 <ruta>/verificar_corrida.py . a            (sensibilidad A)
    python -X utf8 <ruta>/verificar_corrida.py . b            (sensibilidad B)
    python -X utf8 <ruta>/verificar_corrida.py . v9           (extensión, gestión 2026)
    python -X utf8 <ruta>/verificar_corrida.py . v9_blindaje  (extensión, gestión 2025)
    python -X utf8 <ruta>/verificar_corrida.py . v5           (opcional, respaldo de la auditoría)
    python -X utf8 <ruta>/verificar_corrida.py . v6           (opcional, respaldo de la auditoría)
Las corridas de la extensión (v9 y v9_blindaje; v5 y v6, opcionales) se
ejecutaron fuera del contenedor, con GPU: se verifica la integridad de lo
sellado, no su repetición bit a bit.
Imprime sólo hashes, conteos y agregados; nunca una fila.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ESPERADO_CRUDO = {
    "ventas_novapack.csv": (11430061, "5d1190ff295e769374ae6cbb51a3f300eddd31e62834789ffd099ad70d2f83aa"),
    "costos.csv": (152700, "6dc7e86c94bbd4d0781d3dc0c694d06b2c94524f0d6229f3a9d4631b0e7c1f0e"),
    "quiebres.csv": (7355431, "0d51d4ef35399b135a7d42c66597ad062aa08295637027b2b60413d7b5215d95"),
    "tipo_cambio.csv": (790, "354c695488f5f2ec885a0cca764737bcc6d02fe7c1abf4a5387aca5e14f009a8"),
    "mapeo_sku.csv": (17483, "86e633a356a6047a009c0fd5da11af0be5af20b4d2ba51197838d4189e5aaba1"),
    "manifiesto_extraccion.json": (1503, "262f4d366c756086f5a72d594a374958cc6064da737a136841f9e9fceb885238"),
    "mapeo_categoria.csv": (364, "8ce2a16f975cfb4a01687fb42a4a7548f8c90fbd6c7f44b90a7a675d328fa294"),
}
# Las corridas se ejecutaron sobre el mismo commit, con el árbol limpio.
COMMIT_CORRIDAS = "472b891eca2998e3ec55a8a49511032be388bf96"
# variante: (carpeta de salidas, archivo de configuración, hash efectivo esperado, sellada)
# Las selladas figuran en el manifiesto expurgado. Las opcionales (sellada False) no tienen
# hash esperado: su configuración se compara con la versionada en el commit.
VARIANTES = {
    "publicada": ("salidas", "config/config.yaml",
                  "a69d9111303f78ef40520be02c8b40e8b0ff0cfc2291ae15650ea3a781aa9c22", True),
    "a": ("salidas_sensibilidad_a", "config/config_sensibilidad_a.yaml",
          "9cdab9ba10916b29fccd32ff56ee0830745643acf999d4ea8997a0c10f69b705", True),
    "b": ("salidas_sensibilidad_b", "config/config_sensibilidad_b.yaml",
          "1c9922f863be75fc12229f66583e19ceeb38d918148043c0a36783a0d3df3bdb", True),
    "v9": ("salidas_ml2_v9", "config/config_ml2_v9.yaml",
           "2550c63bf5634b30f580c47ca8d29ca7ed06f990fb6c8898a3366d91177ddec1", True),
    "v9_blindaje": ("salidas_ml2_v9_blindaje", "config/config_ml2_v9_blindaje.yaml",
                    "5174160382f016008e846152414ec7edf07d6348cfc26eb5eab9ce26a0d648b8", True),
    "v5": ("salidas_ml2_v5", "config/config_ml2_v5.yaml",
           None, False),
    "v6": ("salidas_ml2_v6", "config/config_ml2_v6.yaml",
           None, False),
}


def sha(ruta: Path) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def git(raiz: Path, *args: str):
    """Salida de git, o None si no hay git o la carpeta no es un clon."""
    try:
        r = subprocess.run(["git", "-C", str(raiz), *args],
                           capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


raiz = (Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")).resolve()
variante = sys.argv[2].lower() if len(sys.argv) > 2 else "publicada"
if variante not in VARIANTES:
    sys.exit(f"variante desconocida: {variante} ({', '.join(VARIANTES)})")
carpeta, archivo_config, esperado_config, sellada = VARIANTES[variante]
fallas = 0
print(f"Corrida: {variante} (carpeta {carpeta}, commit {COMMIT_CORRIDAS[:7]})"
      + ("" if sellada else "; opcional, no sellada en el manifiesto expurgado"))

print("1. Insumos de datos/crudo")
for nombre, (bytes_esp, hash_esp) in ESPERADO_CRUDO.items():
    p = raiz / "datos" / "crudo" / nombre
    ok = p.exists() and p.stat().st_size == bytes_esp and sha(p) == hash_esp
    fallas += not ok
    print(f"   {'OK ' if ok else 'MAL'} {nombre}")

ruta_m = raiz / carpeta / "manifiesto.json"
if not ruta_m.exists():
    sys.exit(f"MAL no existe {carpeta}/manifiesto.json")
m = json.loads(ruta_m.read_text(encoding="utf-8"))
sellos = {"ventas_novapack.csv": (m["datos"]["bytes"], m["datos"]["sha256"])}
sellos.update({a["archivo"]: (a["bytes"], a["sha256"]) for a in m["datos"].get("auxiliares", [])})
ok = sellos == ESPERADO_CRUDO
fallas += not ok
print(f"   {'OK ' if ok else 'MAL'} el manifiesto sella los mismos {len(sellos)} insumos")

print("2. Código")
modificados = list(m["codigo"].get("archivos_modificados", []))
ok = (m["codigo"]["commit"] == COMMIT_CORRIDAS and m["codigo"]["arbol_limpio"] is True
      and modificados == [])
fallas += not ok
print(f"   {'OK ' if ok else 'MAL'} manifiesto: commit {m['codigo']['commit'][:7]}, "
      f"árbol limpio {m['codigo']['arbol_limpio']}, archivos modificados {len(modificados)}")
head = git(raiz, "rev-parse", "HEAD")
if head is None:
    print("   AVISO sin git en esta carpeta: el commit del código se verifica a mano (paso 1)")
else:
    estado = git(raiz, "status", "--porcelain", "--", ".")
    ok = head == COMMIT_CORRIDAS and estado == ""
    fallas += not ok
    print(f"   {'OK ' if ok else 'MAL'} clon: HEAD {head[:7]} (se espera {COMMIT_CORRIDAS[:7]}), "
          f"{'sin cambios' if estado == '' else 'con cambios sin commitear'}"
          + ("" if head == COMMIT_CORRIDAS else f"; antes: git checkout {COMMIT_CORRIDAS[:7]}"))

print("3. Configuración (hash del contenido efectivo)")
contenido = m["configuracion"]["contenido"]
volcado = json.dumps(contenido, sort_keys=True, ensure_ascii=False, default=str)
h_manifiesto = hashlib.sha256(volcado.encode("utf-8")).hexdigest()
anulaciones = list(contenido.get("_anulaciones", []))
sys.path.insert(0, str(raiz))
from src.config import cargar_config  # noqa: E402
h_archivo = cargar_config(raiz / archivo_config, anulaciones=anulaciones or None).hash_configuracion()
ok = (h_manifiesto == h_archivo == m["configuracion"]["sha256"]
      and (esperado_config is None or h_archivo == esperado_config))
fallas += not ok
print(f"   {'OK ' if ok else 'MAL'} {h_archivo[:12]} ({archivo_config}"
      f"{', anulaciones: ' + ', '.join(anulaciones) if anulaciones else ''})")

print("4. Salidas selladas en el manifiesto")
malas = []
for s in m["salidas"]:
    p = raiz / carpeta / s["archivo"]
    if not (p.exists() and p.stat().st_size == s["bytes"] and sha(p) == s["sha256"]):
        malas.append(s["archivo"])
fallas += bool(malas)
print(f"   {len(m['salidas']) - len(malas)} de {len(m['salidas'])} coinciden; distintas: {malas}")

print("5. Agregados")
c = m["resultados"]["cohorte"]
print(f"   cohorte {c['series_iniciales']} -> {c['series_finales']}")
for v in m["resultados"]["valorizado"]:
    print(f"   D {v['modelo']:<15} {v['D']:.1f}  (series con costo {v['series_con_costo']})")
print(f"   duración {m['duracion_segundos']} s")
print("RESULTADO:", "todo coincide" if fallas == 0 else f"{fallas} controles fallaron")
sys.exit(1 if fallas else 0)
