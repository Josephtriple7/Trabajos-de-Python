def calcular_tarifa(tipo_vehiculo, distancia_km=0, toneladas=0):
    tarifas = {
        "bicicleta": 100,
        "moto": 30,
        "carro": 30,
        "camion": 30
    }
    
    if tipo_vehiculo == "bicicleta":
        return tarifas["bicicleta"]
    elif tipo_vehiculo in ["moto", "carro"]:
        return distancia_km * tarifas[tipo_vehiculo]
    elif tipo_vehiculo == "camion":
        return (distancia_km * tarifas["camion"]) + (toneladas * 25)
    else:
        return "Tipo de vehículo no válido"

vehiculo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camion): ").strip().lower()
distancia = float(input("Ingrese la distancia en Km: ")) if vehiculo != "bicicleta" else 0
toneladas = float(input("Ingrese la cantidad de toneladas: ")) if vehiculo == "camion" else 0

importe = calcular_tarifa(vehiculo, distancia, toneladas)
print(f"El importe a pagar es: {importe} córdobas")
