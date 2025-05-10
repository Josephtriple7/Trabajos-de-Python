# main.py

from Oficina import OficinaAtencionCiudadana

def menu_oficina():
    oficina = OficinaAtencionCiudadana()

    while True:
        print("\n--- Oficina de Atención Ciudadana ---")
        print("1. Agregar nuevo documento")
        print("2. Revisar último documento")
        print("3. Mostrar documentos pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            doc = input("Ingrese el nombre o tipo de documento: ")
            oficina.agregar_documento(doc)
        elif opcion == "2":
            oficina.revisar_documento()
        elif opcion == "3":
            oficina.mostrar_pendientes()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_oficina()
