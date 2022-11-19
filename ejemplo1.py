class calculadora:
    def __init__(self):
        self.numero1 = float(input("ingrese el primer numero"))
        self.numero2 = float(input("ingrese el segundo numero"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.numero1 + self.numero2
        print(f"La suma de los dos numeros es {suma}")
        
    def restar(self):
        resta = self.numero1 - self.numero2
        print(f"La resta de los dos numeros es {resta}")
        
    def multiplicacion(self):
        multiplicacion = self.numero1 * self.numero2
        print(f"La suma de los dos numeros es {multiplicacion}")
        
    def division(self):
        division = self.numero1 / self.numero2
        print(f"La suma de los dos numeros es {division}")
        
    def __del__(self):
        print("Se ha eliminado la operacion")