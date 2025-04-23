#La práctica consiste en desarrollar un pequeño programa que permita registrar estudiantes, agregarles calificaciones 
# y generar reportes de su información, incluyendo el promedio de notas.
#Organizar el código utilizando funciones y clases, y separar las partes 
# del programa en módulos (es decir, en archivos .py diferentes).

def mostrar_menu():
    print("\n/-------------------------------\\")
    print("|        MENÚ PRINCIPAL         |")
    print("|-------------------------------|")
    print("| 1. Registrar nuevo estudiante |")
    print("| 2. Agregar calificación       |")
    print("| 3. Mostrar info de estudiante |")
    print("| 4. Mostrar todos los alumnos  |")
    print("| 5. Salir                      |")
    print("\\-------------------------------/")

def validar_entero_positivo(entrada):
    try:
        valor = int(entrada)
        return valor if valor > 0 else None
    except ValueError:
        return None

def buscar_estudiante(nombre, lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None