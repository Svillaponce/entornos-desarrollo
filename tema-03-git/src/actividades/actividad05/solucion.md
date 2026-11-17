# Actividad 5 — Dos funciones, dos ramas, una integración

## Solución paso a paso

Ejecuta los comandos en la terminal de Ubuntu y edita los archivos con PyCharm.
Los hashes mostrados son ejemplos de una ejecución; utiliza los de tu repositorio.

```bash
mkdir git-05-calculadora
cd git-05-calculadora
git init -b main
```

En `calculadora.py`, guarda este contenido:

```python
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("Suma:", sumar(8, 2))
```

En `README.md`, guarda este contenido:

```text
# Calculadora
Operaciones disponibles: suma.
```

```bash
git add calculadora.py README.md
git status --short
git diff --staged
git commit -m "Crear calculadora con suma"
git switch -c feature/multiplicar
```

En `calculadora.py`, guarda este contenido:

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
git status --short
git diff --staged
git commit -m "Añadir multiplicación"
git switch main
git merge --ff-only feature/multiplicar
git switch -c feature/dividir
```

En `calculadora.py`, guarda este contenido:

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
git status --short
git diff --staged
git commit -m "Añadir división con control de cero"
git log --oneline --graph --all --decorate
```

Resultado:

```text
* 07863db (HEAD -> feature/dividir) Añadir división con control de cero
* c4a57eb (main, feature/multiplicar) Añadir multiplicación
* bada5a4 Crear calculadora con suma
```

```bash
git switch main
git merge --no-ff feature/dividir -m "Integrar división"
```

En `README.md`, guarda este contenido:

```text
# Calculadora
Operaciones disponibles: suma, multiplicación y división.
La división por cero devuelve None.
```

```bash
git add README.md
git status --short
git diff --staged
git commit -m "Documentar las tres operaciones"
git branch -d feature/multiplicar feature/dividir
python3 calculadora.py
```

Resultado:

```text
Suma: 10
Multiplicación: 16
División: 4.0
```

```bash
python3 -c 'from calculadora import dividir; assert dividir(8, 0) is None; print(dividir(8, 0))'
```

Resultado:

```text
None
```

```bash
git log --oneline --graph --all --decorate
```

Resultado:

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
git status
```

Resultado:

```text
On branch main
nothing to commit, working tree clean
```

## Respuestas

La primera fusión puede ser fast-forward porque main es antecesora de la rama: no existen commits divergentes. `--ff-only` exige esa condición. La segunda usa `--no-ff` para conservar un nodo explícito de integración. Al terminar quedan **cinco commits**, de los que uno es una fusión, y solo la rama main.

## Evidencias solicitadas

Incluye en `INFORME.md` el gráfico anterior a la segunda fusión, el gráfico final y la explicación de fast-forward y `--no-ff`. Las dos ramas auxiliares deben haberse eliminado con `-d`. No añadas `INFORME.md` a ningún commit.
