class Estudiante:
    def __init__(self,name,nota):
        self.name=name
        self.nota=nota

Estudiante=Estudiante(input("Ingresa tu nombre: "),int(input("Ingresa tu nota: ")))