# Definir un nodo para la pila
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Definir la pila
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def to_list(self):
        current = self.top
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result[::-1]  # fondo a cima

# Método para separar pares e impares
def separarParImpar(stack):
    pares = Stack()
    impares = Stack()
    lista_pares = []
    lista_impares = []

    while not stack.is_empty():
        num = stack.pop()
        if num % 2 == 0:
            pares.push(num)
            lista_pares.append(num)
        else:
            impares.push(num)
            lista_impares.append(num)

    result = Stack()
    while not pares.is_empty():
        result.push(pares.pop())
    while not impares.is_empty():
        result.push(impares.pop())

    return result, lista_pares, lista_impares

# =============================
# Entrada manual y ejecución
# =============================
try:
    entrada = list(map(int, input("Ingresa números separados por espacio: ").split()))
    pila = Stack()
    for num in entrada:
        pila.push(num)

    resultado, pares, impares = separarParImpar(pila)

    print("\nNúmeros pares:", pares)
    print("Números impares:", impares)
    print("Pila resultante (pares izquiera, impares derecha):", resultado.to_list())

except ValueError:
    print("Entrada no válida. Asegúrate de ingresar solo números enteros.")
