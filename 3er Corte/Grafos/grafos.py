import collections

class Grafo: 
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, vertice):      
        '''Si el vertice no está en el diccionario,
        lo añade con un conjunto vacio de vecinos. '''
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice '{vertice}' agregado. ")
        else: 
            print(f"Vértice '{vertice}' ya existe. ")
    
    def agregar_arista(self, u, v, peso=1):
        #Asegure de que ambos vértices existen en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #Añadir la arista
        self.grafo[u].add(v)
        print(f"Arista {u}  -> {v} agregada. ")
        
        #Si no es dirigido, añadir la arista en la direccion opuesta tambien
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregado")
    
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])
            #Convertir a lista para devolver
        return []
        #Si el vertice no existe, no tiene vecinos
    
    def existe_arista(self, u, v):
        #Verifica si ambos vertcies existen y si 'v' esta en la lista de adyacencia de 'u'
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set()
        #Conjunto para guardar los vertices ya visitados
        cola = collections.deque()
        # cola para los vertices a visitar
        
        # Empezar el recorrido desde el vertice inicial
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = []
        #Lista para almacenar el orden de visita
        
        while cola:
            vertice_actual = cola.popleft()
            #Sacar el primer elemento de la cola
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            
            #Añadir a la cola los vecinos no visitados
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido
    
    def dfs(self, inicio):
        visitados = set()