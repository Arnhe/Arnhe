def nombre():
    n1=input("su nombre es: ")
    n2=input("su apellido es: ")
    print(f"su nombre completo es:{ n1 + n2 }") 

def edad():
    n3=input("escriba su edad:")
    edad=int(n3)
    print=(f"su edad es de:{n3}")

def sexo():
    n4=input("escriba su sexo:")
    print=(f"su sexo es:{n4}")
            
def peso():
    n5=input("escriba su peso:")
    peso=int(n5)
    print=(f"su peso es de:{n5}")
    
def altura():
    n6=input("escriba su altura:")
    altura=int(n6)
    print=(f"su altura es de:{n6}")
    
while True:
    print("presione 1 para escribir nombre completo")
    print("presione 2 para saber su edad")
    print("presione 3 para saber su sexo")
    print("presione 4 para saber su peso")
    print("presione 5 para saber su altura")

    x=int(input())
    if x==1:
        nombre()
    elif x==2:
        edad()
    elif x==3:
        sexo()
    elif x==4:
        peso()
    elif x==5:
        altura()
    else:
        break
             
            
