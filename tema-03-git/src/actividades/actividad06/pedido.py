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
