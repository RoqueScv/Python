# Este es nuestro primer acercamiento a Python!

print("Hola Mundo desde Python!")

# Tipo de datos y armado de variables

entero = 10  # Definicion del numero entero
cadena = "Hola Mundo desde una variable"  # String o cadena de texto
booleanos = True  # Siempre con mayuscula en Python
flotante = 10.5  # Numero decimal


print(cadena)

# Funciones matematicas siguen cumpliendo +,-,*,/

multiplicacion = entero*flotante
print("El resultado de la multiplicacion es:", multiplicacion)

# Expresiones

suma = 2 + 5 + 10 + 52 \
    + 6 + 25 + 85 \
        + 25 + 85

print(suma)

# Comando input, sirve para ingresar variables por el teclado


lado = input("Ingrese el lado de un cuadrado: ")
# Si no le indicamos nada input toma todo como strings


lado = int(lado)  # convertimos a lado en un numero entero

area = lado*lado

print("El area del cuadrado es ", area)
