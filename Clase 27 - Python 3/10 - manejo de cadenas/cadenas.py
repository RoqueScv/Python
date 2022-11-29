# Formatos de Cadenas STRING
import sys
print("Ejercicio 1")
x1=10
x2=5
x3=20
print ('El contenido de la primer variable es %d, de la segunda %d y la tercera %d' % (x1,x2,x3))


sys.stdin.readline()
print("Ejercicio 2")
x=10
g=10.2
cadena='juan'
print ('El valor entero %d el valor real %f y la cadena %s' % (x,g,cadena))


sys.stdin.readline()
print("Ejercicio 3")
x1=100
x2=1500
x3=5

print ('%5d' % (x1))
print ('%5d' % (x2))
print ('%5d' % (x3))


sys.stdin.readline()
print("Ejercicio 4")
# uso de lista
animales=['perro','elefante','pez']
print('')
for elemento in animales:
    print ('%20s' % elemento)
for elemento in animales:
    print ('%-20s' % elemento)

sys.stdin.readline()
print("Ejercicio 5")
# decimal octal hexadecimal
print ('')
for num in range(1,256):
    print ('%3d   %3o   %3x' % (num,num,num))
print('')

sys.stdin.readline()
print("Ejercicio 6")
# Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y 
# la cantidad de letras que lo componen.
nombre=input("Ingrese su nombre: ")
print("Primer caracter: ")
print(nombre[0])
print("Cantidad de letras del nombre: ")
print(len(nombre))

sys.stdin.readline()
print("Ejercicio 7")
# Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza 
# con vocal dicho nombre.
nombre=input("Ingrese su nombre: ")
if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print("El nombre ingresado comienza con vocal")
else:
    print("El nombre ingresado no comienza con vocal")
    


sys.stdin.readline()
print("Ejercicio 8")
# Ingresar un mail por teclado. Verificar si el string ingresado contiene 
# solo un caracter "@".
mail=input("Ingrese un mail: ")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")


sys.stdin.readline()
print("Ejercicio 9")
# Inicializar un string con la cadena "jUaN" luego llamar a sus métodos upper(), lower() y 
# capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla.
nombre1="jUaN"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)

sys.stdin.readline()
print("Ejercicio 10")
# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""
oracion=input("Ingrese una oracion: ")
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de espacios en blanco ingresado son ")
print(cantidad)


sys.stdin.readline()
print("Ejercicio 11")
# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la 
# cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea 
# más fácil disponer la condición que verifica que es una vocal.
oracion=input("Ingrese una oracion: ")
oracionmin=oracion.lower()
cantidad=0
x=0
while x<len(oracionmin):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de vocales de la oracion son ")
print(cantidad)

sys.stdin.readline()
print("Ejercicio 12")
# Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en 
# caso contrario mostrar un mensaje de error.
clave=input("Ingrese una clave que tenga entre 10 y 20 caracteres: ")
if len(clave)>=10 and len(clave)<=20:
    print("Longitud correcto")
else:
    print("Longitud incorrecto")