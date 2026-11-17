# Actividad 1 — El primer historial de una agenda

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-01-agenda
cd git-01-agenda
git init -b main
```

En `agenda.py`, guarda este contenido:

```python
CONTACTOS = ["Ana", "Luis", "Marta"]

def mostrar():
    for contacto in CONTACTOS:
        print(contacto)

if __name__ == "__main__":
    mostrar()
```

En `README.md`, guarda este contenido:

```text
# Agenda
Aplicación Python para mostrar una lista de contactos.
```

```bash
git status --short
```

Resultado:

```text
?? README.md
?? agenda.py
```

```bash
git add agenda.py
git status --short
```

Resultado:

```text
A  agenda.py
?? README.md
```

```bash
git diff --staged
git commit -m "Crear listado inicial de contactos"
git status --short
```

Resultado:

```text
?? README.md
```

```bash
git add README.md
git status --short
```

Resultado:

```text
A  README.md
```

```bash
git diff --staged
git commit -m "Documentar la agenda"
```

En `agenda.py`, guarda este contenido:

```python
CONTACTOS = ["Ana", "Luis", "Marta", "Pablo"]

def mostrar():
    for contacto in CONTACTOS:
        print(contacto)

if __name__ == "__main__":
    mostrar()
```

En `README.md`, guarda este contenido:

```text
# Agenda
Aplicación Python para mostrar una lista de contactos.
Permite incorporar contactos al listado.
```

```bash
git add agenda.py
git status --short
```

Resultado:

```text
 M README.md
M  agenda.py
```

```bash
git diff --staged
git commit -m "Añadir a Pablo a los contactos"
git add README.md
git status --short
```

Resultado:

```text
M  README.md
```

```bash
git diff --staged
git commit -m "Documentar incorporación de contactos"
python3 agenda.py
```

Resultado:

```text
Ana
Luis
Marta
Pablo
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
* e7603ed (HEAD -> main) Documentar incorporación de contactos
* 15c6cb3 Añadir a Pablo a los contactos
* 1b35c21 Documentar la agenda
* bd16875 Crear listado inicial de contactos
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

Se crean **cuatro commits**. `README.md` está sin seguimiento desde que se crea hasta que se ejecuta `git add README.md` antes del segundo commit. `??` significa archivo sin seguimiento; `A ` indica un archivo nuevo preparado; ` M` indica una modificación sin preparar y `M ` una modificación preparada. La primera columna corresponde al índice y la segunda al directorio de trabajo.

Separar código y documentación permite revisar, localizar y revertir cada cambio por su propósito. Al final se imprimen Ana, Luis, Marta y Pablo.

## Evidencias solicitadas

Incluye en `INFORME.md` el historial final, el estado final y las respuestas a las tres preguntas. Debe haber cuatro commits en `main`. No añadas `INFORME.md` a ningún commit.
