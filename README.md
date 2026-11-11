# Respuesta al informe del tribunal evaluador del 9 de noviembre de 2026

Guía de esta carpeta. Está escrita para quien la abre sin conocer el trabajo ni su historia: dice qué es cada cosa, en qué orden leerla y cómo comprobar lo que se afirma sin salir de la carpeta.

## 1. De qué se trata

- **El trabajo.** Trabajo final de grado (TFG) «Diseño de un motor de pronóstico de demanda basado en series temporales para mejorar la precisión de la planificación de la demanda en NOVAPACK S.A. para la gestión 2026», de Nicolas Oporto Rojas. Maestría en Ciencia de Datos e Inteligencia Artificial, UAGRM School of Engineering (Universidad Autónoma «Gabriel René Moreno»).
- **La empresa.** NOVAPACK S.A. es un seudónimo. El trabajo, su repositorio y esta guía nombran a la empresa solo así, y a sus personas solo por su rol.
- **El informe.** El 9 de noviembre de 2026, un miembro del tribunal evaluador (M.Sc. Edgar Jaldin Torrico) emitió su informe después de cotejar la versión anterior del trabajo (317 páginas), la matriz de respuesta anterior y el repositorio público de código. Su Anexo I trae seis observaciones, de S2-01 a S2-06, y este dictamen: «mantener la habilitación condicionada y autorizar la defensa únicamente después del cierre documental de S2-01 y del cotejo en acta de S2-06». Pide como respuesta una matriz con cinco columnas: código, corrección realizada, ubicación exacta, commit o archivo de respaldo y evidencia exhibida.
- **La respuesta.** Es lo que reúne esta carpeta: el trabajo corregido (versión del 10 de noviembre de 2026, 320 páginas), la matriz de respuesta, los respaldos que el informe pide exhibir y una copia del repositorio público.
- **El estado.** La respuesta está completa. La matriz acepta las seis observaciones. Las correcciones son de texto y ya están en el trabajo; ninguna toca el código, las corridas ni las cifras, y el repositorio no tiene commits nuevos. Los respaldos que la observación S2-06 pide exhibir están en esta carpeta; de los nueve documentos firmados, que conserva el autor, están el texto y la fecha de firma. No queda nada por corregir ni por aportar. Lo que resta es el acto que el propio dictamen pide y que no puede ocurrir dentro de una carpeta: una sesión presencial en la que quien verifica ve los originales firmados y firma el acta. Por eso el acta de esta carpeta está en blanco.

Todo lo que hay en esta carpeta son copias. Los archivos de trabajo y los originales firmados, que están en papel, los conserva el autor. La carpeta se armó el 11 de noviembre de 2026.

## 2. Qué hay en cada carpeta

| Carpeta o archivo | Contenido |
|---|---|
| `1_enviar_a_Jaldin/` | Lo que se envía al evaluador. `TFG_NICOLAS_OPORTO_2026-11-10.pdf` es el trabajo corregido y el `.docx` del mismo nombre, el mismo trabajo en Word. `Matriz_respuesta_jurado1_Jaldin_2026-11-10.docx` es la matriz de respuesta |
| `2_llevar_a_la_facultad/` | Lo que se lleva a la sesión de verificación. `Acta_verificacion_documental_para_firma` (`.pdf` y `.docx`) es el acta de cotejo, de una página, en blanco. `lamina_resultado_principal_2026-11-10.pptx` es la lámina de defensa |
| `3_informe_del_jurado_2026-11-09/` | El informe que se responde, tal como se recibió. Las observaciones están en su Anexo I |
| `4_respaldos_para_mostrar/` | Los respaldos que la observación S2-06 pide exhibir, en el orden en que los nombra. Es material reservado (sección 8) |
| `5_repositorio_publico/` | Una copia del repositorio público de código, su historia completa y el registro de sus commits |

### Dentro de `4_respaldos_para_mostrar/`

