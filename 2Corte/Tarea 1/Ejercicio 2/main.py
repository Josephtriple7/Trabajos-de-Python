# main.py

from bandeja import BandejaPan

def menu_panaderia():
    bandeja = BandejaPan()

    while True:
        print("\n--- Panadería Tradicional en León ---")
        print("1. Agregar pan a la bandeja")
        print("2. Vender pan")
        print("3. Ver pan listo para vender")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de pan: ")
            bandeja.agregar_pan(tipo)
        elif opcion == "2":
            bandeja.vender_pan()
        elif opcion == "3":
            bandeja.ver_siguiente_pan()
        elif opcion == "4":
            print("¡Hasta luego! Gracias por visitar la panadería.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_panaderia()
