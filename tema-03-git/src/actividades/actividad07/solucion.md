# Actividad 7 — Integración entre ramas y después en main

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-07-biblioteca-integracion
cd git-07-biblioteca-integracion
git init -b main
```

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    for libro in LIBROS:
        if libro["titulo"] == titulo:
            return libro
    return None

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])

if __name__ == "__main__":
    mostrar()
```

En `README.md`, guarda este contenido:

```text
# Biblioteca integradora
Versión inicial: catálogo y búsqueda exacta.
```

En `verificar_integracion.py`, guarda este contenido:

```python
from biblioteca import LIBROS, buscar, prestar, contar_disponibles
assert len(LIBROS) == 3
assert buscar("dune")["titulo"] == "Dune", "Falta búsqueda sin distinguir mayúsculas"
assert buscar("  DUNE  ")["titulo"] == "Dune", "Falta eliminar espacios"
assert buscar("No existe") is None
assert contar_disponibles() == 3
assert prestar(" dune ") is True, "El préstamo debe utilizar la búsqueda integrada"
assert buscar("Dune")["prestado"] is True
assert contar_disponibles() == 2
assert prestar("DUNE") is False, "No se puede prestar dos veces el mismo ejemplar"
assert prestar("No existe") is False
assert contar_disponibles() == 2
print("INTEGRACIÓN COMPLETA: TODAS LAS COMPROBACIONES SUPERADAS")
```

```bash
git add biblioteca.py README.md verificar_integracion.py
git status --short
git diff --staged
git commit -m "Crear catálogo y verificador de integración"
git rev-parse HEAD
```

Resultado:

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
git switch main
git switch -c feature/busquedas
```

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.casefold()
    for libro in LIBROS:
        if libro["titulo"].casefold() == titulo:
            return libro
    return None

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Implementar busquedas"
git merge-base main HEAD
```

Resultado:

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import buscar; assert buscar("dune") == buscar("Dune"); print(buscar("dune"))'
```

Resultado:

```text
{'titulo': 'Dune', 'prestado': False}
```

```bash
git switch main
git switch -c feature/prestamos
```

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.strip()
    for libro in LIBROS:
        if libro["titulo"] == titulo:
            return libro
    return None

def prestar(titulo):
    libro = buscar(titulo)
    if libro is None or libro["prestado"]:
        return False
    libro["prestado"] = True
    return True

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Implementar prestamos"
git merge-base main HEAD
```

Resultado:

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import prestar; print(prestar("Dune")); print(prestar("Dune"))'
```

Resultado:

```text
True
False
```

```bash
git switch main
git switch -c feature/informes
```

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    for libro in LIBROS:
        if libro["titulo"] == titulo:
            return libro
    return None

def contar_disponibles():
    return sum(not libro["prestado"] for libro in LIBROS)

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])
    print("Disponibles:", contar_disponibles())

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Implementar informes"
git merge-base main HEAD
```

Resultado:

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import contar_disponibles; print(contar_disponibles())'
```

Resultado:

```text
3
```

```bash
git switch main
```

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.strip()
    for libro in LIBROS:
        if libro["titulo"] == titulo:
            return libro
    return None

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Normalizar espacios en la búsqueda de main"
git log --oneline --graph --all --decorate
```

Resultado:

```text
* de63e29 (feature/informes) Implementar informes
| * 910f151 (HEAD -> main) Normalizar espacios en la búsqueda de main
|/  
| * bb8e8ab (feature/busquedas) Implementar busquedas
|/  
| * 7482dae (feature/prestamos) Implementar prestamos
|/  
* 106378e Crear catálogo y verificador de integración
```

```bash
git switch feature/busquedas
git switch -c integracion
git merge --no-ff feature/prestamos -m "Integrar feature/prestamos"
```

Git detiene la fusión con este diagnóstico:

```text
Auto-merging biblioteca.py
CONFLICT (content): Merge conflict in biblioteca.py
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git diff --name-only --diff-filter=U
```

Resultado:

```text
biblioteca.py
```

```bash
git status --short
```

Resultado:

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Resuelve el conflicto conservando las funciones de ambas ramas. Sustituye las marcas por el código combinado siguiente:

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.casefold()
    for libro in LIBROS:
        if libro["titulo"].casefold() == titulo:
            return libro
    return None

def prestar(titulo):
    libro = buscar(titulo)
    if libro is None or libro["prestado"]:
        return False
    libro["prestado"] = True
    return True

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Integrar feature/prestamos conservando las funcionalidades"
python3 biblioteca.py
```

Resultado:

```text
Dune
1984
El Quijote
```

```bash
git merge --no-ff feature/informes -m "Integrar feature/informes"
```

Git detiene la fusión con este diagnóstico:

```text
Auto-merging biblioteca.py
CONFLICT (content): Merge conflict in biblioteca.py
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git diff --name-only --diff-filter=U
```

Resultado:

```text
biblioteca.py
```

```bash
git status --short
```

Resultado:

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Resuelve el conflicto conservando las funciones de ambas ramas. Sustituye las marcas por el código combinado siguiente:

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.casefold()
    for libro in LIBROS:
        if libro["titulo"].casefold() == titulo:
            return libro
    return None

def prestar(titulo):
    libro = buscar(titulo)
    if libro is None or libro["prestado"]:
        return False
    libro["prestado"] = True
    return True

def contar_disponibles():
    return sum(not libro["prestado"] for libro in LIBROS)

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])
    print("Disponibles:", contar_disponibles())

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Integrar feature/informes conservando las funcionalidades"
python3 biblioteca.py
```

