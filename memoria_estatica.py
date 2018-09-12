__author__ = 'Leonel Gonzalez Vidales'

class memDinamica:
    __lista = []

    def __init__(self, list):
    	self.__lista = list

    def getAutos(self):
        return self.__lista

    def recorrerArreglo(self):
        for x in self.getAutos():
            print (self.getAutos().index(x)+1, x)

    def agregarelementoarray(self, elemento):
        self.__lista.append(elemento)

    def ordenarLista(self):
    	self.__lista.sort()

    def eliminarNElementos(self, num):
    	self.__lista.pop(num)

    def eliminarElemento(self, elemento):
    	self.__lista.remove(elemento)

    def insertarNPosicion(self, num, elemento):
    	self.__lista.insert(num, elemento)

    def imprimirLista(self):
    	print (self.__lista)




