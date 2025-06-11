def es_capicua(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

numero = int(input("Ingrese un número de tres cifras: "))

if 100 <= numero <= 999:
    if es_capicua(numero):
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")
else:
    print("Por favor, ingrese un número de tres cifras.")