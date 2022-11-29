##para definir una lista sin datos
listaPersonas = []

##Para cargar valores en la lista
##listaPersonas.append("Juan")
##listaPersonas.append("Jose")
##listaPersonas.append("Carlos")
##listaPersonas.append("Maria")


dato = input("inserte un nombre en la lista: ")
while dato != "salir":
    listaPersonas.append(dato)
    dato = input("inserte otro nombre en la lista: ")
    
print("-----------------------------")

##buscar un elemento en la lista
encontrado = False
buscado = input("ingrese nombre a buscar: ")
contador1 = 0
for elemento in listaPersonas:
    if elemento == buscado:
        print("Se encontro a: ",elemento)
        encontrado = True
    contador1 = contador1 + 1
if encontrado == False:
    print("No se encontro a: ",buscado)


##borrar un elemento de la lista
borrado = input("ingrese nombre a borrar: ")
contador2 = 0
for elemento in listaPersonas:
    if elemento == borrado:
        del(listaPersonas[contador2])
    contador2 = contador2 + 1

print(listaPersonas)



