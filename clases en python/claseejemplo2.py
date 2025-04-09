class Perro: 
    def __init__(self,nombre,raza,altura):
        self.nombre=nombre
        self.raza=raza
        self.altura=altura
        
    def comer(self):
        return "El perro esta comiendo"
    def dormir(self):
        return "El perro esta durmiendo"
    def ladrar(self):
        return "El perro esta ladrando"
firu = Perro('Yimi','Pastor aleman',0.6)

print(firu.nombre)
print(firu.raza)
print(firu.altura)
print(firu.comer())
print(firu.dormir())
print(firu.ladrar())