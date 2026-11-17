# Actividad 7 — Integración entre ramas y después en main

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Crear un único commit con catálogo, README y verificador original. Crear las tres ramas desde esa main inicial, sin actualizarlas entre sí.
2. Confirmar cada desarrollo suministrado y probar su función. Las dos llamadas de préstamo se hacen en el mismo proceso para observar `True` y luego `False`.
3. Volver a main y confirmar por separado la normalización con `strip()`. El gráfico previo muestra cuatro líneas independientes desde la base común; el mensaje `Normalizar espacios en la búsqueda de main` identifica este avance propio de main.
4. Crear `integracion` desde `feature/busquedas`, nunca desde la main ya actualizada.
5. Fusionar préstamos dentro de integración. Resolver el conflicto de `buscar` conservando `casefold()` y la función prestar. En esta solución de fase A se conserva la búsqueda sin distinguir mayúsculas, reservando la unión con la regla de espacios para la fase B.
6. Fusionar informes en integración. Conservar búsqueda flexible, préstamo, contador y salida de disponibles. Si Git combina automáticamente, comprobar igualmente el comportamiento. Usar `git branch --merged` y el gráfico para verificar qué ramas están integradas.
7. Probar las tres funciones en fase A antes de tocar main. El verificador completo todavía exige los espacios que aportará main.
8. Volver a main y fusionar integración. Combinar en buscar `titulo.strip()` y `titulo.casefold()`, comparando con `libro["titulo"].casefold()`. Conservar préstamos e informes.
9. Ejecutar el verificador original sin cambios, revisar el estado y el gráfico. Conservar todas las ramas para la revisión.

## Conflictos y decisiones

Préstamos contra integración: ambas ramas cambian la normalización en `biblioteca.py`; se conserva la búsqueda sin distinguir mayúsculas y se añade prestar, que delega en buscar.

Informes contra integración: en la ejecución registrada también aparece un conflicto en `biblioteca.py`, al añadir funciones en la misma zona del archivo. Se conservan juntas `prestar` y `contar_disponibles`, además de la búsqueda con `casefold()` y la presentación con el contador. Las tres fusiones de esta actividad han requerido resolución manual del contenido; los bloques reales aparecen a continuación.

Integración contra main: se reúnen las dos reglas de normalización, en lugar de elegir solo una. Las evidencias muestran los conflictos reales y el código completo de cada resolución.

## Respuestas

Git podría completar una fusión que conservara solo `strip()` y perder la normalización de mayúsculas: Python ejecutaría el archivo, pero `buscar("dune")` devolvería `None` y el validador fallaría al acceder a `['titulo']`. También podría quedar una llamada a una función no importada. Revisaría la salida, el traceback y las funciones combinadas, sin dar por demostrada la corrección por el mero éxito del merge.

Fusionar en una auxiliar reúne y prueba funcionalidades manteniendo main al margen de esa fase. Fusionar después la auxiliar en main incorpora todo su historial y debe compatibilizarlo con el trabajo independiente de main. Las ramas son referencias, no copias aisladas del programa.

El resultado conserva los tres libros, permite buscar `  DUNE  `, prestar solo una vez y reduce disponibles de 3 a 2. El verificador, la salida completa de estado, el gráfico anterior a las fusiones y el gráfico final figuran a continuación. No se elimina ninguna rama.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-07-biblioteca-integracion
cd git-07-biblioteca-integracion
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

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Biblioteca integradora
Versión inicial: catálogo y búsqueda exacta.
```

Editar `verificar_integracion.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
A  biblioteca.py
A  verificar_integracion.py
```

```bash
git diff --staged
```

```bash
git commit -m "Crear catálogo y verificador de integración"
```

```bash
git rev-parse HEAD
```

Salida de referencia (los hashes pueden variar):

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
git switch main
```

```bash
git switch -c feature/busquedas
```

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Implementar busquedas"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import buscar; assert buscar("dune") == buscar("Dune"); print(buscar("dune"))'
```

Salida de referencia (los hashes pueden variar):

```text
{'titulo': 'Dune', 'prestado': False}
```

```bash
git switch main
```

```bash
git switch -c feature/prestamos
```

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Implementar prestamos"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import prestar; print(prestar("Dune")); print(prestar("Dune"))'
```

Salida de referencia (los hashes pueden variar):

```text
True
False
```

```bash
git switch main
```

```bash
git switch -c feature/informes
```

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Implementar informes"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
106378e77cec54a9d57d8ce7f3535641398b29a6
```

```bash
python3 -c 'from biblioteca import contar_disponibles; print(contar_disponibles())'
```

Salida de referencia (los hashes pueden variar):

```text
3
```

```bash
git switch main
```

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Normalizar espacios en la búsqueda de main"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

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
```

```bash
git switch -c integracion
```

```bash
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

Salida de referencia (los hashes pueden variar):

```text
biblioteca.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Salida de referencia (los hashes pueden variar):