| Subcarpeta | Contenido |
|---|---|
| `1_papeles_firmados_van_en_papel/` | Los documentos firmados existen en papel y no están en esta carpeta, pero se pueden revisar igual: `formatos_impresos_sin_firmar/` trae el texto de los nueve, en los archivos de Word de donde se imprimieron, y entre ellos está el índice, con la fecha de firma de cada uno. `anexo_de_la_constancia_08/` trae el archivo de diferencias entre dos commits que acompaña a esa constancia |
| `2_registro_bibliografico/` | El control de citas y referencias del 4 de noviembre de 2026: el registro (`.docx` y `.md`) y el resultado enlace por enlace (`.json`) |
| `3_lamina_de_defensa/` | La misma lámina de `2_llevar_a_la_facultad/` |
| `4_manifiestos/` | `Manifiesto_expurgado_corrida.docx` y, en una subcarpeta por corrida, su `manifiesto.json` |
| `5_verificador/` | `verificar_corrida.py`, que comprueba una corrida contra su manifiesto |
| `6_huellas/` | `huellas_sha256.txt`: la huella de cada archivo de `4_respaldos_para_mostrar/` |
| `7_salidas/` | Una subcarpeta por corrida, con todos sus archivos de salida y su `manifiesto.json` |
| `8_imagen_de_ejecucion/` | La imagen de Docker de las corridas, exportada (`.tar`), con su registro (`10_Registro_imagen_ejecucion.md`), su huella y las salidas de `docker image inspect` y `docker history` |

Los nueve documentos firmados. La Tabla 47 del trabajo (Anexo 18) es el índice de documentos bajo custodia:

| Archivo de `formatos_impresos_sin_firmar/` | Documento | Tabla 47 | Fecha de firma |
|---|---|---|---|
| `01a_Formulario_juicio_experto_juez1.docx` | Formulario de validación por juicio de experto, juez 1 | Fila 1 | 19 de octubre de 2026 |
| `01b_Formulario_juicio_experto_juez2.docx` | Formulario de validación por juicio de experto, juez 2 | Fila 2 | 20 de octubre de 2026 |
| `02_Consentimiento_informado_entrevista.docx` | Consentimiento informado de la entrevista | Fila 3 | 16 de octubre de 2026 |
| `03_Autorizacion_observacion_estructurada.docx` | Autorización de la observación estructurada | Fila 4 | 16 de octubre de 2026 |
| `04_Constancia_empresa_autorizacion_y_revision_repositorio.docx` | Constancia de la empresa | Fila 5 | 20 de octubre de 2026 |
| `07_Acuerdo_confidencialidad_para_firma.docx` | Acuerdo de confidencialidad, que el Anexo 2 del trabajo transcribe con el seudónimo | Fila 6 | 20 de octubre de 2026 |
| `05_Indice_de_custodia.docx` | Índice de documentos bajo custodia | Es el índice mismo | 22 de octubre de 2026 |
| `08_Constancia_cambios_documentales.docx` | Constancia complementaria 08 | No es una fila | 4 de noviembre de 2026 |
| `09_Constancia_conservacion_respaldos.docx` | Constancia complementaria 09 | No es una fila | 4 de noviembre de 2026 |

De dónde sale cada fecha. Las de las filas 1 a 6 son las del índice (`05_Indice_de_custodia.docx`), que la Tabla 47 del trabajo reproduce (páginas 298 y 299). La del índice es la que lleva impresa al pie. La de las dos constancias complementarias, posteriores al cierre del índice, consta en la nota de la Tabla 47 (página 299) y en la fila S2-05e de la matriz.

Cómo se revisan sin el papel. El texto de cada documento está en su formato, y su fecha de firma y el rol de quien lo firma constan en el índice. Con eso se comprueba qué dice cada documento, quién lo firma y cuándo, y se coteja con lo que el trabajo y la matriz afirman de él. Los formatos van sin firma y con la fecha en blanco porque eso se escribe a mano en el papel, que se exhibe en la sesión de verificación.

