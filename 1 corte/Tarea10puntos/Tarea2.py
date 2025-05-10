def calcular_subtotal(precio_unitario, cantidad):
    """Calcula el subtotal de la compra."""
    return precio_unitario * cantidad

def calcular_iva(subtotal):
    """Calcula el IVA del 15% sobre el subtotal."""
    return subtotal * 0.15

def calcular_descuento(subtotal):
    """Aplica un descuento del 12% si el subtotal supera los 1000."""
    if subtotal > 1000:
        return subtotal * 0.12
    else:
        return 0

def calcular_total(subtotal, iva, descuento):
    """Calcula el total final de la factura."""
    return subtotal + iva - descuento

def emitir_factura(nombre_articulo, precio_unitario, cantidad):
    """Emitir la factura."""
    subtotal = calcular_subtotal(precio_unitario, cantidad)
    iva = calcular_iva(subtotal)
    descuento = calcular_descuento(subtotal)
    total = calcular_total(subtotal, iva, descuento)

    print("\n**FACTURA**")
    print(f"Artículo: {nombre_articulo}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad} unidades")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    if descuento > 0:
        print(f"Descuento (12%): -${descuento:.2f}")
    else:
        print("Descuento: No aplica")
    print(f"Total: ${total:.2f}")
   
nombre_articulo = input("Ingrese el nombre del artículo: ")
precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

emitir_factura(nombre_articulo, precio_unitario, cantidad)