# pila_tareas.py

class PilaTareas:
    def __init__(self):
        self.escritorio = []

    def agregar_tarea(self, descripcion):
        self.escritorio.append(descripcion)
        print(f"Tarea agregada al escritorio: {descripcion}")

    def revisar_tarea(self):
        if self.escritorio:
            tarea = self.escritorio.pop()
            print(f"Tarea revisada: {tarea}")
        else:
            print("No hay tareas para revisar.")

    def mostrar_siguiente_tarea(self):
        if self.escritorio:
            print(f"Siguiente tarea a revisar: {self.escritorio[-1]}")
        else:
            print("No hay tareas pendientes.")
