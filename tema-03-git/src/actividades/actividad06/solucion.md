# Actividad 6 — Tres ramas que compiten por main

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-06-pedidos
cd git-06-pedidos
git init -b main
```

En `pedido.py`, guarda este contenido:

```python
TITULO = "Pedido"

def calcular_total(precio, cantidad):
    return precio * cantidad

def mostrar(precio, cantidad):
    print(f"=== {TITULO} ===")
    print("Total:", calcular_total(precio, cantidad))

if __name__ == "__main__":
    mostrar(20, 3)
```

En `README.md`, guarda este contenido:

```text
# Pedidos
Calcula el importe de un pedido.
```

En `verificar.py`, guarda este contenido:

```python
from pedido import calcular_total, calcular_con_descuento, calcular_con_impuesto
assert calcular_total(20, 3) == 60
assert calcular_con_descuento(20, 3, 10) == 54
assert calcular_con_impuesto(20, 3, 21) == 72.6
print("COMPROBACIONES SUPERADAS")
```

```bash
git add pedido.py README.md verificar.py
git status --short
git diff --staged
git commit -m "Crear cálculo inicial y verificador de pedidos"
git rev-parse HEAD
```

Resultado:

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
git switch -c feature/presentacion
```

En `pedido.py`, guarda este contenido:

```python
TITULO = "Gestor de pedidos"

def calcular_total(precio, cantidad):
    return precio * cantidad

def mostrar(precio, cantidad):
    print(f"*** {TITULO} ***")
    print(f"Unidades: {cantidad}")
    print("Total:", calcular_total(precio, cantidad))

if __name__ == "__main__":
    mostrar(20, 3)
```

```bash
git add pedido.py
git status --short
git diff --staged
git commit -m "Añadir presentacion a los pedidos"
git merge-base main HEAD
```

Resultado:

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
git switch -c feature/descuentos
```

En `pedido.py`, guarda este contenido:

```python
TITULO = "Pedidos con descuentos"

def calcular_total(precio, cantidad):
    return precio * cantidad

def calcular_con_descuento(precio, cantidad, porcentaje):
    return calcular_total(precio, cantidad) * (1 - porcentaje / 100)

def mostrar(precio, cantidad):
    print(f"=== {TITULO} ===")
    print("Total con 10 % de descuento:", calcular_con_descuento(precio, cantidad, 10))

if __name__ == "__main__":
    mostrar(20, 3)
```

```bash
git add pedido.py
git status --short
git diff --staged
git commit -m "Añadir descuentos a los pedidos"
git merge-base main HEAD
```

Resultado:

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
git switch -c feature/impuestos
```

En `pedido.py`, guarda este contenido:

```python
TITULO = "Pedidos con impuestos"

def calcular_total(precio, cantidad):
    return precio * cantidad

def calcular_con_impuesto(precio, cantidad, porcentaje):
    return round(calcular_total(precio, cantidad) * (1 + porcentaje / 100), 2)

def mostrar(precio, cantidad):
    print(f"=== {TITULO} ===")
    print("Total con 21 % de impuesto:", calcular_con_impuesto(precio, cantidad, 21))

if __name__ == "__main__":
    mostrar(20, 3)
```

```bash
git add pedido.py
git status --short
git diff --staged
git commit -m "Añadir impuestos a los pedidos"
git merge-base main HEAD
```

Resultado:

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
* 8a669d3 (feature/descuentos) Añadir descuentos a los pedidos
| * a3a01cf (HEAD -> feature/impuestos) Añadir impuestos a los pedidos
|/  
| * 52f605a (feature/presentacion) Añadir presentacion a los pedidos
|/  
* 458c087 (main) Crear cálculo inicial y verificador de pedidos
```

```bash
git switch main
git merge --no-ff feature/presentacion -m "Integrar feature/presentacion"
python3 pedido.py
```

Resultado:

```text
*** Gestor de pedidos ***
Unidades: 3
Total: 60
```

```bash
git merge --no-ff feature/descuentos -m "Integrar feature/descuentos"
```

Git detiene la fusión con este diagnóstico:

```text
Auto-merging pedido.py
CONFLICT (content): Merge conflict in pedido.py
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git diff --name-only --diff-filter=U
```

Resultado:

```text
pedido.py
```

```bash
git status --short
```

Resultado:

```text
UU pedido.py
```

```bash
git diff --cc
```

Resuelve el conflicto conservando las funciones de ambas ramas. Sustituye las marcas por el código combinado siguiente:

En `pedido.py`, guarda este contenido:

```python
TITULO = "Gestor de pedidos"

def calcular_total(precio, cantidad):
    return precio * cantidad

