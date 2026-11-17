# Actividad 5 — Dos funciones, dos ramas, una integración

Fuente: *Actividades tema 3 - Comandos de Git básicos*, Sebastián Villa Ponce, 08/11/2026.

## Pasos y decisiones

1. Registrar suma y README en el commit inicial.
2. Crear `feature/multiplicar`, sustituir el archivo por la versión suministrada y confirmar.
3. Volver a `main` y fusionar con `git merge --ff-only feature/multiplicar`: main no ha avanzado, de modo que solo se mueve su referencia.
4. Desde esa main actualizada crear `feature/dividir`, añadir división y confirmar. Guardar aquí el primer gráfico obligatorio.
5. Volver a main y usar `git merge --no-ff feature/dividir -m ...`: se crea un commit con dos padres aunque fuera posible un avance directo.
6. Documentar las tres operaciones en main y confirmar. Eliminar las ramas con `git branch -d`, que verifica su integración.
7. Ejecutar: suma 10, multiplicación 16 y división 4.0. Comprobar por separado que dividir entre cero devuelve `None`.

## Respuestas

La primera fusión puede ser fast-forward porque main es antecesora de la rama: no existen commits divergentes. `--ff-only` exige esa condición. La segunda usa `--no-ff` para conservar un nodo explícito de integración. Al terminar quedan **cinco commits**, de los que uno es una fusión, y solo la rama main. Los dos gráficos solicitados están en las evidencias.

## Desarrollo completo en la terminal de Ubuntu

Trabaja en una carpeta nueva fuera del repositorio de clase. Los archivos Python
que acompañan este documento contienen el resultado final; para realizar la
actividad se parte de las versiones iniciales que se muestran a continuación.
Edita los archivos en PyCharm y ejecuta los comandos desde esta carpeta.
No se necesitan dependencias externas ni conexión a GitHub.

```bash
mkdir git-05-calculadora
cd git-05-calculadora
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

Editar `calculadora.py` en PyCharm y guardar este contenido completo:

```python
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("Suma:", sumar(8, 2))
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Calculadora
Operaciones disponibles: suma.
```

```bash
git add calculadora.py README.md
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
A  README.md
A  calculadora.py
```

```bash
git diff --staged
```

```bash
git commit -m "Crear calculadora con suma"
```

```bash
git switch -c feature/multiplicar
```

Editar `calculadora.py` en PyCharm y guardar este contenido completo:

```python
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print("Suma:", sumar(8, 2))
    print("Multiplicación:", multiplicar(8, 2))
```

```bash
git add calculadora.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  calculadora.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir multiplicación"
```

```bash
git switch main
```

```bash
git merge --ff-only feature/multiplicar
```

```bash
git switch -c feature/dividir
```

Editar `calculadora.py` en PyCharm y guardar este contenido completo:

```python
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    print("Suma:", sumar(8, 2))
    print("Multiplicación:", multiplicar(8, 2))
    print("División:", dividir(8, 2))
```

```bash
git add calculadora.py
```

```bash
git status --short
```

Salida de referencia (los hashes pueden variar):

```text
M  calculadora.py
```

```bash
git diff --staged
```

```bash
git commit -m "Añadir división con control de cero"
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* 07863db (HEAD -> feature/dividir) Añadir división con control de cero
* c4a57eb (main, feature/multiplicar) Añadir multiplicación
* bada5a4 Crear calculadora con suma
```

```bash
git switch main
```

```bash
git merge --no-ff feature/dividir -m "Integrar división"
```

Editar `README.md` en PyCharm y guardar este contenido completo:

```text
# Calculadora
Operaciones disponibles: suma, multiplicación y división.
La división por cero devuelve None.
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
git commit -m "Documentar las tres operaciones"
```

```bash
git branch -d feature/multiplicar feature/dividir
```

```bash
python3 calculadora.py
```

Salida de referencia (los hashes pueden variar):

```text
Suma: 10
Multiplicación: 16
División: 4.0
```

```bash
python3 -c 'from calculadora import dividir; assert dividir(8, 0) is None; print(dividir(8, 0))'
```

Salida de referencia (los hashes pueden variar):

```text
None
```

```bash
git log --oneline --graph --all --decorate
```

Salida de referencia (los hashes pueden variar):

```text
* c46f1f5 (HEAD -> main) Documentar las tres operaciones
*   d4d9ab3 Integrar división
|\  
| * 07863db Añadir división con control de cero
|/  
* c4a57eb Añadir multiplicación
* bada5a4 Crear calculadora con suma
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
