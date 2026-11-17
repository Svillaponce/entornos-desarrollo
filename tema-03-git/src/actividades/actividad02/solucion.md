# Actividad 2 — Auditoría de archivos y preparación selectiva

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Registrar el conversor y el README iniciales en un commit.
2. Añadir la conversión inversa, la documentación y las reglas de exclusión. Crear también los dos archivos locales ficticios.
3. Comparar `git status --short --untracked-files=all`, `git ls-files` y `git diff`: los dos archivos iniciales están versionados, `.gitignore` es nuevo y los archivos personales ya quedan ignorados.
4. Usar `git check-ignore -v .env NOTAS_TEMPORALES.txt` para conocer la regla exacta y su línea.
5. Preparar únicamente `conversor.py`, revisar `git diff --staged` y confirmar. Después confirmar solo README y `.gitignore`.
6. Ejecutar y verificar que solo hay tres commits y ningún archivo personal versionado.

## Respuestas

El diff añade `fahrenheit_a_celsius` y sustituye la salida del programa por dos conversiones con etiquetas. No hace falta `git add -p`: toda la modificación de `conversor.py` es funcional y se selecciona por archivo. Si hubiera cambios ajenos en ese archivo, `git add -p conversor.py` permitiría seleccionar fragmentos.

`.gitignore` debe versionarse para compartir las reglas con todo el equipo. Añadir `.env` a las reglas **no deja de seguir un archivo ya confirmado**. En ese caso se utilizaría `git rm --cached .env` y un nuevo commit: el archivo quedaría en disco, pero su contenido anterior seguiría en el historial. Aquí solo contiene `MODO=desarrollo`, sin credenciales.

La salida es `20 ºC = 68.0 ºF` y `68 ºF = 20.0 ºC`. Las comprobaciones de ignorados y los extractos completos de ambos tipos de diff se incluyen a continuación.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-02-conversor
cd git-02-conversor
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

Editar `conversor.py` en PyCharm y guardar este contenido completo:

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(20))
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Conversor
Conversión de grados Celsius a Fahrenheit.
```

```bash
git add conversor.py README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
A  conversor.py
```

```bash
git diff --staged
```

Salida de referencia (los hashes pueden variar):

```text
diff --git a/README.md b/README.md
new file mode 100644
index 0000000..8031410
--- /dev/null
+++ b/README.md
@@ -0,0 +1,2 @@
+# Conversor
+Conversión de grados Celsius a Fahrenheit.
diff --git a/conversor.py b/conversor.py
new file mode 100644
index 0000000..1a516af
--- /dev/null
+++ b/conversor.py
@@ -0,0 +1,5 @@
+def celsius_a_fahrenheit(celsius):
+    return celsius * 9 / 5 + 32
+
+if __name__ == "__main__":
+    print(celsius_a_fahrenheit(20))
```

```bash
git commit -m "Crear conversor Celsius a Fahrenheit"
```

Editar `.gitignore` en PyCharm y guardar este contenido completo:

```text
__pycache__/
*.py[cod]
.venv/
.idea/
.env
NOTAS_TEMPORALES.txt
```

Editar `conversor.py` en PyCharm y guardar este contenido completo:

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    print("20 ºC =", celsius_a_fahrenheit(20), "ºF")
    print("68 ºF =", fahrenheit_a_celsius(68), "ºC")
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Conversor
Conversión de grados Celsius a Fahrenheit.
También convierte grados Fahrenheit a Celsius.
```

Editar `.env` en PyCharm y guardar este contenido completo:

```text
MODO=desarrollo
```

Editar `NOTAS_TEMPORALES.txt` en PyCharm y guardar este contenido completo:

```text
Borrador personal: pendiente de revisar.
```

```bash
git status --short --untracked-files=all
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
 M conversor.py
?? .gitignore
```

```bash
git ls-files
```

Salida de referencia (los hashes pueden variar):

```text
README.md
conversor.py
```

```bash
git diff
```

Salida de referencia (los hashes pueden variar):

```text
diff --git a/README.md b/README.md
index 8031410..42eeea9 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # Conversor
 Conversión de grados Celsius a Fahrenheit.
+También convierte grados Fahrenheit a Celsius.
diff --git a/conversor.py b/conversor.py
index 1a516af..4b466ae 100644
--- a/conversor.py
+++ b/conversor.py
@@ -1,5 +1,9 @@
 def celsius_a_fahrenheit(celsius):
     return celsius * 9 / 5 + 32
 
+def fahrenheit_a_celsius(fahrenheit):
+    return (fahrenheit - 32) * 5 / 9
+
 if __name__ == "__main__":
-    print(celsius_a_fahrenheit(20))
+    print("20 ºC =", celsius_a_fahrenheit(20), "ºF")
+    print("68 ºF =", fahrenheit_a_celsius(68), "ºC")
```

```bash
git check-ignore -v .env NOTAS_TEMPORALES.txt
```

Salida de referencia (los hashes pueden variar):

```text
.gitignore:5:.env	.env
.gitignore:6:NOTAS_TEMPORALES.txt	NOTAS_TEMPORALES.txt
```

```bash
git add conversor.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
 M README.md
M  conversor.py
?? .gitignore
```

```bash
git diff --staged
```

Salida de referencia (los hashes pueden variar):

```text
diff --git a/conversor.py b/conversor.py
index 1a516af..4b466ae 100644
--- a/conversor.py
+++ b/conversor.py
@@ -1,5 +1,9 @@
 def celsius_a_fahrenheit(celsius):
     return celsius * 9 / 5 + 32
 
+def fahrenheit_a_celsius(fahrenheit):
+    return (fahrenheit - 32) * 5 / 9
+
 if __name__ == "__main__":
-    print(celsius_a_fahrenheit(20))
+    print("20 ºC =", celsius_a_fahrenheit(20), "ºF")
+    print("68 ºF =", fahrenheit_a_celsius(68), "ºC")
```

```bash
git commit -m "Añadir conversión Fahrenheit a Celsius"
```

```bash
git add README.md .gitignore
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  .gitignore
M  README.md
```

```bash
git diff --staged
```

Salida de referencia (los hashes pueden variar):

```text
diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..e78200d
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,6 @@
+__pycache__/
+*.py[cod]
+.venv/
+.idea/
+.env
+NOTAS_TEMPORALES.txt
diff --git a/README.md b/README.md
index 8031410..42eeea9 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # Conversor
 Conversión de grados Celsius a Fahrenheit.
+También convierte grados Fahrenheit a Celsius.
```

```bash
git commit -m "Documentar conversión e ignorar archivos locales"
```

```bash
git ls-files
```

Salida de referencia (los hashes pueden variar):

```text
.gitignore
README.md
conversor.py
```

```bash
python3 conversor.py
```

Salida de referencia (los hashes pueden variar):

```text
20 ºC = 68.0 ºF
68 ºF = 20.0 ºC
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* d76847e (HEAD -> main) Documentar conversión e ignorar archivos locales
* 7cb5e58 Añadir conversión Fahrenheit a Celsius
* 7126212 Crear conversor Celsius a Fahrenheit
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
