# Actividad 6 — Tres ramas que compiten por main

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Registrar en un solo commit pedido, README y el verificador suministrado. Que el verificador falle en esta versión es normal: faltan dos funciones.
2. Crear cada rama desde main sin fusionar ninguna todavía. En cada rama copiar la versión completa correspondiente y confirmar.
3. Comprobar con `git merge-base main HEAD` que todas nacen del mismo hash y guardar el gráfico previo.
4. Volver a main y fusionar presentación, descuentos e impuestos en ese orden. Se utiliza `--no-ff` para identificar explícitamente cada integración.
5. Ante cada conflicto inspeccionar `git status --short` y `git diff --cc`, editar el archivo, retirar las marcas y combinar funciones. Revisar lo preparado y confirmar para cerrar la fusión; `git commit` completa el merge pendiente, equivalente a terminarlo con `git merge --continue` tras preparar el resultado.
6. Ejecutar pedido tras cada fusión. La primera conserva el nuevo título, las unidades y el total; la segunda añade el descuento; la tercera añade el impuesto sin eliminar nada.
7. Ejecutar el verificador intacto. Conservar las tres ramas y comprobar main limpia.

## Conflictos y criterio de resolución

La primera fusión no tiene conflictos. Descuentos e impuestos modifican el mismo título y la presentación de `pedido.py`; las evidencias muestran los bloques concretos detectados por Git en cada paso. Se conserva `Gestor de pedidos`, la presentación con unidades y las funciones `calcular_total`, `calcular_con_descuento` y `calcular_con_impuesto`, con su comportamiento original. La salida final contiene 3 unidades, total 60, descuento 54.0 e impuesto 72.6.

## Respuestas

Aceptar el archivo entrante completo sustituiría también las partes con mejoras anteriores: por ejemplo, al integrar impuestos se podrían perder los descuentos y la presentación. Git combina texto, no demuestra que el programa funcione: una fusión sin conflictos puede dejar llamadas a funciones inexistentes o una fórmula incorrecta. Se ejecuta el programa tras cada paso y el verificador final sin modificarlo. Se conserva el historial de las tres ramas divergentes y sus tres fusiones.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-06-pedidos
cd git-06-pedidos
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

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Pedidos
Calcula el importe de un pedido.
```

Editar `verificar.py` en PyCharm y guardar este contenido completo:

```python
from pedido import calcular_total, calcular_con_descuento, calcular_con_impuesto
assert calcular_total(20, 3) == 60
assert calcular_con_descuento(20, 3, 10) == 54
assert calcular_con_impuesto(20, 3, 21) == 72.6
print("COMPROBACIONES SUPERADAS")
```

```bash
git add pedido.py README.md verificar.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
A  pedido.py
A  verificar.py
```

```bash
git diff --staged
```

```bash
git commit -m "Crear cálculo inicial y verificador de pedidos"
```

```bash
git rev-parse HEAD
```

Salida de referencia (los hashes pueden variar):

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
```

```bash
git switch -c feature/presentacion
```

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  pedido.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir presentacion a los pedidos"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
```

```bash
git switch -c feature/descuentos
```

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  pedido.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir descuentos a los pedidos"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git switch main
```

```bash
git switch -c feature/impuestos
```

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  pedido.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir impuestos a los pedidos"
```

```bash
git merge-base main HEAD
```

Salida de referencia (los hashes pueden variar):

```text
458c08752f0a94fe1596f658024c46aba38d6bdf
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

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
```

```bash
git merge --no-ff feature/presentacion -m "Integrar feature/presentacion"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* 8a669d3 (feature/descuentos) Añadir descuentos a los pedidos
| * a3a01cf (feature/impuestos) Añadir impuestos a los pedidos
|/  
| * 4339e6e (HEAD -> main) Integrar feature/presentacion
|/| 
| * 52f605a (feature/presentacion) Añadir presentacion a los pedidos
|/  
* 458c087 Crear cálculo inicial y verificador de pedidos
```

```bash
python3 pedido.py
```

Salida de referencia (los hashes pueden variar):

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

Salida de referencia (los hashes pueden variar):

```text
pedido.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
UU pedido.py
```

```bash
git diff --cc
```

Salida de referencia (los hashes pueden variar):

```text
diff --cc pedido.py
index 2b46ee0,9acd1a8..0000000
--- a/pedido.py
+++ b/pedido.py
@@@ -1,12 -1,14 +1,24 @@@
++<<<<<<< HEAD
 +TITULO = "Gestor de pedidos"
