# Syntax error --- error de sintaxis

# print("Hola Mundo!!!"

# Error de nombre

#prit("Hola Mundo!!!!")

# Error de indentacion

# def verIndentacion(self):
#print("Que tipo de error es este?")

# Error de tipo
# print("palabra"+5)

# zero division
# print(5/0)

# Error semantico --- index

#lista = []
# lista.pop()


# excepciones

while(True):
    try:
        n = float(input("Ingrese un numero: "))
        m = 10
        print("{}/{}={}", n, m, m/n)

    except:
        print("Se produjo un error, por favor cambie los numeros")
    else:
        print("La division no tiene errores")
        break
    finally:
        print("Se termino nuestro programita!")
