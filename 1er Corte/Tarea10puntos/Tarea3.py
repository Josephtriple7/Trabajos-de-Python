def calcular_compra(precio_por_docena, cantidad_docenas):
    descuento_mayor = 0.15  
    descuento_menor = 0.10  

    monto_compra = precio_por_docena * cantidad_docenas
    
    if cantidad_docenas > 3:
        descuento = monto_compra * descuento_mayor
    else:
        descuento = monto_compra * descuento_menor
    
    monto_a_pagar = monto_compra - descuento
    
    if cantidad_docenas > 3:
        unidades_obsequio = (cantidad_docenas - 3) * 1
    else:
        unidades_obsequio = 0
    
    return monto_compra, descuento, monto_a_pagar, unidades_obsequio

precio = float(input("Ingrese el precio por docena del producto: "))
cantidad = int(input("Ingrese la cantidad de docenas a comprar: "))

monto_compra, descuento, monto_a_pagar, unidades_obsequio = calcular_compra(precio, cantidad)

print(f"Monto de la compra: {monto_compra:.2f} córdobas")
print(f"Monto del descuento: {descuento:.2f} córdobas")
print(f"Monto a pagar: {monto_a_pagar:.2f} córdobas")
print(f"Unidades de obsequio: {unidades_obsequio}")