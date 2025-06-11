# pila_sacos.py

class PilaSacos:
    def __init__(self):
        self.camion = []

    def cargar_saco(self, descripcion):
        self.camion.append(descripcion)
        print(f"Saco cargado al camión: {descripcion}")

    def descargar_saco(self):
        if self.camion:
            saco = self.camion.pop()
            print(f"Saco descargado: {saco}")
        else:
            print("No hay sacos para descargar.")

    def ver_saco_superior(self):
        if self.camion:
            print(f"Saco encima (listo para descargar): {self.camion[-1]}")
        else:
            print("El camión está vacío.")
