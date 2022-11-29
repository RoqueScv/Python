import abc
from abc import ABC, abstractmethod


class Animal:
    def __init__(self, nombre):
        self.setNombre(nombre)

    def setNombre(self, nombre):
        self.nombre = nombre


@abc.abstractmethod
def sonido(self):
    pass


def __str__(self):
    return "Nombre", self.nombre


class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def sonido(self):
        print("Miau miau")

    def __str__(self):
        return super().__str__(), "Edad", self.raza


animal1 = Gato("Rolo", "Siames")
animal1.sonido()
print(animal1)