++=======
+ TITULO = "Pedidos con descuentos"
++>>>>>>> feature/descuentos
  
  def calcular_total(precio, cantidad):
      return precio * cantidad
  
+ def calcular_con_descuento(precio, cantidad, porcentaje):
+     return calcular_total(precio, cantidad) * (1 - porcentaje / 100)
+ 
  def mostrar(precio, cantidad):
++<<<<<<< HEAD
 +    print(f"*** {TITULO} ***")
 +    print(f"Unidades: {cantidad}")
 +    print("Total:", calcular_total(precio, cantidad))
++=======
+     print(f"=== {TITULO} ===")
+     print("Total con 10 % de descuento:", calcular_con_descuento(precio, cantidad, 10))
++>>>>>>> feature/descuentos
  
  if __name__ == "__main__":
      mostrar(20, 3)
```

Git ha detenido la fusión. Se combinan las funciones de ambos lados, se eliminan las marcas de conflicto y se conserva el resultado siguiente.

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  pedido.py
```

```bash
git diff --staged
```

```bash
git commit -m "Integrar feature/descuentos conservando las funcionalidades"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
*   511d199 (HEAD -> main) Integrar feature/descuentos conservando las funcionalidades
|\  
| * 8a669d3 (feature/descuentos) Añadir descuentos a los pedidos
* |   4339e6e Integrar feature/presentacion
|\ \  
| |/  
|/|   
| * 52f605a (feature/presentacion) Añadir presentacion a los pedidos
|/  
| * a3a01cf (feature/impuestos) Añadir impuestos a los pedidos
|/  
* 458c087 Crear cálculo inicial y verificador de pedidos
```

```bash
python3 pedido.py
```

Salida de referencia (los hashes pueden variar):

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

Salida de referencia (los hashes pueden variar):

```text
pedido.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
UU pedido.py
```

```bash
git diff --cc
```

Salida de referencia (los hashes pueden variar):

```text
diff --cc pedido.py
index 12713e2,dac5eee..0000000
--- a/pedido.py
+++ b/pedido.py
@@@ -1,16 -1,14 +1,29 @@@
++<<<<<<< HEAD
 +TITULO = "Gestor de pedidos"
++=======
+ TITULO = "Pedidos con impuestos"
++>>>>>>> feature/impuestos
  
  def calcular_total(precio, cantidad):
      return precio * cantidad
  
++<<<<<<< HEAD
 +def calcular_con_descuento(precio, cantidad, porcentaje):
 +    return calcular_total(precio, cantidad) * (1 - porcentaje / 100)
 +
 +def mostrar(precio, cantidad):
 +    print(f"*** {TITULO} ***")
 +    print(f"Unidades: {cantidad}")
 +    print("Total:", calcular_total(precio, cantidad))
 +    print("Total con 10 % de descuento:", calcular_con_descuento(precio, cantidad, 10))
++=======
+ def calcular_con_impuesto(precio, cantidad, porcentaje):
+     return round(calcular_total(precio, cantidad) * (1 + porcentaje / 100), 2)
+ 
+ def mostrar(precio, cantidad):
+     print(f"=== {TITULO} ===")
+     print("Total con 21 % de impuesto:", calcular_con_impuesto(precio, cantidad, 21))
++>>>>>>> feature/impuestos
  
  if __name__ == "__main__":
      mostrar(20, 3)
```

Git ha detenido la fusión. Se combinan las funciones de ambos lados, se eliminan las marcas de conflicto y se conserva el resultado siguiente.

Editar `pedido.py` en PyCharm y guardar este contenido completo:

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
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  pedido.py
```

```bash
git diff --staged
```

```bash
git commit -m "Integrar feature/impuestos conservando las funcionalidades"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

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
python3 pedido.py
```

Salida de referencia (los hashes pueden variar):

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

Salida de referencia (los hashes pueden variar):

```text
COMPROBACIONES SUPERADAS
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

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
