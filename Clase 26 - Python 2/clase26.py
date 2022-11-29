"""Esta es la clase numero 26-Python 2"""

print("Estructuras secuencial")

# Secuenciales son acciones que se ejecutan una debajo de la otra

numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))

print("La suma de los dos numeros da como resultado",
      numero1+numero2)

# Estructuras condicionales (If, else, elif)

edad = int(input("Ingrese la edad de la persona:"))

if edad < 18:
    print("Usted es menor de edad!")
elif edad == 18:
    print("Usted tiene justo 18 años")
elif edad == 87:
    print("Usted tiene 87 años")
else:
    print("Usted es mayor de edad!")


nota = int(input("Ingrese la nota del parcial:"))

if nota >= 0 and nota < 4:  # solamente entra si está entre 0 y 4
    print("Estas desaprobado")
elif nota >= 4 and nota < 7:
    print("Estas aprobado")
elif nota >= 7 and nota <= 10:
    print("Estas promocionado!")
else:
    print("El numero ingreso debe estar entre 0 y 10")

# Bloques de iteracion!
# Ejemplos de while

print("Contador de numeros del 1 al 10")

contador = 1
while contador < 11:  # Reminder <11 o <= 10
    print(contador)
    contador = contador + 1

print("Suma de los numeros del 1 al 10")

contador1 = 1
dato = 0
while contador1 <= 10:
    dato = dato + contador1
    contador1 += 1

print("La suma del numero 1 al 10 es igual a:", dato)

# Ejemplos de bucle for

print("Ejemplo de bucle for")

for i in range(1, 11):
    print(i)

menor10 = 0
mayor10 = 0

for x in range(3):
    numero = int(input("Ingrese su numero:"))
    if numero >= 10:
        mayor10 += 1
    else:
        menor10 += 1

print("Cantidad de numeros mayores a 10:", mayor10)
print("Cantidad de numeros menores a 10:", menor10)


print("Ejemplo de Diego")
z = 0

for z in range(1, 11, z+2):
    print(z)

print("Ejemplo de Matias")

for i in range(1, 11, 2):
    print(i)
