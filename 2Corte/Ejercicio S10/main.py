from Estructuras.cola import Cola
from Separadores.Separador import Separador
from Separadores.Separador import crear_cola_con_elementos, mostrar_resultados

def main():
    elementos = ['A', 'B', 'C', 'D', 'E']
    cola = crear_cola_con_elementos(elementos)
    resultado = Separador(cola).procesar()
    mostrar_resultados(resultado)

if __name__ == "__main__":
    main()