Las filas 7 a 9 de la Tabla 47 son archivos. La fila 7 es el manifiesto expurgado y el verificador (`4_manifiestos/` y `5_verificador/`). La fila 8 es la captura de datos, que no está en esta carpeta. La fila 9 son las salidas (`7_salidas/`).

Las cinco corridas. Los nombres de carpeta son los del repositorio:

| Carpeta | Corrida | Salidas que sella su manifiesto |
|---|---|---|
| `salidas` | Publicada | 45 |
| `salidas_sensibilidad_a` | Sensibilidad A | 45 |
| `salidas_sensibilidad_b` | Sensibilidad B | 45 |
| `salidas_ml2_v9` | Extensión exploratoria V9 | 46 |
| `salidas_ml2_v9_blindaje` | Extensión exploratoria V9 con blindaje | 46 |

Cada carpeta trae además su `manifiesto.json`. La carpeta `salidas` trae otros cinco archivos que su manifiesto no sella: `.gitkeep` y cuatro figuras (`figura08_microservicio.png`, `figura_arquitectura_motor.png`, `figura_proceso_propuesto.png` y `figura_reparto_seleccion.png`).

### Dentro de `5_repositorio_publico/`

- `tfg-motor-pronostico-demanda/`: los 179 archivos del repositorio en su último commit publicado (f799b56), sin la carpeta `.git`.
- `tfg-motor-pronostico-demanda.bundle`: el repositorio completo, con sus 73 commits, en un solo archivo. Se abre con `git clone`.
- `historial_git.txt`: el registro de los 73 commits, primero un renglón por commit y después cada commit completo.

El repositorio original está publicado en https://github.com/noportor/tfg-motor-pronostico-demanda, con una sola rama, `master`. Es público: se clona con `git clone` sin iniciar sesión y sin credenciales. Así se comprobó el 11 de noviembre de 2026, y el clon dio el mismo commit (f799b56) y los mismos 73 commits que la copia de esta carpeta, que se bajó de ahí ese día. El paso 9 de la sección 6 lo repite.

## 3. En qué orden leer

1. El Anexo I del informe: las seis observaciones y el dictamen.
2. La matriz. Empieza con unos párrafos de contexto (versión del trabajo, estado del repositorio, sesión de verificación) y sigue con una fila por observación. La observación S2-05 ocupa seis filas, de S2-05a a S2-05f.
3. Para cada fila, lo que cita: las páginas del trabajo, los archivos del repositorio y los respaldos.

Una revisión completa comprueba, fila por fila:

- que el texto corregido está en la página que la fila cita;
- que cada archivo y cada línea del repositorio dicen lo que la fila afirma, en el commit que indica;
- que cada huella citada coincide con el archivo de esta carpeta;
- que cada evidencia nombrada está en esta carpeta o figura en la sección 7.

El repositorio no se modificó en esta ronda. Por eso conserva, en comentarios, en los README y en las salidas selladas, la redacción anterior de algunos pasajes que el trabajo ya corrigió. La matriz los lista uno por uno, con archivo y línea, después de las palabras «No se modifican y se declaran», y explica por qué quedan así. Encontrarlos no es una discrepancia nueva.

## 4. Qué pide cada observación y dónde comprobar la respuesta

