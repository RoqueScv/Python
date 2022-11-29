class Animal:
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        print("Guau guau")


class Gato(Animal):
    def hablar(self):
        print("Miau")


class Vaca(Animal):
    def hablar(self):
        print("Mu")


for animal in [Perro(), Gato(), Vaca()]:
    animal.hablar()
