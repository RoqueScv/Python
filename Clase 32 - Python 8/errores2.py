
# Division por zero
# print(10/0)

# Type error
# print(10+"Hola")

# name error
#print(4 + spam*5)

try:
    n = float(input("Ingrese un numero divisor: "))
    10/n
except ZeroDivisionError:
    print("No se puede divivir por cero")
except ValueError:
    print("No se puede dividir un numero por un string")
except TypeError:
    print("No se puede dividir un string por un numero")
else:
    print("La division no dio error")