| Código | Qué pide el informe | Dónde comprobar, además de las páginas del trabajo que cita la fila |
|---|---|---|
| S2-01 | Cotejar en acta, con los originales, el alcance de cada ratificación y de la autorización institucional e individual. Corregir la frase de la página 140 que atribuye el acceso al acuerdo de confidencialidad | El texto de cada documento, en `4_respaldos_para_mostrar/1_papeles_firmados_van_en_papel/formatos_impresos_sin_firmar/`, y su fecha de firma, en el índice de esa misma carpeta y en la Tabla 47. Los originales se exhiben en la sesión |
| S2-02 | Precisar el alcance de la cohorte A: es una sensibilidad retrospectiva y no una cohorte seleccionada enteramente al origen; B es la más estricta | La lámina de defensa. El código de `src/particion.py` en el commit 472b891. El flujo sellado de A: `7_salidas/salidas_sensibilidad_a/cohorte_flujo.csv` |
| S2-03 | Ajustar tres pasajes sobre multiplicidad y valores p, y explicar por estimador qué intervalo excluye o no el cero | En el repositorio, `resultados/tablas/tabla_H3_incertidumbre_agrupada.csv` (Tabla 20) y `tabla_H4_incertidumbre_extension.csv` (Tabla 21) |
| S2-04 | Exhibir la constancia 08, los manifiestos, las salidas y la imagen exacta de ejecución. El Dockerfile por sí solo no prueba el identificador de la imagen | `4_manifiestos/`, `5_verificador/`, `7_salidas/` y `8_imagen_de_ejecucion/`, y el archivo de diferencias de la constancia 08 |
| S2-05 | Ajustes formales: «proximidad causal» y «efectos» (a y b), «permitirá» como expectativa (c), los 110 DOI y URL (d), las constancias 08 y 09 (e) y la grafía «Nicolas» (f) | Para (d), `2_registro_bibliografico/`. Para (e), las fuentes de la 08 y de la 09. Para (f), el documento de identidad y un documento del registro académico, que no están en esta carpeta |
| S2-06 | Exhibir consentimientos, autorizaciones, formularios, constancias 08 y 09, registro bibliográfico, lámina de defensa, manifiestos, verificador, huellas, salidas e imagen de ejecución, y registrar en acta qué se cotejó y su alcance | Todo `4_respaldos_para_mostrar/` y el acta en blanco de `2_llevar_a_la_facultad/` |

## 5. Cómo leer las citas

- **Páginas.** Son las impresas en el trabajo. El PDF no trae etiquetas de página. Las páginas preliminares van en romanos, de la I a la XVIII, y coinciden con la página del PDF. Desde la Introducción, la página impresa n es la página n + 18 del PDF: la 140 es la 158 del PDF y la última, la 302, es la 320.
- **Rutas del repositorio.** Son relativas a su carpeta `motor-pronostico/`, salvo cuando la matriz dice «de la raíz». En esta carpeta: `5_repositorio_publico/tfg-motor-pronostico-demanda/motor-pronostico/`.
- **Commits.** Son cuatro los que importan: 472b891, el de las corridas; 17893d4, el que revisó la empresa; 0d552eb y f799b56, los dos posteriores, que son documentales. La copia de archivos de esta carpeta es f799b56. Para ver un archivo en otro commit hay que abrir el `.bundle` (sección 6, paso 4).
- **«Sin commit».** En la matriz quiere decir que el respaldo es el archivo que la fila nombra.
- **Huella.** Es el SHA-256 del archivo.
- **Números de dos cifras.** De 01a a 10, son archivos de custodia. El 10 es el registro de la imagen de ejecución. «Fila n» es una fila de la Tabla 47.
- **Tablas 47 y 48.** Están en el Anexo 18, páginas 298 a 302. La Tabla 47 es el índice de documentos bajo custodia. La Tabla 48 trae los sellos de las corridas: el commit, el identificador de la imagen y las huellas de los manifiestos, de los insumos y de la Tabla 20.
- **Manifiesto.** Es el `manifiesto.json` que cada corrida escribe al terminar: commit del código, huella de la configuración, huellas de los insumos y de las salidas y resultados agregados. El manifiesto expurgado es un documento que transcribe esos sellos sin datos reservados.

## 6. Comprobaciones que se pueden repetir dentro de esta carpeta

