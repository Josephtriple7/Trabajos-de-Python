from Clinica.farmacia3 import Patient, PharmacyQueue
# Línea agregada para forzar commit
def main():
    pharmacy = PharmacyQueue()
    valid_services = ["compra", "consulta", "receta"]
    
    while True:
        print("\nSistema de Gestión de Turnos - Farmacia")
        print("1. Registrar nuevo paciente")
        print("2. Atender al siguiente paciente")
        print("3. Mostrar turnos pendientes")
        print("4. Salir")
        
        option = input("Seleccione una opción (1-4): ")
        
        if option == "1":
            name = input("Ingrese el nombre del paciente: ")
            service = input("Ingrese el tipo de servicio (compra, consulta, receta): ").lower()
            if service in valid_services:
                pharmacy.add_patient(Patient(name, service))
            else:
                print("Error: Tipo de servicio inválido. Use compra, consulta o receta.")
        
        elif option == "2":
            print(pharmacy.serve_next())
        
        elif option == "3":
            print("\n" + pharmacy.show_pending())
        
        elif option == "4":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida, por favor seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
