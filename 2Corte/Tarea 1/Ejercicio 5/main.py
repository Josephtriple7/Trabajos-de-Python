# main.py

from sacos import PilaSacos

def menu_logistica():
    pila = PilaSacos()

    while True:
        print("\n--- Logística de Carga - Mercado de Chinandega ---")
        print("1. Cargar saco al camión")
        print("2. Descargar saco del camión")
        print("3. Ver saco que está encima")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            descripcion = input("Descripción del saco: ")
            pila.cargar_saco(descripcion)
        elif opcion == "2":
            pila.descargar_saco()
        elif opcion == "3":
            pila.ver_saco_superior()
        elif opcion == "4":
            print("Finalizando proceso logístico. ¡Buen trabajo!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_logistica()
