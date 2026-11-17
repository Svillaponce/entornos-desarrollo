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
