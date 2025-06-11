# pila_donantes.py

class PilaDonantes:
    def __init__(self):
        self.pila = []

    def registrar_donante(self, nombre):
        self.pila.append(nombre)
        print(f"Donante registrado: {nombre}")

    def revertir_registro(self):
        if self.pila:
            eliminado = self.pila.pop()
            print(f"Registro revertido: {eliminado}")
        else:
            print("No hay registros para revertir.")

    def mostrar_donante_actual(self):
        if self.pila:
            print(f"Donante actual en proceso: {self.pila[-1]}")
        else:
            print("No hay donantes registrados.")
