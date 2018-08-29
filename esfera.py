__author__ = 'Leonel Gonzalez'

import math


class Esfera:
    __radio = 0

    """
    Metodo constructor
    """

    def __init__(self, rad):
        if rad > 0:
            self.__radio = rad
        else:
            self.__radio = 0

    def getRadio(self):
        return self.__radio

    def setRadio(self, rad):
        self.__radio = rad

    def getDiametro(self):
        return (self.__radio * 2)

    def getCircunferencia(self):
        return (self.getDiametro() * math.pi)

    def getArea(self):
        return (4 * math.pi * self.__radio * self.__radio)

    def getVolumen(self):
        return (4 * math.pi * math.pow(self.__radio, 3)) / 3
