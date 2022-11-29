##tuplas
tupla1 = (1,2,3,4)
lista1 = [1,2,3,4]
print (lista1)
print("------------------------------")
print(tupla1) #contenido de la tupla

print('Contenido en la posicion 2: ',tupla1[2])

##Recorro la tupla con un for
for elemento in tupla1:
    print(elemento)

## Modificamos el contenido de la posicion 3
##tupla1[3] = 20 --> en la tupla no puedo reasignar un valor
##pero en la lista si
lista1[3] = 20


print(lista1)

print("----------------------------------------")

print("copio parte de una tupla a la otra tupla")
tupla2 = tupla1[1:3]#2,3
print(tupla2)

tupla2 = tupla1[1:4]#2,3,4
print(tupla2)

tupla2 = tupla1[1:50]#2,3,4
print(tupla2)

tupla2 = tupla1[2:]#3,4
print(tupla2)

tupla2 = tupla1[:2]#1,2
print(tupla2)

##UNE ELEMENTOS
resultado = tupla1 + tupla2 #une los elementos de ambas estructuras
print(resultado)

print("--------------------")

lista2 = [10,20,30,40]
resultado2 = lista1 + lista2 #une los elementos de ambas estructuras
print(resultado2)

print("------------------------------------------")

print(tupla2[1:])
print("------------------------------------------")

parte1 = tupla1[0:2]#1,2
parte2 = tupla2[1:]#2

resultado3 = parte1 + parte2
print(resultado3)

print("------------------------------------------")

print("Busqueda de valores en una lista: ")
if 50 in lista1:
    print("el valor 50 esta en la lista 1")
else:
    print("el valor 50 no esta en la lista 1")



print("------------------------------------------")

print("Borramos un valor en la lista: ")

del(lista1[3])#Borro el valor 20
print(lista1)

print("------------------------------------------")

print("Error de indice fuera de rango: ")
##print(lista1[3])

print("Lista con elementos de diferente tipo: ")
lista3 = ['Hola','Chau',20,1.234]
print(lista3)

print("------------------------------------------------")
##Ejercicios
##Ejercicio1: Ingresar por teclado 5 edades y guardarlas en una lista.
##Imprimir solamente los mayores de edad.
edad = [0,0,0,0,0]
mayores18 = [0,0,0,0,0]
for i in range(0,5):
    edad[i] = int(input('Ingrese una edad: '))
    if(edad[i] >= 18):
        mayores18[i] = edad[i]

print('Los mayores a 18: ')
for j in range(0,5):
    if mayores18[j] != 0:
        print(mayores18[j])
    



##Ejercicio2: Ingresar por teclado valores enteros y positivos a una
##lista hasta que sea cero.
##Imprimir maximo, minimo y promedio.

## nota: longitud de una estructura
##print(len(lista1))

print('------------------------------------------------')
listaValores = []
maximo = 0
suma = 0
minimo = 1000
numero = int(input('Ingrese un numero positivo: '))
while numero != 0:
    listaValores.append(numero)
    suma = suma + numero
    if maximo < numero:
        maximo = numero
    if minimo > numero:
        minimo = numero
    numero = int(input('Ingrese otro numero positivo: '))
print('Maximo: ',maximo)
print('Minimo: ',minimo)
print('Promedio: ',suma / len(listaValores))
print(listaValores)























































