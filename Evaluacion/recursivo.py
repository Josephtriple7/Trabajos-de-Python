def mcd(a,b):
    if b == 0: #se iguala b a 0 
        return a #de ser asi entonces sera a
    else:
        return mcd(b,a % b)
print("Ejepmlo de ")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
print(f"El MCD de {num1} y {num2} es {mcd(num1, num2)}")