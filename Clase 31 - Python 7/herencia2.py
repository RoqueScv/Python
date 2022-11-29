
class Numeros:

    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.total = 0

    def cargar1(self):
        self.numero1 = float(input("Ingrese el primer numero: "))

    def cargar2(self):
        self.numero2 = float(input("Ingrese el segundo numero: "))

    def resultado(self):
        print(f"El resultado de la operacion es: {self.total} ")

    def operar(self):
        pass


class Suma(Numeros):
    def operar(self):
        self.total = self.numero1 + self.numero2


class Resta(Numeros):
    def operar(self):
        self.total = self.numero1 - self.numero2


suma1 = Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
suma1.resultado()


resta1 = Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
resta1.resultado()
