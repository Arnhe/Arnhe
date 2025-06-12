  def suma():
    num1 = int(input("escriba un numero: "))
    num2 = int(input("escriba un numero: "))
    resultado = num1 + num2
    print(f"la suma es: {resultado}")

def resta():
    num1 = int(input("escriba un numero: "))
    num2 = int(input("escriba un numero: "))
    resultado = num1 - num2
    print(f"la resta es: {resultado}")

def multiplicar():
    num1 = int(input("escriba un numero: "))
    num2 = int(input("escriba un numero: "))
    resultado = num1 * num2
    print(f"la multiplicacion es: {resultado}")

while True:
    print("presione 1 para suma")
    print("presione 2 para restar")
    print("presione 3 para multiplicar")

    x = int(input("Ingrese su opción: "))

    if x == 1:
        suma()
    elif x == 2:
        resta()
    elif x == 3:
        multiplicar()
    else:
        print
