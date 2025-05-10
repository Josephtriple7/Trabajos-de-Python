# main.py

from donantes import PilaDonantes

def menu_donacion():
    pila = PilaDonantes()

    while True:
        print("\n--- Campaña de Donación de Sangre - Estelí ---")
        print("1. Registrar donante")
        print("2. Revertir último registro")
        print("3. Mostrar donante actual en proceso")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del donante: ")
            pila.registrar_donante(nombre)
        elif opcion == "2":
            pila.revertir_registro()
        elif opcion == "3":
            pila.mostrar_donante_actual()
        elif opcion == "4":
            print("Gracias por colaborar con la campaña.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_donacion()
