class Perro:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} hace guau guau"

    def __str__(self):
        return f"{self.nombre} es un perro que ladra y que tiene {self.edad} anios"

perro1 = Perro("Pocho",5)
print(perro1.nombre)
print(perro1.ladrar())
print(perro1)

