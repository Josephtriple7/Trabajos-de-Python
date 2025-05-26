from Estructuras.cola import Cola

def crear_cola_con_elementos(elementos):
    cola = Cola()
    for elemento in elementos:
        cola.encolar(elemento)
    return cola

def mostrar_resultados(resultado):
    print("Cola (pares):", resultado["Cola (pares)"])
    print("Pila (impares):", resultado["Pila (impares)"])