Hace falta un intérprete de comandos POSIX (en Windows, Git Bash) con `git`, `sha256sum`, `tar`, `diff` y Python 3. Todo se corre desde la raíz de esta carpeta y nada escribe dentro de ella. Si `python` no abre Python 3, se usa `python3` o la ruta del intérprete.

**Paso 1. Las copias de respaldo están íntegras.** No tiene que imprimir ningún renglón.

```bash
(cd 4_respaldos_para_mostrar && sha256sum -c 6_huellas/huellas_sha256.txt | grep -v ': OK$')
```

**Paso 2. Las huellas que citan el trabajo y la matriz.** Tiene que decir `OK` en los catorce renglones. La primera es la huella del PDF, que la matriz cita en su encabezado. Las de los cinco `manifiesto.json` y la del archivo `tabla_H3` están impresas en la Tabla 48 del trabajo. Las demás las cita la matriz.

```bash
sha256sum -c - <<'FIN'
c3760d070a4fdca83db4671751d363546c83ed2324b1df64ebbb204b99482758  1_enviar_a_Jaldin/TFG_NICOLAS_OPORTO_2026-11-10.pdf
db1b7e8c9c7c590d9107536e65db3f6d7a39e8428a333b34d641680144bdba35  2_llevar_a_la_facultad/lamina_resultado_principal_2026-11-10.pptx
d2636cd4db5bd599fffc25b9011f0c7c6df724809fe29796465ef4fbdbe670a1  4_respaldos_para_mostrar/1_papeles_firmados_van_en_papel/anexo_de_la_constancia_08/diff_17893d4_a_f799b56_publicado.txt
05cbb56aa05a18092ebeb08b646474e3a3e2a3e20e6c4b3e2974d66531bf7607  4_respaldos_para_mostrar/2_registro_bibliografico/control_enlaces_2026-11-04.json
f29d7247bcecdf0976813b23537c0a5adf835c8c28515a9dcba0426bdc0b7928  4_respaldos_para_mostrar/2_registro_bibliografico/control_bibliografico_2026-11-04.docx
517ca40043c9c3ec452a888debf9d4fa26373b7f1d5c4c23e153c2c5a74b52f1  4_respaldos_para_mostrar/4_manifiestos/Manifiesto_expurgado_corrida.docx
ff3951cae7e265be6a160ba27d093b01b11438190ada336795a10fb3117dc374  4_respaldos_para_mostrar/4_manifiestos/salidas/manifiesto.json
f65be35b5e037bdd2f8bfe44da3586bad16da39b704d7e830d8a9aa28031d6e5  4_respaldos_para_mostrar/4_manifiestos/salidas_sensibilidad_a/manifiesto.json
02a5613571c8d01b412df265960f8952faf9508dc7f8cfe44ac99fde23420abb  4_respaldos_para_mostrar/4_manifiestos/salidas_sensibilidad_b/manifiesto.json
c0940a4eca15fbf47dc3c42cf99e56c21f546103df9b7b62f4f3aea1211ac1c3  4_respaldos_para_mostrar/4_manifiestos/salidas_ml2_v9/manifiesto.json
0fcae1db6aa269ba1e971e16c35fbdae614336a5a0fd9a3eb3839cf1237a182a  4_respaldos_para_mostrar/4_manifiestos/salidas_ml2_v9_blindaje/manifiesto.json
4af07cdb565eba6fefb7edd5eb4ecaf343afdba74feb458938804bccf3b5087b  4_respaldos_para_mostrar/5_verificador/verificar_corrida.py
92aeed5c78f4cfd7bc926db23542833781a5d0faa0b9311874f9ef3996c62c33  4_respaldos_para_mostrar/8_imagen_de_ejecucion/motor-pronostico_36118f8f.tar
1e3a8e96e80c192fd6c5d15908115c8a62fd888424118a4c415b6518330dd432  5_repositorio_publico/tfg-motor-pronostico-demanda/motor-pronostico/resultados/tablas/tabla_H3_incertidumbre_agrupada.csv
FIN
```

