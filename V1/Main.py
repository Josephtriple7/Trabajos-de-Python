from Estudiantes import Estudiante
from Funciones import mostrar_menu, validar_entero_positivo, buscar_estudiante

lista_estudiantes = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Nombre del estudiante: ")
        edad_input = input("Edad: ")
        edad = validar_entero_positivo(edad_input)
        if edad is None:
            print("⚠️ Edad inválida.")
            continue
        carrera = input("Carrera: ")
        estudiante = Estudiante(nombre, edad, carrera)
        lista_estudiantes.append(estudiante)
        print("✅ Estudiante registrado.")

    elif opcion == '2':
        nombre = input("Nombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, lista_estudiantes)
        if estudiante:
            nota_input = input("Calificación a agregar (0-100): ")
            try:
                nota = float(nota_input)
                estudiante.agregar_calificacion(nota)
            except ValueError:
                print("⚠️ Calificación inválida.")
        else:
            print("⚠️ Estudiante no encontrado.")

    elif opcion == '3':
        nombre = input("Nombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, lista_estudiantes)
        if estudiante:
            estudiante.mostrar_info()
        else:
            print("⚠️ Estudiante no encontrado.")

    elif opcion == '4':
        if not lista_estudiantes:
            print("⚠️ No hay estudiantes registrados.")
        for est in lista_estudiantes:
            est.mostrar_info()
            print("-" * 30)

    elif opcion == '5':
        print("👋 ¡Hasta luego!")
        break
    else:
        print("⚠️ Opción no válida.")