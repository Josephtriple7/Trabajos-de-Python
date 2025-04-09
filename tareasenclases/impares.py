def obtener_lista_impares(n):
    return list(range(1, n + 1, 2))

def main():
    lista_impares = []
    while True:
        opcion = input("\n(a) Ingresar un número impar (1-19)\n(b) Sumar la serie\n(c) Multiplicar la serie\n(d) Salir\nOpción: ").strip().lower()
        
        if opcion == 'a':
            try:
                n = int(input("Ingrese un número impar entre 1 y 19: "))
                if n % 2 == 1 and 1 <= n <= 19:
                    lista_impares = obtener_lista_impares(n)
                    print(f"Lista de impares: {lista_impares}")
                else:
                    print("Número fuera de rango o par.")
            except ValueError:
                print("Ingrese un número válido.")
        elif opcion in ('b', 'c'):
            if lista_impares:
                resultado = sum(lista_impares) if opcion == 'b' else eval('*'.join(map(str, lista_impares)))
                print(f"Resultado: {resultado}")
            else:
                print("Primero ingrese un número en 'a'.")
        elif opcion == 'd':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()