**Paso 3. Las salidas de cada corrida son las que sella su manifiesto.** Tiene que decir 45 de 45 en `salidas` y en las dos sensibilidades, 46 de 46 en las dos de la extensión, y en las cinco, commit 472b891 y árbol limpio `True`.

```bash
python - <<'FIN'
import hashlib, json, pathlib
base = pathlib.Path("4_respaldos_para_mostrar/7_salidas")
for d in sorted(p for p in base.iterdir() if p.is_dir()):
    m = json.loads((d / "manifiesto.json").read_text(encoding="utf-8"))
    bien = sum(1 for s in m["salidas"]
               if (d / s["archivo"]).is_file()
               and (d / s["archivo"]).stat().st_size == s["bytes"]
               and hashlib.sha256((d / s["archivo"]).read_bytes()).hexdigest() == s["sha256"])
    print(d.name, "|", bien, "de", len(m["salidas"]), "salidas coinciden | commit", m["codigo"]["commit"][:7],
          "| árbol limpio:", m["codigo"]["arbol_limpio"])
FIN
```

**Paso 4. El repositorio.** Se abre el `.bundle` en una carpeta temporal. Tiene que dar el commit `f799b5635feb471953618b2023296c7cc0213e4b` y 73 commits, y `diff` no tiene que imprimir nada: la copia de archivos es ese commit.

```bash
TMP=$(mktemp -d)
git clone -q -c core.autocrlf=false 5_repositorio_publico/tfg-motor-pronostico-demanda.bundle "$TMP/repo"
git -C "$TMP/repo" rev-parse HEAD
git -C "$TMP/repo" rev-list --count HEAD
diff -r --exclude=.git "$TMP/repo" 5_repositorio_publico/tfg-motor-pronostico-demanda
```

**Paso 5. Una cita de código en otro commit y las diferencias de la constancia 08.** El primer comando muestra las líneas de `src/particion.py` que cita la fila S2-02, en el commit de las corridas; así se lee cualquier otra cita. El segundo tiene que dar la huella `d2636cd4db5bd599fffc25b9011f0c7c6df724809fe29796465ef4fbdbe670a1`, la misma del archivo de diferencias del paso 2. El tercero, `23 files changed, 62 insertions(+), 38 deletions(-)`.

```bash
git -C "$TMP/repo" show 472b891:motor-pronostico/src/particion.py | sed -n '186,194p'
git -C "$TMP/repo" diff 17893d4 f799b56 | sha256sum
git -C "$TMP/repo" diff --stat 17893d4 f799b56 | tail -1
```

**Paso 6. El verificador (opcional).** Necesita Python con `pandas` y `PyYAML`. Se corre sobre un clon en el commit de las corridas, con las salidas copiadas dentro.

```bash
git -C "$TMP/repo" checkout -q 472b891
cp -r 4_respaldos_para_mostrar/7_salidas/* "$TMP/repo/motor-pronostico/"
for v in publicada a b v9 v9_blindaje; do
  python -X utf8 -B 4_respaldos_para_mostrar/5_verificador/verificar_corrida.py "$TMP/repo/motor-pronostico" $v
done
```

En cada corrida tiene que imprimir esto:

- En el punto 1, `MAL` en los siete insumos, porque la captura de datos no está en esta carpeta, y después `OK  el manifiesto sella los mismos 7 insumos`.
- En los puntos 2 y 3, `OK` en el commit, en el estado del clon y en la configuración.
- En el punto 4, `45 de 45 coinciden` o `46 de 46 coinciden`, con la lista de distintas vacía.
- En el punto 5, los agregados del manifiesto. En la corrida publicada: `cohorte 4406 -> 1668` y, en el renglón `D motor`, 75.4.
- En la última línea, `RESULTADO: 7 controles fallaron`. Son los siete insumos ausentes. Según la matriz, con la captura en su lugar el verificador da «todo coincide» en las cinco corridas.

