# Actividad 4 — Deshacer un error sin ocultarlo

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-04-reservas
cd git-04-reservas
git init -b main
```

En `reservas.py`, guarda este contenido:

```python
def calcular_total(noches, precio_noche):
    return noches * precio_noche

if __name__ == "__main__":
    print(calcular_total(3, 40))
```

```bash
git add reservas.py
git status --short
git diff --staged
git commit -m "Calcular reservas por noches"
```

En `reservas.py`, guarda este contenido:

```python
def calcular_total(noches, precio_noche):
    return noches * precio_noche + 25

if __name__ == "__main__":
    print(calcular_total(3, 40))
```

```bash
git add reservas.py
git status --short
git diff --staged
git commit -m "Añadir suplemento de 25 euros"
COMMIT_ERROR=$(git rev-parse HEAD)
```

Se guarda el hash del commit erróneo antes de crear el commit de condiciones.

En `CONDICIONES.md`, guarda este contenido:

```text
# Condiciones
El precio se calcula por noche de alojamiento.
```

```bash
git add CONDICIONES.md
git status --short
git diff --staged
git commit -m "Documentar condiciones de alojamiento"
python3 reservas.py
```

Resultado:

```text
145
```

```bash
git log --oneline -p -- reservas.py
```

Resultado:

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
python3 reservas.py
```

Resultado:

```text
120
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
* c43756a (HEAD -> main) Revert "Añadir suplemento de 25 euros"
* 206857e Documentar condiciones de alojamiento
* 6ff3436 Añadir suplemento de 25 euros
* 1c6b754 Calcular reservas por noches
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

`revert` añade un commit con el cambio inverso y conserva tanto el error como la documentación posterior. Un `reset --hard` hasta la primera versión movería `main` hacia atrás y reemplazaría índice y archivos: las condiciones dejarían de estar en esa rama y podrían perderse además modificaciones locales. Por eso revert es la operación adecuada para conservar la trazabilidad.

## Evidencias solicitadas

Incluye en `INFORME.md` el historial final, las salidas 145 y 120 y la explicación de por qué se utiliza `revert`. Conserva `CONDICIONES.md`. No añadas `INFORME.md` a ningún commit.
