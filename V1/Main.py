from Estudiantes import Estudiante
from Funciones import mostrar_menu, validar_entero_positivo, buscar_estudiante

lista_estudiantes = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        print("\n/---- REGISTRO DE ESTUDIANTE ----\\")
        nombre = input("| Nombre: ")
        edad_input = input("| Edad: ")
        edad = validar_entero_positivo(edad_input)
        if edad is None:
            print("| ⚠️ Edad inválida. Debe ser un número entero positivo.")
            continue
        carrera = input("| Carrera: ")
        estudiante = Estudiante(nombre, edad, carrera)
        lista_estudiantes.append(estudiante)
        print("\\ Estudiante registrado con éxito. /")

    elif opcion == '2':
        nombre = input("\nIngrese el nombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, lista_estudiantes)
        if estudiante:
            nota_input = input("Ingrese la calificación (0-100): ")
            try:
                nota = float(nota_input)
                estudiante.agregar_calificacion(nota)
            except ValueError:
                print("│ ⚠️ Calificación inválida.")
        else:
            print("│ ⚠️ Estudiante no encontrado.")

    elif opcion == '3':
        nombre = input("\nNombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, lista_estudiantes)
        if estudiante:
            estudiante.mostrar_info()
        else:
            print("│ ⚠️ Estudiante no encontrado.")

    elif opcion == '4':
        print("\n/---- LISTA DE ESTUDIANTES ----\\")
        if not lista_estudiantes:
            print("| ⚠️ No hay estudiantes registrados.           |")
        for est in lista_estudiantes:
            est.mostrar_info()
        print("\\--------------------------------/")

    elif opcion == '5':
        print("\n\\ Gracias por usar el programa. ¡Hasta luego! /")
        break
    else:
        print("│ ⚠️ Opción no válida. Intente de nuevo.")