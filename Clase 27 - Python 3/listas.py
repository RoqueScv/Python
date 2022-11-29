# Las listas son los arrays de Python

cursos = ["HTML", "JS", "PYTHON"]  # Arranca desde 0, len=3
numeros = [10, 25, 52, 88]
vacia = []

for i in range(len(cursos)):  # for i in cursos
    print(cursos[i])

print(cursos[1])
print(cursos[-1])

x = 0

while x < len(cursos):
    print(cursos[x])
    x += 1

# Listas con sum

print("La suma de los valores en numeros es: ", sum(numeros))

# append agrega al final de la lista (push agrega al final del array)

cursos.append("DJANGO")

# Insert podemos elegir donde insertar

cursos.insert(1, "CSS")

print(cursos)


# pop (Igual al pop de los arrays) el remove (Saca el que quiero)

cursos.pop()

cursos.remove("HTML")

print(cursos)

# Index----->busca valor y devuelve posicion
# Count----->cuantas veces hay algo en la lista
# reverse----->me va a dar vuelta la lista

print("El numero 25 está en el lugar ", numeros.index(25))
print("La lista numeros tiene ", numeros.count(25), "numeros 25")
numeros.reverse()

print(numeros)

# Sort es un ordenador

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros.clear()
print(numeros)
