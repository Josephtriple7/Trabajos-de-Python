# main.py

from tareas import PilaTareas

def menu_revision():
    pila = PilaTareas()

    while True:
        print("\n--- Revisión de Tareas - Docente de Informática ---")
        print("1. Agregar nueva tarea")
        print("2. Revisar tarea")
        print("3. Mostrar siguiente tarea a revisar")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            pila.agregar_tarea(descripcion)
        elif opcion == "2":
            pila.revisar_tarea()
        elif opcion == "3":
            pila.mostrar_siguiente_tarea()
        elif opcion == "4":
            print("Finalizando revisión de tareas. ¡Buen trabajo!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_revision()
