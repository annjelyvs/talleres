# #Taller de condicionales y diagramas
# print("EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS\n")

# #1. Verificar si un numero es positivo, negativo o cero
# print("primer ejercicio ")

# num33= float(input("Ingrese un numero positivo, negetivo o cero: "))
# if num33 >0:
#     print(f"Su numero {num33} es positivo")
# elif num33 <0:
#     print(f"Su numero {num33} es negativo")
# else:
#     print("Su numero es cero")


# #2. Calcular el mayor de dos numeros ingresados 
# print("segundo ejercicio")

# num28= int(input("Ingresa un numero: "))
# num19= int(input("Ingresa un segundo numero: "))
# if num28 > num19:
#     print(f"El numero {num28} es mayor que {num19}")
# else:
#     print(f"El numero {num19} es mayor que {num28}")


# #DETERMINA SI ES UN NUMERO ES PAR O IMPAR
# print("EJERCICIO 3")

# nume2= (float(input("Ingresa un numero : ")))
# if nume2 %2==0:
#     print("el numero es par ")
# else:
#     print("el numero es impar")
    

# #DADO UN NUMERO, VERIFICA SI ESTA ENTRE   10 y 20
# print(f"cuarto ejercicio")

# num333=int(input("ingrese un numero: "))
# if num333 >=10 and num333 <=20:
#     print(f"el numero {num333} esta entre 10 y 20")
# else:
#     print(f"el numero {num333} no esta entre 10 y 20")
    
    
# #DADOS TRES NUMEROS, ENCUENTRA EL MAYOR UTILIZANDO CONDICIONALES 
# print("ejercicio numero 5")
# print(f"quinto ejercicio")
# num70=int(input("ingrese un numero: "))
# num5=int(input("ingrese un segundo numero: "))
# num9=int(input("ingrese un tercer numero: "))

# if num70 >= num5 and num70 >= num9:
#     print(f"el numero {num70} es mayor")
# elif num5 >= num70 and num70>= num9:
#     print(f"el numero {num5} es mayor")
# else:
#     print(f"el numero {num9} es mayor")

# #calcule el 10% de descuento si el total es mayor a $100
# print("ejercicio numero 6")

# facture=float(input("ingrese el monto total: "))
# if facture > 100:
#     print(f"el descuento es de {facture * 0.1:.1F} ")
# else:
#     print(f"su monto fue de {facture} por lo cual no tiene descuento")
    
# #VERIFICA SI UNA PERSOAN PUEDE VOAR ( MAYOR O IGUAL A 18 AÑOS)
# print("ejercicio numero 7")

# edad2=int(input("ingrese su edad: "))
# if edad2 >= 18:
#     print(f" puede votar ya que tiene {edad2}")
# else:
#     print(f"no puede votar ya que tiene {edad2}")


# #DADO EL PRECIO Y  TIPO DE CLIENTE ( VIP  o normal), APLICA UN DESCUENTO DEL 20% SOLO A VIP
# print("ejercicio numero 8 ")

# precio=float(input("ingrese el precio: "))
# tipo_cliente=input("ingrese si es tipo de cliente VIP o normal: ").lower()

# if tipo_cliente == "VIP":
#     print(f"tu descuento es de {precio*0.2:.2F}")
# else:
#     print(f"no tienes descuento ya que eres cliente {tipo_cliente}")

#DETERMINA SI UN NUMERO ES MULTIPLO DE  Y DE 3 AL MISMO TIEMPO
# print("ejercicio numero 9")

# multiplo=int(input("ingrese un numero: "))

# if multiplo % 5 ==0 and multiplo %3 == 0:
#     print(f"{multiplo} es multiplo de 5 y 3")
# else:
#     print(f"el numero{multiplo} no es multiplo de 5 y 3")


# #DADO UN NUMERO, VERIFICA SI ES DIVISIBLE ENTRE DOS NUMEROS DADOS
# print(" EJERCICIO NUMERO 10")

# num22=int(input("ingresa un numero:  "))
# num23=int(input("ingrese el primero numero divisor: "))
# num24=int(input("ingrese el segundo numero divisor:  "))

# if num22 % num23 == 0 and num22 % num24 ==0:
#     print(f"{num22} es divicible entre {num23} y {num24}")
# else:
#     print(f"{num22} no es divisible entre {num23} y {num24}")


# print("EJERCICIOS CON LISTAS Y CON CONDICIONALES ")

# print("ejercicio numero 11")
# #crear lista y mostrar mayor que 10 o menor que 10
# lista=[5,10,5,6,15]
# if lista[2]>10:
#     print(f"el numero {lista[2]}  es mayor a 10")
# else:
#     print(f"el numero {lista[2]} es menor o igual a 10")
    
# print("ejercicio numero 12")   

# lista2=[3,5,7,9]
# if 7 in lista2:
#     print("el numero 7 esta en la lista")
# else:
#     print("el numero 7 no esta en la lista")
    
# print("ejercicio numero 13")

# lista3=[4,6,2,8]
# suma= lista3[0]+lista3[1]
# if suma >10:
#     print(f"la suma es alta ya que el resultado es {suma}")
# else:
#     print(f"la suma es baja ya que el resultado es {suma}")

# print("ejercicio numero 14")

# lista4=["ana","luis","pedro", "marta"]
# ulti=lista4[3]
# if ulti=="marta":
#     print(f"nombre {ulti} es correcto")
# else:
#     print(f"el nombre {ulti} no es correcto")

# print("ejercicio numero 15")

# colores = ["rojo", "azul", "verde"]
# if colores[1] == "azul":
#     colores[1] = "amarillo" 
# print(colores)


# print("EJERCICIOS DE TUPLAS CON CONDICIONALES")
# print("ejercicio numero 16")

# tupla=(5,8,12,20)
# if tupla[0]< tupla[-1]:
#     print("orden ascendente")
# else:
#     print("orden desendente")

# print("ejercicio numero 17")
# tupla2=(25,32,28)
# if tupla2[1]>30:
#     print("edad mayor a 30")
# else:
#     print("edad menor o igual a 30")
    
# print("ejercicio numero 18")
# tupla = (1, 2, 3)
# lista = list(tupla)
# if lista[1] == 2:
#     lista[1] = 10
# tupla_resultante = tuple(lista)
# print(tupla_resultante)

# print("ejercicio 19")
# tupla4=(4, 9) 
# Valor= tupla[1]
# if Valor>5:
#     print("coordenada alta") 
# else:
#    print("coordenada baja") 

# print("ejercicio 20")
# tupla21=(3, 4) 
# tupla22=(3, 5) 
# if tupla21 == tupla22:
#     print("las tuplas son iguales") 
# else:
#     print("las tuplas son diferentes ")

# print("ejercicio 21")
# Dic={"nombre" : "Juan", 
# "edad":17}
# if Dic["edad"]>=18:
#     print("adulto") 
# else:
#     print("usted es menor de edas")

# print("ejercicio 22")
# Dic2={"nombre": "Lucía", 
# "edad": 20}
# if Dic2["edad"] > 18:
#     Dic2 ["edad"] = 21
# print(Dic2)

# print("ejercicio 23")
# print("\nagregar clave")
# dic3 = {"nombre": "Carlos"}
# print(dic3)
# if "ciudad" not in dic3:
#     dic3["ciudad"] = "Bogotá"
# print(f"Diccionario actualizado {dic3}")

# print("ejercicio 24")
# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")

# print("ejercicico 25")
# precios = {"pan": 1200, "leche": 2000}
# if "pan" in precios:
#     print(precios["pan"])
# else:
#     print("Producto no disponible")