```text
diff --cc biblioteca.py
index 23e18bf,dbe1521..0000000
--- a/biblioteca.py
+++ b/biblioteca.py
@@@ -5,9 -5,9 +5,13 @@@ LIBROS = 
  ]
  
  def buscar(titulo):
++<<<<<<< HEAD
 +    titulo = titulo.casefold()
++=======
+     titulo = titulo.strip()
++>>>>>>> feature/prestamos
      for libro in LIBROS:
 -        if libro["titulo"] == titulo:
 +        if libro["titulo"].casefold() == titulo:
              return libro
      return None
```

Git ha detenido la fusión. Se combinan las funciones de ambos lados, se eliminan las marcas de conflicto y se conserva el resultado siguiente.

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Integrar feature/prestamos conservando las funcionalidades"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* de63e29 (feature/informes) Implementar informes
| *   5c2bfb0 (HEAD -> integracion) Integrar feature/prestamos conservando las funcionalidades
| |\  
| | * 7482dae (feature/prestamos) Implementar prestamos
| |/  
|/|   
| * bb8e8ab (feature/busquedas) Implementar busquedas
|/  
| * 910f151 (main) Normalizar espacios en la búsqueda de main
|/  
* 106378e Crear catálogo y verificador de integración
```

```bash
python3 biblioteca.py
```

Salida de referencia (los hashes pueden variar):

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

Salida de referencia (los hashes pueden variar):

```text
biblioteca.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Salida de referencia (los hashes pueden variar):

```text
diff --cc biblioteca.py
index 5556c86,0ee4480..0000000
--- a/biblioteca.py
+++ b/biblioteca.py
@@@ -11,12 -10,8 +11,17 @@@ def buscar(titulo)
              return libro
      return None
  
++<<<<<<< HEAD
 +def prestar(titulo):
 +    libro = buscar(titulo)
 +    if libro is None or libro["prestado"]:
 +        return False
 +    libro["prestado"] = True
 +    return True
++=======
+ def contar_disponibles():
+     return sum(not libro["prestado"] for libro in LIBROS)
++>>>>>>> feature/informes
  
  def mostrar():
      for libro in LIBROS:
```

Git ha detenido la fusión. Se combinan las funciones de ambos lados, se eliminan las marcas de conflicto y se conserva el resultado siguiente.

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Integrar feature/informes conservando las funcionalidades"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
*   e25f3c0 (HEAD -> integracion) Integrar feature/informes conservando las funcionalidades
|\  
| * de63e29 (feature/informes) Implementar informes
* |   5c2bfb0 Integrar feature/prestamos conservando las funcionalidades
|\ \  
| * | 7482dae (feature/prestamos) Implementar prestamos
| |/  
* / bb8e8ab (feature/busquedas) Implementar busquedas
|/  
| * 910f151 (main) Normalizar espacios en la búsqueda de main
|/  
* 106378e Crear catálogo y verificador de integración
```

```bash
python3 biblioteca.py
```

Salida de referencia (los hashes pueden variar):

```text
Dune
1984
El Quijote
Disponibles: 3
```

```bash
git branch --merged
```

Salida de referencia (los hashes pueden variar):

```text
  feature/busquedas
  feature/informes
  feature/prestamos
* integracion
```

```bash
python3 -c 'from biblioteca import buscar, prestar, contar_disponibles; assert buscar("dune"); assert contar_disponibles() == 3; assert prestar("DUNE"); assert not prestar("Dune"); assert contar_disponibles() == 2; print("FASE A CORRECTA")'
```

Salida de referencia (los hashes pueden variar):

```text
FASE A CORRECTA
```

```bash
git switch main
```

```bash
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

Salida de referencia (los hashes pueden variar):

```text
biblioteca.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
UU biblioteca.py
```

```bash
git diff --cc
```

Salida de referencia (los hashes pueden variar):

```text
diff --cc biblioteca.py
index a3b4d9d,454b9cb..0000000
--- a/biblioteca.py
+++ b/biblioteca.py
@@@ -5,9 -5,9 +5,13 @@@ LIBROS = 
  ]
  
  def buscar(titulo):
++<<<<<<< HEAD
 +    titulo = titulo.strip()
++=======
+     titulo = titulo.casefold()
++>>>>>>> integracion
      for libro in LIBROS:
-         if libro["titulo"] == titulo:
+         if libro["titulo"].casefold() == titulo:
              return libro
      return None
```

Git ha detenido la fusión. Se combinan las funciones de ambos lados, se eliminan las marcas de conflicto y se conserva el resultado siguiente.

Editar `biblioteca.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  biblioteca.py
```

```bash
git diff --staged
```

```bash
git commit -m "Integrar integracion conservando las funcionalidades"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

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
python3 biblioteca.py
```

Salida de referencia (los hashes pueden variar):

```text
Dune
1984
El Quijote
Disponibles: 3
```

```bash
python3 verificar_integracion.py
```

Salida de referencia (los hashes pueden variar):

```text
INTEGRACIÓN COMPLETA: TODAS LAS COMPROBACIONES SUPERADAS
```

```bash
git branch --merged
```

Salida de referencia (los hashes pueden variar):

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

Salida de referencia (los hashes pueden variar):

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
