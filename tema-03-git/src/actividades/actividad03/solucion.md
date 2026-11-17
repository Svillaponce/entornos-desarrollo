# Actividad 3 — Un commit equivocado y varios cambios pendientes

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-03-incidencias
cd git-03-incidencias
git init -b main
```

En `incidencias.py`, guarda este contenido:

```python
INCIDENCIAS = ["Pantalla rota", "Impresora sin papel"]

def listar():
    for incidencia in INCIDENCIAS:
        print(incidencia)

if __name__ == "__main__":
    listar()
```

En `README.md`, guarda este contenido:

```text
# Incidencias
Listado de incidencias técnicas.
```

```bash
git add incidencias.py README.md
git status --short
```

Resultado:

```text
A  README.md
A  incidencias.py
```

```bash
git diff --staged
git commit -m "Crear listado de incidencias"
```

En `incidencias.py`, guarda este contenido:

```python
INCIDENCIAS = ["Pantalla rota", "Impresora sin papel", "Red sin conexión"]

def listar():
    for indice, incidencia in enumerate(INCIDENCIAS, start=1):
        print(f"{indice}. {incidencia}")

if __name__ == "__main__":
    listar()
```

En `README.md`, guarda este contenido:

```text
# Incidencias
Listado de incidencias técnicas.
Las incidencias se muestran numeradas.
```

```bash
git add incidencias.py README.md
git diff --staged
git restore --staged README.md
git status --short
```

Resultado:

```text
 M README.md
M  incidencias.py
```

```bash
git status --short
```

Resultado:

```text
 M README.md
M  incidencias.py
```

```bash
git diff --staged
git commit -m cosas
git status --short
```

Resultado:

```text
 M README.md
```

```bash
git diff --staged
git commit --amend -m "Numerar incidencias y añadir fallo de red"
git add README.md
git status --short
```

Resultado:

```text
M  README.md
```

```bash
git diff --staged
git commit -m "Documentar listado numerado"
```

En `PLAN.md`, guarda este contenido:

```text
# Plan de mejora
- Incorporar prioridad de incidencias.
- Añadir un filtro por estado.
```

```bash
git add PLAN.md
git status --short
```

Resultado:

```text
A  PLAN.md
```

```bash
git diff --staged
git commit -m "Plan provisional"
git reset --soft HEAD~1
git status --short
```

Resultado:

```text
A  PLAN.md
```

```bash
git diff --staged
git status --short
```

Resultado:

```text
A  PLAN.md
```

```bash
git diff --staged
git commit -m "Documentar futuras mejoras"
```

En `incidencias.py`, guarda este contenido:

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

Resultado:

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
python3 incidencias.py
```

Resultado:

```text
1. Pantalla rota
2. Impresora sin papel
3. Red sin conexión
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
* 3568d23 (HEAD -> main) Documentar futuras mejoras
* 08be5f3 Documentar listado numerado
* 3abe03e Numerar incidencias y añadir fallo de red
* c4d738d Crear listado de incidencias
```

```bash
git status
```

Resultado:

```text
On branch main
nothing to commit, working tree clean
```

## Respuestas

`restore --staged` modifica el índice, conserva el archivo en disco y no mueve HEAD. `restore archivo` sustituye el contenido no preparado por el del índice: por eso primero se revisa el diff. `reset --soft HEAD~1` mueve la rama al commit anterior y conserva el índice y el directorio de trabajo.

`--amend` reemplaza el último commit: cambia su hash, sin añadir un commit más a la cadena final. El historial final de `main` contiene **cuatro commits**, sin los mensajes `cosas` ni `Plan provisional`. Los commits sustituidos pueden seguir en el reflog; no se han borrado de la base de objetos inmediatamente. La salida final contiene Pantalla rota, Impresora sin papel y Red sin conexión, numeradas del 1 al 3.

## Evidencias solicitadas

Incluye en `INFORME.md` el historial final, el estado tras `reset --soft`, el estado final y la comparación entre las tres operaciones de recuperación. No añadas `INFORME.md` a ningún commit.
