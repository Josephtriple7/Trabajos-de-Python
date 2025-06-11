class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente=None
class cola:
    def __init__(self):
        self.frente=None
        self.final=None
    
    def insertar(self,dato):
        nuevo=Nodo(dato)
        if self.final is None:  
            self.frente=self.final=nuevo
            print(f"Elemento '{dato}' insertado")
            return None
        eliminado=self.frente.dato
        self.frente=self.frente.siguiente
        if self.frente is None:
            #si cola queda vacia
            self.final=None
        print(f"Elemento '{eliminado}' eliminado")
        return eliminado
    
    #Metodo para imprimir datos de la cola
    def imprimir(self):
        if self.frente is None:
            print("Cola vacia")
        else: 
            print("Contenido de la cola desde frente al final")
            actual=self.frente
            while actual is None:
                print(actual.dato)
                actual=actual.siguiente