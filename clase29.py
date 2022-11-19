#definicion de clase que nos permita cargar nombre, id y edad de una persona
#metodo que nos permite imprimir los datos de la persona
#ver si es mayor de edad o no

class Persona: #Clase viene a ser la plantilla
    def inicializar(self, nombre, id, edad): #Metodos son las funciones dentro de la clase (inicializar e imprimir)
        self.nombre = nombre
        self.id = id
        self.edad = edad
    
    def imprimir(self):
        print(self.nombre, self.id)
        print("El nombre de la persona es", self.nombre)
        print(f"El id de la persona es {self.id}")
        print("La edad de la persona es", self.edad)

persona1 = Persona() #persona1 va a ser objeto de la clase Persona
persona1.inicializar("Arturo", 534535)
persona1.imprimir()

persona2 = Persona() 
persona2.inicializar("Juan", 453345)
persona2.imprimir()

persona2 = Persona() 
persona2.inicializar("Jose", 123456)
persona2.imprimir()