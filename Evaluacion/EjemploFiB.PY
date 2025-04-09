def recursivo(valor):
    if(valor>0):
        print("valor: ",valor)
        recursivo(valor-1)
recursivo(5)