**Paso 7. El recuento del registro bibliográfico.** Tiene que decir `110 comprobaciones; 59 enlaces distintos; 44 DOI; 15 URL`, que son las cifras de la fila S2-05d.

```bash
python - <<'FIN'
import json
d = json.load(open("4_respaldos_para_mostrar/2_registro_bibliografico/control_enlaces_2026-11-04.json", encoding="utf-8"))["detalle"]
e = {x["enlace"] for x in d}
n = sum("doi.org" in x for x in e)
print(len(d), "comprobaciones;", len(e), "enlaces distintos;", n, "DOI;", len(e) - n, "URL")
FIN
```

**Paso 8. El identificador de la imagen exportada.** Los dos comandos tienen que mostrar `36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe`, el identificador de la Tabla 48. No hace falta Docker.

```bash
tar -xOf 4_respaldos_para_mostrar/8_imagen_de_ejecucion/motor-pronostico_36118f8f.tar index.json; echo
tar -xOf 4_respaldos_para_mostrar/8_imagen_de_ejecucion/motor-pronostico_36118f8f.tar blobs/sha256/36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe | sha256sum
```

**Paso 9. El repositorio original en GitHub (opcional; necesita internet).** Es el único paso que sale de esta carpeta. No pide usuario ni contraseña. El primer comando tiene que mostrar `f799b5635feb471953618b2023296c7cc0213e4b` seguido de `refs/heads/master`. Después del clon, los otros dos tienen que dar ese mismo commit y 73, igual que el paso 4.

```bash
git ls-remote https://github.com/noportor/tfg-motor-pronostico-demanda refs/heads/master
git clone -q https://github.com/noportor/tfg-motor-pronostico-demanda "$TMP/original"
git -C "$TMP/original" rev-parse HEAD
git -C "$TMP/original" rev-list --count HEAD
```

Al terminar se puede borrar la carpeta temporal: `rm -rf "$TMP"`.

## 7. Lo que no está en esta carpeta

- **Los originales firmados.** Están en papel y los conserva el autor, que los exhibe en la sesión de verificación. Su texto y sus fechas de firma sí están en esta carpeta (sección 2), así que se pueden revisar. Si un papel difiere de su archivo, vale el papel.
- **La captura de datos.** Son los siete archivos de `datos/crudo` (ventas y registros auxiliares) y están bajo custodia. Sus huellas constan en cada `manifiesto.json`, en el verificador y en la Tabla 48.
- **Las corridas opcionales v5 y v6.** El verificador las nombra como respaldo opcional; el manifiesto expurgado no las sella.
- **La carpeta compartida de custodia.** Guarda las copias escaneadas de los documentos firmados y los archivos. Se muestra en pantalla en la sesión.
- **El documento de identidad del autor y un documento del registro académico.** Se exhiben en la sesión, para la fila S2-05f.
- **El acta completa.** La de esta carpeta está en blanco: la completa y la firma quien verifica, en la sesión.

## 8. Material reservado

`4_respaldos_para_mostrar/` se exhibe al tribunal y no se publica ni se entrega en copia: así lo dicen la matriz y el acta. La carpeta trae un `.gitignore` que la excluye entera de cualquier repositorio. Al revisarla:

- `formatos_impresos_sin_firmar/` trae los nombres reales de la empresa y de los firmantes. No se copian ni se citan en ningún informe: se nombra a cada firmante por su rol, como hace el trabajo.
- `7_salidas/` trae resultados serie por serie. De esos archivos solo se informan huellas, conteos y agregados, nunca filas.
- El `.tar` de la imagen incluye archivos locales de configuración que el repositorio no versiona. No se entrega ni se publica.

Las demás carpetas no traen nombres reales: el trabajo, la matriz, el informe, el acta, la lámina y el repositorio usan el seudónimo.
