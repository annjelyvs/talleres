print("DE REGISTRO SIMPLE DE PRODUCTO Y CALCULO DE COSTOS") 

producto= input("Ingrese el nombre del producto: ")
precio_pro= float(input("Ingrese el precio unitario del producto: "))
c_c=int(input("Ingrese la cantidad comprada del producto: "))

tupla=(producto,precio_pro)
lista= [tupla, c_c]

diccionario={
    "producto": lista
}

costo_total= precio_pro*c_c

print(tupla)
print(lista)
print(diccionario)
print(f"El costo total es de todo es : ", costo_total)

print(" FACTURA DE MULTIPLES PRODUCTOS (VERSION FIJA SIN BUCLES)")

producto_1= input("Ingrese el nombre de el producto: ")
precio_1= float(input("Ingrese el precio unitario: "))
cantidad_1= int(input("Ingrese la cantidad comprada del producto: "))

producto_2= input("Ingrese el nombre de el segundo producto: ")
precio_2= float(input("Ingrese el precio unitario: "))
cantidad_2= int(input("Ingrese la cantidad comprada del segundo producto: "))

producto_3= input("Ingrese el nombre de el tercer producto: ")
precio_3= float(input("Ingrese el precio unitario: "))
cantidad_3= int(input("Ingrese la cantidad comprada del tercer producto: "))

tupla_1= (producto_1,precio_1)
tupla_2= (producto_2,precio_2)
tupla_3= (producto_3,precio_3)

lista_1= [tupla_1,cantidad_1]
lista_2= [tupla_2,cantidad_2]
lista_3= [tupla_3,cantidad_3]

diccionario_1={
    "producto 1": lista_1,
    "producto 2": lista_2,
    "producto 3": lista_3
}

total1= precio_1*cantidad_1
total2= precio_2*cantidad_2
total3= precio_3* cantidad_3

total= total1+total2+total3

print(f"El total general es de: ", total)
print(diccionario_1)

print("p3.REGISTRO DE NOTAS DE UN ESTUDIANTE")
nombre= input("Ingrese el nombre del usuario: ")
materia= input("Ingrese una asignatura: ")

nota=float(input("Ingrese la primera nota de : "))
nota1=float(input("Ingrese la segunda nota de: "))
promedio= (nota+nota1)//2

materia2=input("Ingrese una segunda asignatura: ")
nota_2=float(input("Ingrese la primera nota: "))
notal=float(input("Ingrese la segunda nota: "))
promedio2=(nota_2+notal)//2

materia3=input("Ingrese una tercera asignatura: ")
nota3=float(input("Ingrese la primera nota: "))
notas=float(input("Ingrese la segunda nota: "))
prome=(nota3+notas)//2

tu=(materia, promedio)
tu2=(materia2,promedio2)
tu3=(materia3,prome)

list_1=[tu,nota,nota1]
list_2=[tu2,nota_2,notal]
list_3=[tu3,nota3,notas]

listass=[list_1,list_2,list_3]

boletin={
    "nombre": nombre,
    "materias": lista
}
print(boletin)
finished= (promedio+promedio2+prome)//3
print(f"El estudiante", nombre, "obtuvo un promedio final de todas las asignaturas de ", finished)