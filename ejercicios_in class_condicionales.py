# print("sistema de credito bancario")

# nom=input("ingrese su nombre completo: ")
# edad=int(input("ingrese su edad: "))
# credi=int(input("ingrese el monto del credito deseado: "))

# if edad >=18 and credi >=20000000:
#     print("{nom}cumple con los requisitos, su minto fue aprbado por el monto de {credi}")
# else: 
#     print("no cumple con los requisitos requeridos")

# print("sistema de precios de boletas")

# edad4=int(input("ingrese su edad: "))
# if edad==0 and edad4 <4:
#     print("entrada gratis")
# if edad ==4 and edad ==18: 
#     print("entrada de 5 euros")
# else:
#     print("es mayor de dad,paga 18 euros")


print("sistema de calculadora")
 
print("""""""MENU""""""""""""""""
        SUMA-------(+)
        RESTA------(-)
        MULTIPLICACION ----(*)
        DIVISION ----(/)""")

oper=input("ingrese alguna de las operaciiones que aparece en el menu:  ")

if oper== "+":
    nu= float(input("Ingrese un primer número: "))
    num= float(input("Ingrese un segundo número: "))
    sum= nu+num
    print(f" \nsu resultado de la suma es {sum}")
    
elif oper== "-":
    nu1= float(input("Ingrese un primer numero: "))
    num1=float(input("Ingrese un segundo número: "))
    res= nu1-num1
    print(f"\nSu resultado de la resta es {res}")
    
elif oper== "*":
    nu2= float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo numero: "))
    multipli= nu2*num2
    print(f"\nSu resultado de la multiplicacion  es {multipli}")
    
elif oper== "/":
    nu3=float(input("Ingrese su primer numero: "))
    num3=float(input("Ingrese su segundo numero: "))
    divici=nu3//num3
    print(f"\nSu resultado de la division es {divici:.1F}") # se utiliza el ".1F" para decidir cuantos decimales desea
    
else:
    print("no coincide con ningun simbolo de operacion")
