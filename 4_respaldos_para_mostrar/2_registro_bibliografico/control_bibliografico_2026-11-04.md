# Control bibliográfico final (4 de noviembre de 2026)

Observación menor 6 del informe de verificación del jurado 1 (3 de noviembre): ejecutar un último control cita-referencia
y verificar DOI/URL antes del depósito. Privado; se exhibe al tribunal a su solicitud.

## Qué se controló y cómo

1. **Citas y referencias.** Fuentes del gestor de referencias del documento (parte `customXml`, lista de fuentes) frente a las
   etiquetas de todos los campos de cita del cuerpo, incluidas las citas fusionadas (un campo con dos o más fuentes).
   Script de control del autor (`citadas.py`, fuera del repositorio público) sobre la copia limpia entregable.
2. **Enlaces.** Para cada fuente con DOI o URL y para cada URL de la bibliografía de apoyo, una petición HTTP (HEAD y, si
   hace falta, GET) y el código de respuesta. Script de control del autor (`control_biblio.py`, fuera del repositorio
   público); resultados por enlace en el archivo `control_enlaces_2026-11-04.json` que acompaña a este resumen.
3. **DOI con bloqueo del editor.** Los DOI que el editor responde con 403 o 503 a consultas automáticas se verificaron uno
   por uno en el registro Crossref (`https://api.crossref.org/works/<doi>`), que devuelve los metadatos de la obra.

## Resultado

| Control | Resultado |
|---|---|
| Fuentes en el gestor | 62 |
| Campos de cita en el cuerpo | 183 (citas fusionadas: 11) |
| Fuentes sin ninguna cita | 0 |
| Citas sin fuente en el gestor | 0 |
| Enlaces probados (DOI y URL) | 110 |
| Enlaces con respuesta 2xx o 3xx | 88 |
| DOI distintos con 403 o 503 del editor | 12, todos confirmados en Crossref |
| Fuentes sin DOI ni URL (libros, normas y leyes) | 11 |

## DOI con bloqueo del editor, confirmados en Crossref

| DOI | Código HTTP | Dónde aparece | Verificación |
|---|---|---|---|
| https://doi.org/10.1002/9781119135289 | 403 | fuente Boy21 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1002/9781119199885 | 403 | fuente Gil10 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1057/jors.1969.103 | 403 | fuente Bat69 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1057/jors.1972.50 | 403 | fuente Cro72 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1057/palgrave.jors.2601841 | 403 | fuente SBC05 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1080/00031305.2017.1380080 | 403 | fuente Tay18 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1080/01621459.1975.10480264 | 403 | fuente BoT75 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1145/2523813 | 403 | fuente Gam14 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1145/2939672.2939785 | 403 | fuente Che16 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1145/3292500.3330701 | 403 | fuente Aki19 y bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1201/9781003399599 | 503 | bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |
| https://doi.org/10.1201/9781315374406 | 503 | bibliografía de apoyo | confirmado en Crossref (api.crossref.org/works) |

Nota. El campo `fuentes_no_citadas` del archivo JSON proviene de un conteo simplificado que no distingue las citas fusionadas;
el resultado válido es el de `fmt/citadas.py`, reproducido arriba: ninguna fuente sin cita y ninguna cita sin fuente.
