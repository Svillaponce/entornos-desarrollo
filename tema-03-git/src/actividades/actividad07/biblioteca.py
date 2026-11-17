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
