class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
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
        return result[::-1]  # De fondo a cima


def convBinario(numero):
    if numero == 0:
        return [0]

    pila = Stack()
    while numero > 0:
        resto = numero % 2
        pila.push(resto)
        numero //= 2

    binario = []
    while not pila.is_empty():
        binario.append(pila.pop())

    return binario

try:
    numero = int(input("Ingresa un número entero para convertir a binario: "))
    if numero < 0:
        print("Por favor ingresa un número entero no negativo.")
    else:
        resultado = convBinario(numero)
        print(f"El número {numero} en binario es: {''.join(map(str, resultado))}")
except ValueError:
    print("Entrada no válida. Debes ingresar un número entero.")
