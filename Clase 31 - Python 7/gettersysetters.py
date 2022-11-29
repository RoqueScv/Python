# Getters y setters

class ListadoBebidas:

    def __init__(self):
        self.__gaseosa = 'Gaseosa'
        self.__bebidas_validas = ['Gaseosa', 'Jugo']

    @property
    def gaseosa(self):
        return "Una bebida valida es: {}".format(self.__gaseosa)

    @gaseosa.setter
    def gaseosa(self, gaseosa):
        self.__gaseosa = gaseosa


bebidas = ListadoBebidas()
print(bebidas.gaseosa)
bebidas.gaseosa = "Agua"
print(bebidas.gaseosa)
