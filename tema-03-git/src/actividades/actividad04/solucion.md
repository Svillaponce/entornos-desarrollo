# Actividad 4 — Deshacer un error sin ocultarlo

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Registrar el cálculo correcto, después el suplemento incorrecto y finalmente las condiciones en tres commits separados.
2. Ejecutar para observar `145`, cuando el resultado correcto es `120`.
3. Inspeccionar `git log --oneline -p -- reservas.py`. Identificar el hash del commit que añadió `+ 25`. En esta reproducción se captura con `git rev-parse HEAD` justo después de crearlo, antes de registrar las condiciones.
4. Ejecutar `git revert --no-edit HASH_DEL_ERROR`, usando el hash real encontrado, **no HEAD**, porque el último commit contiene las condiciones.
5. Ejecutar de nuevo y comprobar `120`, las condiciones conservadas y los cuatro commits del historial.

## Respuestas

`revert` añade un commit con el cambio inverso y conserva tanto el error como la documentación posterior. Un `reset --hard` hasta la primera versión movería `main` hacia atrás y reemplazaría índice y archivos: las condiciones dejarían de estar en esa rama y podrían perderse además modificaciones locales. Por eso revert es la operación adecuada para conservar la trazabilidad.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-04-reservas
cd git-04-reservas
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

Editar `reservas.py` en PyCharm y guardar este contenido completo:

```python
def calcular_total(noches, precio_noche):
    return noches * precio_noche

if __name__ == "__main__":
    print(calcular_total(3, 40))
```

```bash
git add reservas.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  reservas.py
```

```bash
git diff --staged
```

```bash
git commit -m "Calcular reservas por noches"
```

Editar `reservas.py` en PyCharm y guardar este contenido completo:

```python
def calcular_total(noches, precio_noche):
    return noches * precio_noche + 25

if __name__ == "__main__":
    print(calcular_total(3, 40))
```

```bash
git add reservas.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  reservas.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir suplemento de 25 euros"
```

```bash
COMMIT_ERROR=$(git rev-parse HEAD)
```

Se guarda el hash del commit erróneo antes de crear el commit de condiciones.

Editar `CONDICIONES.md` en PyCharm y guardar este contenido completo:

```text
# Condiciones
El precio se calcula por noche de alojamiento.
```

```bash
git add CONDICIONES.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  CONDICIONES.md
```

```bash
git diff --staged
```

```bash
git commit -m "Documentar condiciones de alojamiento"
```

```bash
python3 reservas.py
```

Salida de referencia (los hashes pueden variar):

```text
145
```

```bash
git log --oneline -p -- reservas.py
```

Salida de referencia (los hashes pueden variar):

```text
6ff3436 Añadir suplemento de 25 euros
diff --git a/reservas.py b/reservas.py
index 41e2b42..61a8f26 100644
--- a/reservas.py
+++ b/reservas.py
@@ -1,5 +1,5 @@
 def calcular_total(noches, precio_noche):
-    return noches * precio_noche
+    return noches * precio_noche + 25
 
 if __name__ == "__main__":
     print(calcular_total(3, 40))
1c6b754 Calcular reservas por noches
diff --git a/reservas.py b/reservas.py
new file mode 100644
index 0000000..41e2b42
--- /dev/null
+++ b/reservas.py
@@ -0,0 +1,5 @@
+def calcular_total(noches, precio_noche):
+    return noches * precio_noche
+
+if __name__ == "__main__":
+    print(calcular_total(3, 40))
```

```bash
git revert --no-edit "$COMMIT_ERROR"
```

```bash
python3 reservas.py
```

Salida de referencia (los hashes pueden variar):

```text
120
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* c43756a (HEAD -> main) Revert "Añadir suplemento de 25 euros"
* 206857e Documentar condiciones de alojamiento
* 6ff3436 Añadir suplemento de 25 euros
* 1c6b754 Calcular reservas por noches
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
