# Actividad 1 — El primer historial de una agenda

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Crear `git-01-agenda`, copiar los dos archivos iniciales e inicializar `main`.
2. Registrar solo `agenda.py`; comprobar que `README.md` sigue como `??`.
3. Registrar el README en el segundo commit.
4. Añadir Pablo y la frase indicada, pero preparar y confirmar cada archivo por separado.
5. Ejecutar el programa y comprobar el historial y el estado final.

## Respuestas

Se crean **cuatro commits**. `README.md` está sin seguimiento desde que se crea hasta que se ejecuta `git add README.md` antes del segundo commit. `??` significa archivo sin seguimiento; `A ` indica un archivo nuevo preparado; ` M` indica una modificación sin preparar y `M ` una modificación preparada. La primera columna corresponde al índice y la segunda al directorio de trabajo.

Separar código y documentación permite revisar, localizar y revertir cada cambio por su propósito. Al final se imprimen Ana, Luis, Marta y Pablo. El historial y el estado reales figuran al final del documento.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-01-agenda
cd git-01-agenda
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

Editar `agenda.py` en PyCharm y guardar este contenido completo:

```python
CONTACTOS = ["Ana", "Luis", "Marta"]

def mostrar():
    for contacto in CONTACTOS:
        print(contacto)

if __name__ == "__main__":
    mostrar()
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Agenda
Aplicación Python para mostrar una lista de contactos.
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
?? README.md
?? agenda.py
```

```bash
git add agenda.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  agenda.py
?? README.md
```

```bash
git diff --staged
```

```bash
git commit -m "Crear listado inicial de contactos"
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
?? README.md
```

```bash
git add README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
```

```bash
git diff --staged
```

```bash
git commit -m "Documentar la agenda"
```

Editar `agenda.py` en PyCharm y guardar este contenido completo:

```python
CONTACTOS = ["Ana", "Luis", "Marta", "Pablo"]

def mostrar():
    for contacto in CONTACTOS:
        print(contacto)

if __name__ == "__main__":
    mostrar()
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Agenda
Aplicación Python para mostrar una lista de contactos.
Permite incorporar contactos al listado.
```

```bash
git add agenda.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
M  agenda.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir a Pablo a los contactos"
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
git commit -m "Documentar incorporación de contactos"
```

```bash
python3 agenda.py
```

Salida de referencia (los hashes pueden variar):

```text
Ana
Luis
Marta
Pablo
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* e7603ed (HEAD -> main) Documentar incorporación de contactos
* 15c6cb3 Añadir a Pablo a los contactos
* 1b35c21 Documentar la agenda
* bd16875 Crear listado inicial de contactos
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
