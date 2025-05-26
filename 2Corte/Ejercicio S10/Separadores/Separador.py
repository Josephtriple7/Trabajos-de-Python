from Estructuras.cola import Cola
from Estructuras.pila import Pila

class Separador:
    def __init__(self, cola):
        self.cola_original = cola
        self.cola_pares = Cola()
        self.pila_impares = Pila()

    def procesar(self):
        posicion = 0
        while not self.cola_original.esta_vacia():
            elemento = self.cola_original.desencolar()
            if posicion % 2 == 0:
                self.cola_pares.encolar(elemento)
            else:
                self.pila_impares.apilar(elemento)
            posicion += 1

        return {
            "Cola (pares)": self.cola_pares.mostrar(),
            "Pila (impares)": self.pila_impares.mostrar()
        }