def calcular_con_descuento(precio, cantidad, porcentaje):
    return calcular_total(precio, cantidad) * (1 - porcentaje / 100)

def mostrar(precio, cantidad):
    print(f"*** {TITULO} ***")
    print(f"Unidades: {cantidad}")
    print("Total:", calcular_total(precio, cantidad))
    print("Total con 10 % de descuento:", calcular_con_descuento(precio, cantidad, 10))

if __name__ == "__main__":
    mostrar(20, 3)
```

```bash
git add pedido.py
git status --short
git diff --staged
git commit -m "Integrar feature/descuentos conservando las funcionalidades"
python3 pedido.py
```

Resultado:

```text
*** Gestor de pedidos ***
Unidades: 3
Total: 60
Total con 10 % de descuento: 54.0
```

```bash
git merge --no-ff feature/impuestos -m "Integrar feature/impuestos"
```

Git detiene la fusión con este diagnóstico:

```text
Auto-merging pedido.py
CONFLICT (content): Merge conflict in pedido.py
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git diff --name-only --diff-filter=U
```

Resultado:

```text
pedido.py
```

```bash
git status --short
```

Resultado:

```text
UU pedido.py
```

```bash
git diff --cc
```

Resuelve el conflicto conservando las funciones de ambas ramas. Sustituye las marcas por el código combinado siguiente:

En `pedido.py`, guarda este contenido:

```python
TITULO = "Gestor de pedidos"

def calcular_total(precio, cantidad):
    return precio * cantidad

def calcular_con_descuento(precio, cantidad, porcentaje):
    return calcular_total(precio, cantidad) * (1 - porcentaje / 100)

def calcular_con_impuesto(precio, cantidad, porcentaje):
    return round(calcular_total(precio, cantidad) * (1 + porcentaje / 100), 2)

def mostrar(precio, cantidad):
    print(f"*** {TITULO} ***")
    print(f"Unidades: {cantidad}")
    print("Total:", calcular_total(precio, cantidad))
    print("Total con 10 % de descuento:", calcular_con_descuento(precio, cantidad, 10))
    print("Total con 21 % de impuesto:", calcular_con_impuesto(precio, cantidad, 21))

if __name__ == "__main__":
    mostrar(20, 3)
```

```bash
git add pedido.py
git status --short
git diff --staged
git commit -m "Integrar feature/impuestos conservando las funcionalidades"
python3 pedido.py
```

Resultado:

```text
*** Gestor de pedidos ***
Unidades: 3
Total: 60
Total con 10 % de descuento: 54.0
Total con 21 % de impuesto: 72.6
```

```bash
python3 verificar.py
```

Resultado:

```text
COMPROBACIONES SUPERADAS
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

```text
*   d5110da (HEAD -> main) Integrar feature/impuestos conservando las funcionalidades
|\  
| * a3a01cf (feature/impuestos) Añadir impuestos a los pedidos
* |   511d199 Integrar feature/descuentos conservando las funcionalidades
|\ \  
| * | 8a669d3 (feature/descuentos) Añadir descuentos a los pedidos
| |/  
* |   4339e6e Integrar feature/presentacion
|\ \  
| |/  
|/|   
| * 52f605a (feature/presentacion) Añadir presentacion a los pedidos
|/  
* 458c087 Crear cálculo inicial y verificador de pedidos
```

```bash
git status
```

Resultado:

```text
On branch main
nothing to commit, working tree clean
```

## Conflictos y criterio de resolución

La primera fusión no tiene conflictos. Descuentos e impuestos modifican el mismo título y la presentación de `pedido.py`; los pasos anteriores muestran el diagnóstico de Git y el código combinado de cada resolución. Se conserva `Gestor de pedidos`, la presentación con unidades y las funciones `calcular_total`, `calcular_con_descuento` y `calcular_con_impuesto`, con su comportamiento original. La salida final contiene 3 unidades, total 60, descuento 54.0 e impuesto 72.6.

## Respuestas

Aceptar el archivo entrante completo sustituiría también las partes con mejoras anteriores: por ejemplo, al integrar impuestos se podrían perder los descuentos y la presentación. Git combina texto, no demuestra que el programa funcione: una fusión sin conflictos puede dejar llamadas a funciones inexistentes o una fórmula incorrecta. Se ejecuta el programa tras cada paso y el verificador final sin modificarlo. Se conserva el historial de las tres ramas divergentes y sus tres fusiones.

## Evidencias solicitadas

Incluye en `INFORME.md` los conflictos de cada fusión, las decisiones para combinarlos, el gráfico final y las respuestas. Conserva las tres ramas para la revisión. No añadas `INFORME.md` a ningún commit.
