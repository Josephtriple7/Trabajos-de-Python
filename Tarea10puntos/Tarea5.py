import math

def calcular_area():
    while True:
        print("========================================")
        print("CÁLCULO DE SUPERFICIES (versión 1.0)")
        print("========================================")
        print("1. Cuadrado")
        print("2. Círculo")
        print("3. Rectángulo")
        print("4. Trapecio")
        print("5. Triángulo")
        opcion = input("Seleccione una opción (1-5): ")
        
        if not opcion.isdigit() or int(opcion) not in range(1, 6):
            print("Opción no válida. Inténtelo de nuevo.")
            continue
        
        opcion = int(opcion)
        area = 0
        
        if opcion == 1:  # Cuadrado
            lado = float(input("Ingrese el lado: "))
            area = lado ** 2
        elif opcion == 2:  # Círculo
            radio = float(input("Ingrese el radio: "))
            area = math.pi * radio ** 2
        elif opcion == 3:  # Rectángulo
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = base * altura
        elif opcion == 4:  # Trapecio
            base1 = float(input("Ingrese la base 1: "))
            base2 = float(input("Ingrese la base 2: "))
            altura = float(input("Ingrese la altura: "))
            area = (base1 + base2) * altura / 2
        elif opcion == 5:  # Triángulo
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = (base * altura) / 2
        
        print(f"El área calculada es: {area:.2f}")
        
        continuar = input("¿Desea calcular otra área? (S/N): ").strip().upper()
        if continuar != "S":
            break
    
    print("Programa finalizado.")

if __name__ == "__main__":
    calcular_area()
