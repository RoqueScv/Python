class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def operaciones(self):
        print(f"{self.nombre} tiene depositado {self.monto} pesos")

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Arturo")
        self.cliente2 = Cliente("Julieta")
        self.cliente3 = Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(2000)
        self.cliente2.depositar(10000)
        self.cliente3.depositar(30000)
        self.cliente1.extraer(1000)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print(f"El total de los depositos es {total}")
        self.cliente1