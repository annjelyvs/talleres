# print("ejercicios de while")

# print("ejercicio1")
# print("Suma hasta cero")


# total = 0
# while True:
#     num1 = int(input("ingrese un numero (0 para terminar):  "))
#     if num1 == 0:
#         break
#     total += num1
#     print(f"Su total es {total}")
# print("Programa finalizado")


# print("ejerciico 2")
#print("Contraseña secreta")

# contraseña=input("Escribe la contraseña: ")
# while contraseña!= "python123":
#     print("Contraseña incorrecta")
#     contraseña=input("Intenta de nuevo: ")
# print("¡Bienvenido!")

# print("ejercicio 3")
#print("Lista de compras")

# productos=[]
# while True:
#     produc=input("ingrese un producto (fin para salir): ").lower()
#     productos.append(produc)
#     if produc == "fin":
#         print(f"el programa finalizo  {produc}")
#         break

# print("ejercicio 4")
# print("Contador de pares e impares")

# par=0
# impar=0
# contador=0
# while contador <= 10:
#     num3=int(input("ingresa un numero: "))
#     if num3 %2 ==0:
#         par+=1
#         print(f"{num3} es un numero par")
#     else:
#         impar+=1
#         print(f"{num3} el numero es impar")
#         num3 +=1

# print("ejercicio 5")
# print("Promedio de calificaciones")

# nota=[]
# notas=input("ingrese su nota  (0 a 5) si deseas finalizar escribe(salir): ")
# while notas!= "salir":
#     nota=float(notas)
#     if 0<=notas and notas <=5:
#         nota.append(notas)
#     else:
#         print("nota invalida")
#     notas=input("ingrese su nota  (0 a 5) si deseas finalizar escribe(salir): ")

# if notas:
#     prom=sum(nota)/len(notas)
#     print(f"el promedio {prom:.2f}")
# else:
#     print("la nota es invalida")
    


# print("ejercicio 6")
# print("Tabla de multiplicar interactiva")

# notas=[]
# calificaciones=input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")
# while calificaciones.lower() != "salir":
#     nota = float(calificaciones )
#     if 0<=  nota <=5:
#         notas.append(nota)
#     else:
#         print("Nota invalida")
#     entrada = input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")

# if notas:
#     promedio=sum(notas)/len(notas)
#     print(f"El promedio: {promedio:.2f}")
# else:
#     print("La nota es invalida")


# print("ejercicio 7")
# print("Adivina el número")

# secret=84
# intentos=0
# print("¡Hola! He escogido un número del 1-100, ¿Crees ser capaz de adivinar cuál es?")
# numeros=int(input("Ingresa un número del 1-60: "))
# while numeros != secret:
#     intentos+=1
#     if numeros < secret:
#         print(f"El número secreto es mayor que {numeros}")
#     else:
#         print(f"El número secreto es menor que {numeros}")
#     numeros=int(input("Ingresa un número del 1-60: "))
# print(f"¡Grandioso! Lograste adivinar el número en {intentos} intentos y el número secreto es: {secret}")


# print("Ejercicio 8")
# print("Tupla de frutas")

# inten=0
# list2=["manzana","mango","banano","uva"]
# print("¡Bienvenido!")
# print("He creado una lista con frutas ¿Podrás adivinar alguna de las frutas que escogí?")
# frut= input("Ingresa la fruta que crees que está en mi lista: ")
# while frut.lower() not in list2:
#     inten+=1
#     print(f"{frut} no está en mi lista, ¡intentemos de nuevo!")
#     frut= input("Ingresa la fruta que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Las frutas que hay en mi lista son: {list2}")


# print("Ejercicio 9")
# print("Diccionario de traducción")

# dic={
#     "hola":"hello",
#     "fue":"was",
#     "por favor":"please",
#     "adios":"good bye",
#     "jugo":"juice"
# }
# print("Bienvenido al traductor español-ingles")
# word=input("Ingrese la palabra en español que desea traducir: ").lower()
# while word not in dic:
#     print("Lo sentimos, no tenemos la traduccion de esta palabra. Intenta de nuevo")
#     word=input("Ingrese la palabra en español que desea traducir: ")
# print(f"La palabra {word} en ingles es {dic[word]}")