Resultado:

```text
Dune
1984
El Quijote
Disponibles: 3
```

```bash
git branch --merged
```

Resultado:

```text
  feature/busquedas
  feature/informes
  feature/prestamos
* integracion
```

```bash
python3 -c 'from biblioteca import buscar, prestar, contar_disponibles; assert buscar("dune"); assert contar_disponibles() == 3; assert prestar("DUNE"); assert not prestar("Dune"); assert contar_disponibles() == 2; print("FASE A CORRECTA")'
```

Resultado:

```text
FASE A CORRECTA
```

```bash
git switch main
git merge --no-ff integracion -m "Integrar integracion"
```

Git detiene la fusión con este diagnóstico:

```text
Auto-merging biblioteca.py
CONFLICT (content): Merge conflict in biblioteca.py
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git diff --name-only --diff-filter=U
```

Resultado:

```text
biblioteca.py
```

```bash
git status --short
```

Resultado:

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Resuelve el conflicto conservando las funciones de ambas ramas. Sustituye las marcas por el código combinado siguiente:

En `biblioteca.py`, guarda este contenido:

```python
LIBROS = [
    {"titulo": "Dune", "prestado": False},
    {"titulo": "1984", "prestado": False},
    {"titulo": "El Quijote", "prestado": False},
]

def buscar(titulo):
    titulo = titulo.strip()
    titulo = titulo.casefold()
    for libro in LIBROS:
        if libro["titulo"].casefold() == titulo:
            return libro
    return None

def prestar(titulo):
    libro = buscar(titulo)
    if libro is None or libro["prestado"]:
        return False
    libro["prestado"] = True
    return True

def contar_disponibles():
    return sum(not libro["prestado"] for libro in LIBROS)

def mostrar():
    for libro in LIBROS:
        print(libro["titulo"])
    print("Disponibles:", contar_disponibles())

if __name__ == "__main__":
    mostrar()
```

```bash
git add biblioteca.py
git status --short
git diff --staged
git commit -m "Integrar integracion conservando las funcionalidades"
python3 biblioteca.py
```

Resultado:

```text
Dune
1984
El Quijote
Disponibles: 3
```

```bash
python3 verificar_integracion.py
```

Resultado:

```text
INTEGRACIÓN COMPLETA: TODAS LAS COMPROBACIONES SUPERADAS
```

```bash
git branch --merged
```

Resultado:

```text
  feature/busquedas
  feature/informes
  feature/prestamos
  integracion
* main
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
*   5c0adb9 (HEAD -> main) Integrar integracion conservando las funcionalidades
|\  
| *   e25f3c0 (integracion) Integrar feature/informes conservando las funcionalidades
| |\  
| | * de63e29 (feature/informes) Implementar informes
| * |   5c2bfb0 Integrar feature/prestamos conservando las funcionalidades
| |\ \  
| | * | 7482dae (feature/prestamos) Implementar prestamos
| | |/  
| * / bb8e8ab (feature/busquedas) Implementar busquedas
| |/  
* / 910f151 Normalizar espacios en la búsqueda de main
|/  
* 106378e Crear catálogo y verificador de integración
```

```bash
git status
```

Resultado:

```text
On branch main
nothing to commit, working tree clean
```

## Conflictos y decisiones

Préstamos contra integración: ambas ramas cambian la normalización en `biblioteca.py`; se conserva la búsqueda sin distinguir mayúsculas y se añade prestar, que delega en buscar.

Informes contra integración: en la ejecución registrada también aparece un conflicto en `biblioteca.py`, al añadir funciones en la misma zona del archivo. Se conservan juntas `prestar` y `contar_disponibles`, además de la búsqueda con `casefold()` y la presentación con el contador. Las tres fusiones de esta actividad han requerido resolución manual del contenido; las resoluciones se muestran en los pasos anteriores.

Integración contra main: se reúnen las dos reglas de normalización, en lugar de elegir solo una. Las evidencias muestran los conflictos reales y el código completo de cada resolución.

## Respuestas

Git podría completar una fusión que conservara solo `strip()` y perder la normalización de mayúsculas: Python ejecutaría el archivo, pero `buscar("dune")` devolvería `None` y el validador fallaría al acceder a `['titulo']`. También podría quedar una llamada a una función no importada. Revisaría la salida, el traceback y las funciones combinadas, sin dar por demostrada la corrección por el mero éxito del merge.

Fusionar en una auxiliar reúne y prueba funcionalidades manteniendo main al margen de esa fase. Fusionar después la auxiliar en main incorpora todo su historial y debe compatibilizarlo con el trabajo independiente de main. Las ramas son referencias, no copias aisladas del programa.

El resultado conserva los tres libros, permite buscar `  DUNE  `, prestar solo una vez y reduce disponibles de 3 a 2. No se elimina ninguna rama.

## Evidencias solicitadas

Incluye en `INFORME.md` el gráfico anterior a las fusiones y la base de las ramas, los conflictos y sus resoluciones, un ejemplo de fallo funcional sin conflicto textual, la salida completa del validador y de `git status`, el gráfico final y la explicación de las dos fases. Identifica el commit independiente de `main` y conserva todas las ramas. No añadas `INFORME.md` a ningún commit.
