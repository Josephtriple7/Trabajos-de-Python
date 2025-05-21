# Importa la clase TurnoFarmacia desde el archivo Turno.py
from Turno import TurnoFarmacia

# Función principal que controla el menú del sistema
def main():
    # Crea una instancia de la clase TurnoFarmacia
    farmacia = TurnoFarmacia()

    # Bucle principal del programa
    while True:
        # Muestra el menú de opciones
        print("\n--- Gestión de Turnos en Farmacia ---")
        print("1. Registrar nuevo paciente")
        print("2. Atender siguiente paciente")
        print("3. Mostrar turnos pendientes")
        print("4. Salir")

        # Solicita al usuario que elija una opción
        opcion = input("Seleccione una opción: ")

        # Opción 1: Registrar nuevo paciente
        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            servicio = input("Ingrese el tipo de servicio (compra, consulta, receta): ")
            farmacia.registrar_paciente(nombre, servicio)

        # Opción 2: Atender al siguiente paciente
        elif opcion == "2":
            farmacia.atender_paciente()

        # Opción 3: Mostrar todos los turnos pendientes
        elif opcion == "3":
            farmacia.mostrar_turnos_pendientes()

        # Opción 4: Salir del programa
        elif opcion == "4":
            print("Saliendo del sistema.")
            break

        # Si la opción no es válida
        else:
            print("Opción no válida. Intente nuevamente.")

# Este bloque asegura que main() se ejecute solo si este archivo es el principal
if __name__ == "__main__":
    main()