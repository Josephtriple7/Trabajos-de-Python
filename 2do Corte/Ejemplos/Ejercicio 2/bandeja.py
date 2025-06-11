# bandeja.py
class BandejaPan:
    def __init__(self):
        self.bandeja = []

    def agregar_pan(self, tipo_pan):
        self.bandeja.append(tipo_pan)
        print(f"Pan agregado a la bandeja: {tipo_pan}")

    def vender_pan(self):
        if self.bandeja:
            pan = self.bandeja.pop()
            print(f"Pan vendido: {pan}")
        else:
            print("No hay panes en la bandeja para vender.")

    def ver_siguiente_pan(self):
        if self.bandeja:
            print(f"Pan listo para vender: {self.bandeja[-1]}")
        else:
            print("La bandeja está vacía.")