# print("Ejercicio 10")
# print("Calculadora básica")

# print("\nEjercicio 10")
# print("Calculadora básica\n")
# print("¡Bienvenido!")
# print("¿Qué operación quisieras realizar ?")
# print("\n-----------------------------------------------")
# print("Suma = 1")
# print("Resta = 2")
# print("Multiplicación = 3")
# print("División = 4")
# print("Salir = 5")
# print("-----------------------------------------------\n")
# sum=1
# rest=2
# multi =3
# divi =4
# salir =5
# while True :
#     ope= int(input("Ingrese el número de la operación que desea realizar: "))
#     numer1 = float(input("Ingrese el primer número: "))
#     numer2= float(input("Ingrese el segundo número: "))
#     if ope == sum:
#         resul= numer1+numer2
#         print(f"El resultado de la suma entre {numer1} y {numer2} es: {resul}")
#     elif ope == rest:
#         resul= numer1-numer2
#         print(f"El resultado de la resta {numer1} y {numer2} es: {resul}")
#     elif ope == multi:
#         resul= numer1*numer2
#         print(f"El resultado de la multiplicación {numer1} y {numer2} es: {resul}")
#     elif ope == divi:
#         resul= numer1/numer2
#         print(f"El resultado de la división {numer1} y {numer2} es: {resul}")
#     else:
#         print("Opción no válida. Por favor, elija una opción del 1 al 5.")
#     volver=input("\n¿Deseas realizar otra operación? (si/no): ")
#     if volver.lower() == "no":
#         print("Saliendo de la calculadora...¡Hasta luego!")
#         break

# print("Ejercicio 11")
# print("Registro de edades")

# personas= {}
# while True:
#     name= input("Ingrese el nombre de la persona (ingrese 'salir' para finalizar): ")
#     if name.lower() == "salir":
#         break
#     edad = int(input(f"Ingrese la edad de {name}: "))
#     personas[name] = edad
# print(f"Personas registradas \n{personas}")



# print("Ejercicio 12")
# print("Buscar en lista")
# inten=0
# lista3=["azul","violeta","anaranjado","verde"]
# print("¡Bienvenido!")
# print("He creado una lista con colores ¿Podrás adivinar algunos de los colores que introduje en esta ?")
# color= input("Ingresa el color que crees que está en mi lista: ")
# while color.lower() not in lista3:
#     inten+=1
#     print(f"{color} no está en mi lista, ¡intentemos de nuevo!")
#     color= input("Ingresa el color que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Los colores que hay en mi lista son: {lista3}")


# print("Ejercicio 13")
# print("Potencias de un número")

# print("¡Bienvenido!")
# nu=int(input("Ingresa un número del cual deseas saber la potencia: "))
# exp=1
# while exp<=5:
#     resu=nu**exp
#     print(f"{nu} elevado a {exp} = {resu}")
#     exp+=1
# print("Programa finalizado ¡good bye!")


# print("Ejercicio 14")
# print("Lista de cuadrados")

# cuadra = []
# contador = 0
# while contador < 5:
#     num2 = int(input("Ingresa un número: "))
#     cálculo = num2 ** 2
#     cuadra.append(cálculo) 

#     print(f"El cuadrado de {num2} es {cálculo}")
#     contador += 1 

# print(f"\nLista de cuadrados ingresados: {cuadra}")
# print("Fin del programa")


# print("Ejercicio 15")
# print("Diccionario de estudiantes")

# studens = {}
# while True:
#     nombre= input("Ingresa el nombre del estudiante: ").lower()

#     if nombre == "fin":
#         print("Programa finalizado")
#         break

#     nota_f = float(input("Ingresa su nota final: "))

#     studens[nombre] = nota_f

#     continuar= input("¿Desea ingresar otro estudiante? (si/no): ").lower()

#     if continuar == "si":
#         print("puede continuar")
#     else:
#         print("Programa detenido")
#         break

# print(f"la lista completa de estudiantes ingresados es: {studens}")
# print("Fin del programa")

