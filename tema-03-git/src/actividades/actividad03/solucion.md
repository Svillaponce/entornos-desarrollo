# Actividad 3 — Un commit equivocado y varios cambios pendientes

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Registrar `incidencias.py` y el README iniciales juntos. El enunciado enumera ambos archivos y después exige modificar el README versionado.
2. Aplicar los cambios A y B, preparar ambos y retirar únicamente README con `git restore --staged README.md`.
3. Confirmar el código con el mensaje deliberadamente incorrecto `cosas`. Revisar que el índice esté vacío y corregirlo con `git commit --amend -m ...`.
4. Confirmar el README por separado.
5. Crear PLAN y registrar `Plan provisional`; ejecutar `git reset --soft HEAD~1`, comprobar que PLAN aparece preparado (`A `) y confirmar con `Documentar futuras mejoras`.
6. Introducir la línea de fallo, inspeccionar `git diff` y ejecutar `git restore incidencias.py` para descartar solo esa edición no preparada.
7. Ejecutar el listado de tres incidencias numeradas y comprobar el estado final.

## Respuestas

`restore --staged` modifica el índice, conserva el archivo en disco y no mueve HEAD. `restore archivo` sustituye el contenido no preparado por el del índice: por eso primero se revisa el diff. `reset --soft HEAD~1` mueve la rama al commit anterior y conserva el índice y el directorio de trabajo.

`--amend` reemplaza el último commit: cambia su hash, sin añadir un commit más a la cadena final. El historial final de `main` contiene **cuatro commits**, sin los mensajes `cosas` ni `Plan provisional`. Los commits sustituidos pueden seguir en el reflog; no se han borrado de la base de objetos inmediatamente. La salida final contiene Pantalla rota, Impresora sin papel y Red sin conexión, numeradas del 1 al 3.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-03-incidencias
cd git-03-incidencias
```

Si todavía no tienes configurada una identidad de Git, después de inicializar
el repositorio ejecuta `git config user.name "Tu nombre"` y
`git config user.email "tu-correo@example.com"`. Estos ajustes serán locales.
Antes de cada commit se revisan el estado y los cambios preparados.
Las salidas de referencia proceden de una ejecución comprobada; los mensajes
pueden variar entre Windows y Ubuntu.

```bash
git init -b main
```

Editar `incidencias.py` en PyCharm y guardar este contenido completo:

```python
INCIDENCIAS = ["Pantalla rota", "Impresora sin papel"]

def listar():
    for incidencia in INCIDENCIAS:
        print(incidencia)

if __name__ == "__main__":
    listar()
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Incidencias
Listado de incidencias técnicas.
```

```bash
git add incidencias.py README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
A  incidencias.py
```

```bash
git diff --staged
```

```bash
git commit -m "Crear listado de incidencias"
```

Editar `incidencias.py` en PyCharm y guardar este contenido completo:

```python
INCIDENCIAS = ["Pantalla rota", "Impresora sin papel", "Red sin conexión"]

def listar():
    for indice, incidencia in enumerate(INCIDENCIAS, start=1):
        print(f"{indice}. {incidencia}")

if __name__ == "__main__":
    listar()
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Incidencias
Listado de incidencias técnicas.
Las incidencias se muestran numeradas.
```

```bash
git add incidencias.py README.md
```

```bash
git diff --staged
```

```bash
git restore --staged README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
M  incidencias.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
M  incidencias.py
```

```bash
git diff --staged
```

```bash
git commit -m cosas
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
```

```bash
git diff --staged
```

```bash
git commit --amend -m "Numerar incidencias y añadir fallo de red"
```

```bash
git add README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  README.md
```

```bash
git diff --staged
```

```bash
git commit -m "Documentar listado numerado"
```

Editar `PLAN.md` en PyCharm y guardar este contenido completo:

```text
# Plan de mejora
- Incorporar prioridad de incidencias.
- Añadir un filtro por estado.
```

```bash
git add PLAN.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  PLAN.md
```

```bash
git diff --staged
```

```bash
git commit -m "Plan provisional"
```

```bash
git reset --soft HEAD~1
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  PLAN.md
```

```bash
git diff --staged
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  PLAN.md
```

```bash
git diff --staged
```

```bash
git commit -m "Documentar futuras mejoras"
```

Editar `incidencias.py` en PyCharm y guardar este contenido completo:

```python
INCIDENCIAS = ["Pantalla rota", "Impresora sin papel", "Red sin conexión"]

def listar():
    for indice, incidencia in enumerate(INCIDENCIAS, start=1):
        print(f"{indice}. {incidencia}")

if __name__ == "__main__":
    listar()

print("FALLO DE PRUEBA")
```

```bash
git diff
```

Salida de referencia (los hashes pueden variar):

```text
diff --git a/incidencias.py b/incidencias.py
index cde4408..2ac9cf7 100644
--- a/incidencias.py
+++ b/incidencias.py
@@ -6,3 +6,5 @@ def listar():
 
 if __name__ == "__main__":
     listar()
+
+print("FALLO DE PRUEBA")
```

```bash
git restore incidencias.py
```

```bash
python3 incidencias.py
```

Salida de referencia (los hashes pueden variar):

```text
1. Pantalla rota
2. Impresora sin papel
3. Red sin conexión
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* 3568d23 (HEAD -> main) Documentar futuras mejoras
* 08be5f3 Documentar listado numerado
* 3abe03e Numerar incidencias y añadir fallo de red
* c4d738d Crear listado de incidencias
```

```bash
git status --porcelain
```

```bash
git status
```

Salida de referencia (los hashes pueden variar):

```text
On branch main
nothing to commit, working tree clean
```

## Informe y comprobación de entrega

Al realizar la práctica, copia al `INFORME.md` que pide el enunciado las respuestas
y las evidencias indicadas en este documento, usando las salidas y hashes de tu
propia ejecución. No confirmes ese informe. Para que el informe local no aparezca
como archivo nuevo en `git status`, puedes excluirlo solo en este repositorio:

```bash
printf '\n/INFORME.md\n' >> .git/info/exclude
git status
git log --oneline --graph --all --decorate
```

El código debe estar limpio y no debe quedar una fusión pendiente. Este
`solucion.md` reúne la explicación y las respuestas; no es necesario añadir
otros documentos explicativos al repositorio de clase.
