import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        '''Inicializa el grafo como un diccionario varío,
        la clave es el vértice y el valor es una lista tuplas (vecino, peso)'''
        self.grafo = {}
        #Define si el grafo es dirigido o no
        self.es_dirigido = es_dirigido
        
    def agregar_vertice(self, vertice):
        #Agregar un vértice si no existe
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            #Lista vacía de vecinos
            print(f"Vertice '{vertice}' agregado.")
        else:
            print(f"Vertice '{vertice}' ya existe.")
    
    def agregar_arista(self, u, v, peso=1):
        #Asegura que ambos vertices existen: sino, los agrega automaticamente
        self.agregar_vertice(u)
        self.agregar_vertice[v]
        
        #Agregar una arista desde u hacia v con el peso especificado
        self.grafo[u].append((v, peso))
        print(f"Arista agregada: {u} -> {v} con peso {peso}")
        
        #Si el grafo no es dirigido, tambien se debe agregar la arista opiuesta (de v a u)
        if not self.es_dirigido:
            self.grafo[v].append((u, peso))
            print(f"Arista agregada: {v} -> {u} con peso {peso} (bidireccional)")
            
    def obtener_vecinos(self, vertice):
        #Devuelve la lista de vecinos de un vertice
        if vertice in self.grafo:
            #Extrae solo los nombres de las vecinos (ignorando el peso)
            return [vecino for vecino, in self.grafo[vertice]]
        else:
            #Si el vertice no existe, lo reporta y devuelve la lista vacía
            print(f"Advertencia: vertice '{vertice}' no existe.")
            return []
    
    def existe_arista(self, u, v):
        #Verifica si existe una arista desde u hacia v
        if u in self.grafo:
            #Busca entre las conexciones del vertice u si esta el vertice v
            return any(vecino == v for vecino, in self.grafo[u])
        return False
        #Si u no existe, no puede haber una arista

#-----------------------PRUEBA DE IMPLEMENTACIÓN----------------------------------        

print("\n--- Grafo no dirigido ---")
#Crea una instancia de grafo no dirigido

grafo_nd = Grafo(es_dirigido=False)

#Agrega manualmente los vertices A, B, C, D, E
for vertice in ['A', 'B', 'C', 'D', 'E']:
    grafo_nd.agregar_vertice(vertice)
    
#Agrega las aristas ( conexiones entre vertices)

grafo_nd.agregar_arista('A', 'B')
grafo_nd.agregar_arista('A', 'C')
grafo_nd.agregar_arista('B', 'D')
grafo_nd.agregar_arista('C', 'D')
grafo_nd.agregar_arista('D', 'E')

#Muestra los vecinos de algunos vertices
print(f"Vecinos de A: {grafo_nd.obtener_vecinos('A')}")
print(f"Vecinos de D: {grafo_nd.obtener_vecinos('D')}")
print(f"Vecinos de F: {grafo_nd.obtener_vecinos('F')}")
# Como F no existe deberia dar advertencia

#Verificar si existen ciertas aristas
print(f"¿Existe arista entre A y C? {grafo_nd.existe_arista('A', 'C')}")
print(f"¿Existe arista entre A y D? {grafo_nd.existe_arista('A', 'D')}")

#----------GRAFO DIRIGIDO----------

print("\n--- Grafo dirigido ---")
#Crea una nueva instancia de grafo, pero esta vez es dirigido

grafo_d= Grafo(es_dirigido=True)

#Agrega algunas aristas (automaticamente se crean los vertices)

grafo_d.agregar_arista('X', 'Y')
grafo_d.agregar_arista('Y', 'Z')
grafo_d.agregar_arista('X', 'Z')

#Muestra los vecinos de X y Y
print(f"Vecinos de Y: {grafo_d.obtener_vecinos('X')}")
print(f"Vecinos de Y: {grafo_d.obtener_vecinos('Y')}")