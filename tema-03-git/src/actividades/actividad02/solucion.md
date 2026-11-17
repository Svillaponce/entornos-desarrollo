# Actividad 2 — Auditoría de archivos y preparación selectiva

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-02-conversor
cd git-02-conversor
git init -b main
```

En `conversor.py`, guarda este contenido:

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(20))
```

En `README.md`, guarda este contenido:

```text
# Conversor
Conversión de grados Celsius a Fahrenheit.
```

```bash
git add conversor.py README.md
git status --short
```

Resultado:

```text
A  README.md
A  conversor.py
```

```bash
git diff --staged
```

Resultado:

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

En `.gitignore`, guarda este contenido:

```text
__pycache__/
*.py[cod]
.venv/
.idea/
.env
NOTAS_TEMPORALES.txt
```

En `conversor.py`, guarda este contenido:

```python
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    print("20 ºC =", celsius_a_fahrenheit(20), "ºF")
    print("68 ºF =", fahrenheit_a_celsius(68), "ºC")
```

En `README.md`, guarda este contenido:

```text
# Conversor
Conversión de grados Celsius a Fahrenheit.
También convierte grados Fahrenheit a Celsius.
```

En `.env`, guarda este contenido:

```text
MODO=desarrollo
```

En `NOTAS_TEMPORALES.txt`, guarda este contenido:

```text
Borrador personal: pendiente de revisar.
```

```bash
git status --short --untracked-files=all
```

Resultado:

```text
 M README.md
 M conversor.py
?? .gitignore
```

```bash
git ls-files
```

Resultado:

```text
README.md
conversor.py
```

```bash
git diff
```

Resultado:

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

Resultado:

```text
.gitignore:5:.env	.env
.gitignore:6:NOTAS_TEMPORALES.txt	NOTAS_TEMPORALES.txt
```

```bash
git add conversor.py
git status --short
```

Resultado:

```text
 M README.md
M  conversor.py
?? .gitignore
```

```bash
git diff --staged
```

Resultado:

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
git add README.md .gitignore
git status --short
```

Resultado:

```text
A  .gitignore
M  README.md
```

```bash
git diff --staged
```

Resultado:

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
git ls-files
```

Resultado:

```text
.gitignore
README.md
conversor.py
```

```bash
python3 conversor.py
```

Resultado:

```text
20 ºC = 68.0 ºF
68 ºF = 20.0 ºC
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
* d76847e (HEAD -> main) Documentar conversión e ignorar archivos locales
* 7cb5e58 Añadir conversión Fahrenheit a Celsius
* 7126212 Crear conversor Celsius a Fahrenheit
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

El diff añade `fahrenheit_a_celsius` y sustituye la salida del programa por dos conversiones con etiquetas. No hace falta `git add -p`: toda la modificación de `conversor.py` es funcional y se selecciona por archivo. Si hubiera cambios ajenos en ese archivo, `git add -p conversor.py` permitiría seleccionar fragmentos.

`.gitignore` debe versionarse para compartir las reglas con todo el equipo. Añadir `.env` a las reglas **no deja de seguir un archivo ya confirmado**. En ese caso se utilizaría `git rm --cached .env` y un nuevo commit: el archivo quedaría en disco, pero su contenido anterior seguiría en el historial. Aquí solo contiene `MODO=desarrollo`, sin credenciales.

## Evidencias solicitadas

Incluye en `INFORME.md` las reglas que ignoran `.env` y `NOTAS_TEMPORALES.txt`, dos extractos de `git diff` o `git diff --staged` y las respuestas. Debe haber tres commits y ningún archivo personal versionado. No añadas `INFORME.md` a ningún commit.
