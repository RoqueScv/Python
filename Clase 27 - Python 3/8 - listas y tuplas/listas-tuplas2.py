##defino una lista y una tupla
lista = [10,-20,5,0]
tupla = ('Hola',10,2.5,True)

print(lista[3])
print('Valor en el indice 3 de la lista:',lista[3])

print(tupla[0])
print('Valor en el indice 0 de la tupla:',tupla[0])

print('----------------------------------')

lista[1]= 90
print(lista)

## no se puede modificar el valor en una tupla
##tupla[0]='Chau' 
print(tupla)

print('Impresion de rangos')

print(lista[1:3])#[90 5]

print(lista[:3])#[10 90 5]

print(lista[1:])#[90 5 0]

print(tupla[1:])#[10 2.5 True]

print('copia de estructuras')

lista2 = lista[2:]
print(lista2)

print('agrego elemento a la lista')
lista.append(100)
print(lista)

print('busqueda de valor en la lista')

if 100 in lista:
    print('El valor 100 esta en la lista')
else:
    print('El valor 100 NO esta en la lista')


if 'Chau' in tupla:
    print('El valor Chau esta en la tupla')
else:
    print('El valor Chau NO esta en la tupla')

if 'Juan' not in tupla:
    print('Juan no esta en la tupla')
else:
    print('Juan SI esta en la tupla')

print('Eliminamos datos de la lista')
del(lista[0])
print(lista)

print(lista[0])#[90, 5, 0, 100]

del(lista[:2])
print(lista)#[0, 100]

del(lista[:])#elimino todos los datos de la lista
print(lista)

del(lista)# elimino la lista
##print(lista)

##se puede  volver a definir una lista con el mismo identificador
lista =[1,2]
print(lista)

print('creo lista vacia y le agrego elementos')
edades = []
edades.append(10)
edades.append(20)
edades.append(30)

print(edades)


##tupla.append(30)
##print(tupla)

print('Longitud de la lista = ', len(lista), 'elementos')

print('Ejercicio')

numeros = []
for indice in range(0,5):
    valor = int(input('ingrese un valor : '))
    numeros.append(valor)
    
print(numeros)


print('Ejercicio 2')
numeros2 = []
for indice in range(0,5):
    valor = int(input('ingrese un valor : '))
    numeros2.append(valor)
    print('Indice:',indice,'Valor:',numeros2[indice])


print('Ejercicio 3')
numeros3 = [10,20,30,40,50]

for valor in numeros3:
    print(valor)


















    



















































    
    

















































