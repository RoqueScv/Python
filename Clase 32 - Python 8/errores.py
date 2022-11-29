# Error de sintaxis

# print("Hola mundo"

# Error de nombre

#prin("Hola mundo")

# Error semantico

lista = []
if len(lista) > 0:
    lista.pop()

# Excepciones

while(True):
    try:
        n = float(input("Ingrese un numero: "))
        m = 5
        print("{}/{} = {}".format(n, m, n/m))

    except:
        print("Se produjo un error, intente nuevamente")
    else:
        print("La division no dio error")
        break
    finally:
        print("Se terminó una iteracion")
