INCIDENCIAS = ["Pantalla rota", "Impresora sin papel", "Red sin conexión"]

def listar():
    for indice, incidencia in enumerate(INCIDENCIAS, start=1):
        print(f"{indice}. {incidencia}")

if __name__ == "__main__":
    listar()
