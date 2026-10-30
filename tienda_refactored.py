# Constantes para descuentos y distancias
DESCUENTO_VIP = 0.8
DESCUENTO_ESTUDIANTE = 0.85
DESCUENTO_MAYORISTA = 0.7
DISTANCIA_LARGA = 100
DISTANCIA_MEDIA = 50
DESCUENTO_LARGO = 5
DESCUENTO_MEDIO = 2


def calcular_subtotal(productos):
    """Suma el precio por la cantidad de cada producto."""
    subtotal = 0
    for producto in productos:
        precio = producto[0]
        cantidad = producto[1]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento_cliente(total, tipo_cliente):
    """Aplica el descuento correspondiente al tipo de cliente."""
    if tipo_cliente == "vip":
        total *= DESCUENTO_VIP
    elif tipo_cliente == "est":
        total *= DESCUENTO_ESTUDIANTE
    elif tipo_cliente == "may":
        total *= DESCUENTO_MAYORISTA
    return total


def aplicar_descuento_distancia(total, distancia):
    """Aplica el descuento correspondiente a la distancia."""
    if distancia > DISTANCIA_LARGA:
        total -= DESCUENTO_LARGO
    elif distancia > DISTANCIA_MEDIA:
        total -= DESCUENTO_MEDIO
    return total


def calcular_total(productos, tipo_cliente, distancia):
    """Calcula el total final sin permitir importes negativos."""
    total = calcular_subtotal(productos)
    total = aplicar_descuento_cliente(total, tipo_cliente)
    total = aplicar_descuento_distancia(total, distancia)
    if total < 0:
        total = 0
    return total
