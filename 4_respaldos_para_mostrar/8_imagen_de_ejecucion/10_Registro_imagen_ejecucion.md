# Registro de la imagen de ejecución (archivo de custodia 10)

Trabajo final de grado «Diseño de un motor de pronóstico de demanda basado en series temporales para mejorar la precisión de la planificación de la demanda en NOVAPACK S.A. para la gestión 2026». Autor: Nicolas Oporto Rojas.

Fecha de este registro y de la exportación: 10 de noviembre de 2026. Es posterior a las corridas (19 de octubre de 2026). No reemplaza ni modifica ningún documento firmado, y no es una fila del índice de documentos bajo custodia (Tabla 47 del trabajo): lo complementa, como las constancias complementarias 08 y 09.

## Qué se conserva

- `motor-pronostico_36118f8f.tar`: 246.619.136 bytes; SHA-256 `92aeed5c78f4cfd7bc926db23542833781a5d0faa0b9311874f9ef3996c62c33`. Se obtuvo con `docker save motor-pronostico:latest -o motor-pronostico_36118f8f.tar` (Docker 29.9.2, almacén de imágenes containerd).
- El archivo tiene formato OCI. Su `index.json` apunta al índice de la imagen, `sha256:36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe`, que es el identificador de la Tabla 48 del trabajo. Ese índice apunta al manifiesto linux/amd64 `sha256:e0050318bc9081db3c547d9d9477359f6cabed566021eadde1b99dfd6218808a`, y este a la configuración `sha256:d5956bc8ffbcebc2e7b2ffce86a03aa7b9d119084e3fd1cd58f0fe2952235aa6` y a 17 capas.
- `docker_image_inspect.json` y `docker_history.txt`: salida de `docker image inspect` y de `docker history --no-trunc` al momento de exportar.
- `sha256.txt`: la huella del archivo exportado.

## Qué acredita y qué no

- Acredita la identidad de la imagen conservada. El identificador es la huella SHA-256 del índice de la imagen: cualquier cambio en su contenido lo cambia.
- La imagen se creó el 2026-10-14T18:38:46.814299324Z y su etiqueta se asignó por última vez el 2026-10-14T18:38:58.74900577Z (ambas en UTC), antes de las corridas del 19 de octubre de 2026.
- El manifiesto de cada corrida no registra el identificador de la imagen. Registra, en su bloque `dependencias`, la versión de Python, la plataforma y las versiones de las bibliotecas. El vínculo entre la imagen y las corridas publicada, A y B es esa coincidencia, valor por valor (Python 3.13.16; plataforma Linux con glibc 2.41; pandas 3.0.2; numpy 2.4.4; scipy 1.17.1; scikit-learn 1.8.0; matplotlib 3.10.8; lightgbm 4.7.0; scikit-posthocs 0.14.0; PyYAML 6.0.2), más las fechas. No es un sello criptográfico de la ejecución.
- El Dockerfile del repositorio (commit 472b891) parte de `python:3.13-slim`, una etiqueta y no una huella. En el equipo del autor esa etiqueta designa hoy una imagen del 5 de agosto de 2026, con Python 3.13.14, distinta de la base con la que se construyó la imagen de las corridas (capas del 4 y 5 de octubre de 2026, con Python 3.13.16). Reconstruir la imagen no reproduce el identificador: por eso se conserva la imagen. Para reproducir las tres corridas en contenedor se carga (`docker load`) y no se reconstruye; ninguna corrida se repitió para este registro.
- El código de las corridas no es la copia que guarda la imagen: lo aportó el repositorio montado en el contenedor, en el commit 472b891, con el árbol limpio, como sella cada manifiesto.
- Las dos corridas de la extensión (V9 y V9 con blindaje) se ejecutaron fuera de la imagen, en un entorno local con GPU (Python 3.12.13). De ellas se verifica la integridad de lo sellado, no su repetición.

## Reserva

La imagen es material reservado. La capa que copia la carpeta del proyecto incluye, además del código, dos archivos locales de configuración que el repositorio no versiona (la lista local de términos reservados y la configuración local de la extracción) y registros de corridas. Los datos y las salidas no están en la imagen: el archivo `.dockerignore` los excluye. Por eso el archivo exportado se exhibe y no se entrega ni se publica, y el autor lo conserva y lo elimina con la misma regla que la constancia complementaria 09 fija para sus copias de los respaldos.

## Cómo cotejarla

1. `sha256sum motor-pronostico_36118f8f.tar` da `92aeed5c78f4cfd7bc926db23542833781a5d0faa0b9311874f9ef3996c62c33`.
2. Sin Docker: `tar -xOf motor-pronostico_36118f8f.tar blobs/sha256/36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe | sha256sum` da `36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe`, el identificador de la Tabla 48.
3. Con Docker: `docker load -i motor-pronostico_36118f8f.tar` y `docker image inspect motor-pronostico:latest --format '{{.Id}}'`. Con el almacén containerd muestra `sha256:36118f8f20f3633d55608aa5bccb2ab8fc25c1117530a5ec515c07775df62dfe`. Con el almacén clásico puede mostrar la huella de la configuración, `sha256:d5956bc8ffbcebc2e7b2ffce86a03aa7b9d119084e3fd1cd58f0fe2952235aa6`, que el propio archivo permite cotejar.
4. Entorno: `docker run --rm --network none motor-pronostico:latest python -c "import sys,pandas,numpy,scipy,sklearn,matplotlib,lightgbm,scikit_posthocs,yaml;print(sys.version.split()[0],pandas.__version__,numpy.__version__,scipy.__version__,sklearn.__version__,matplotlib.__version__,lightgbm.__version__,scikit_posthocs.__version__,yaml.__version__)"`, frente al bloque `dependencias` del `manifiesto.json` de cada corrida.
