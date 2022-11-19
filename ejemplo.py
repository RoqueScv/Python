# ejemplo de clases

class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("El auto esta en movimiento")

    def frenar(self):
        print("El auto esta detenido")

auto1 = Auto("Fiat", 2014)

print(f"Mi auto es un {auto1.marca} modelo {auto1.modelo}")

auto1.acelerar()
auto1.frenar()