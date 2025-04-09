#Ejemplificando clases en python
class Alumno:
    def __init__(self,nombre,edad): # siempre poner dos guiones bajo a cada lado del "init"
        self.nombre=nombre # simepre poner "self." antes de cada propiedad
        self.edad=edad # estas son propiedades, al utilizarlos siempre tiene que llamarse en orden de como lo declare en la definicion

    def saludar(self):
        print(f"Hola,{self.nombre}\nLa edad es: {self.edad}")