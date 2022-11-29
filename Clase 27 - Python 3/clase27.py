# Cadenas de caracteres o strings

cadenas = 'Entre comillas el "contenido"'
cadenas1 = "Las comillas pueden ser 'dobles'"
cadenarepetida = cadenas*3
vacia = ""
numero = "10"


print(cadenas + cadenas1 + numero)

print(cadenarepetida)

cadena1 = "Arturo"
cadena2 = "arturo"

print(cadena1 == cadena2)  # Case sensitive

print(len(cadenas))  # Nos devuelve la longitud de la cadena lenght
print(cadenas[0])  # Me devuelve la primera letra de cadenas

print(cadenas.lower())  # es como tener lower case de js
print(cadenas.upper())  # El upper case
print(cadenas.capitalize())  # A la primera letra la pone en Mayuscula

# Slice o rebanadas


print(cadenas[:5])  # cadenas[principio:final+1]
print(cadenas[10:])  # Vacio, va hasta el final
print(cadenas[:])

for letra in cadena1:
    print(letra)

# min y max hace referencia al codigo ascii

print(min(cadena1))
print(max(cadena1))

# join split y replace

cadena3 = ' '.join(cadena1)
print(cadena3)

lista = cadenas.split(' ')  # Lista es parecido al array de JS
print(lista)

reemplazar = cadenas.replace('e', 'E')
print(reemplazar)

# f strings es muy similiar a ${} en JS o {{}} en vue

print(f'Suma de 5 + 8 es {5+8}')

num1 = 5
num2 = 8

print(f'Suma de {num1} + {num2} es {num1 + num2}')
