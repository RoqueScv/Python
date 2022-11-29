# Crear una funcion que valide el ingreso de numeros naturales

def ingresarNaturales(msj):
    while True:
        try:
            valorReal = float(input(msj))
            valor = int(valorReal)
            assert (valor == valorReal), "No es un numero natural"
            assert (valor > 0), "No es un numero natural"
            break
        except AssertionError as error:
            print(error)
        except ValueError:
            print("No es un numero")
        except:
            print("Error desconocido")
        return valor

# Programa Principal


def __main__():
    mje = "Ingrese un numero natural: "
    num = ingresarNaturales(mje)
    print("El numero ingresado es: ", num)


__main__()
