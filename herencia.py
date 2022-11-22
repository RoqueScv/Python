#Superclase Persona, estoy me trae atributos y metodo 
#Subclase Empleado, atributos y metodos de persona y atributos y metodos empleado

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.dni = int(input("Ingrese su DNI: "))

    def imprimir(self):
        print(f"{self.nombre} tiene un DNI de numero {self.dni}")

class Empleado(Persona):        #Clase hijo, hereda metodos y atributos de Persona
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese su sueldo: "))
        
    def imprimir(self):
        super().imprimir()
        print ("Sueldo: ",self.sueldo)

    def paga_ganancias(self):
        if self.sueldo > 300000:
            print("El empleado debe pagar ganancias")
        else:
            print("El empleado no debe pagar ganancias")

persona1 = Persona()
persona1.imprimir()

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_ganancias()