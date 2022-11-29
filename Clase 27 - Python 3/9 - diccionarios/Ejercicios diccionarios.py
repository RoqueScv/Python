print('Ejercicio 1:')

##En el bloque principal del programa definir un diccionario que almacene
##los nombres de paises como clave y como valor la cantidad de habitantes.
##Implementar una función para mostrar cada clave y valor.

## defino la funcion
def mostrarPoblacion(paises):
    for clave in paises:
        print('Pais: ' + clave + ' Poblacion:',paises[clave])


## bloque principal
paises =    {
                'Argentina':46000000,
                'Uruguay':3000000,
                'Ucrania':44000000,
            }

## llamo a la funcion
mostrarPoblacion(paises)



print('Ejercicio 2:')
##Crear un diccionario que permita almacenar 5 artículos, utilizar como clave
##el nombre de productos y como valor el precio del mismo.
## 
##Desarrollar además las funciones de:
##   Imprimir en forma completa el diccionario
##   Imprimir solo los artículos con precio superior a 100.

def imprimirDiccionario(listasProd):
    for producto in listasProd:
        print('Producto: ' + producto + ' Precio:',listasProd[producto])

def imprimirMayor100(listasProd):
    for producto in listasProd:
        if listasProd[producto] > 100:
            print('Producto por encima de 100 $ : ' + producto)
    

##Bloque Principal
## cargo el dicccionario
listasProd = {}

for x in range(3):
    producto = input('Ingrese un producto: ')
    precio = int(input('Ingrese un precio: '))
    listasProd[producto] = precio

##print(listasProd)


imprimirDiccionario(listasProd)
print('-----------------------')
imprimirMayor100(listasProd) 



















