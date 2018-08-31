__author__ = 'Leonel Gonzalez Vidales'

class memoria_estatica:
    __autos = ['Audi', 'Ferrari', 'Ford']

    def getAutos(self):
        return self.__autos

    def recorrerArreglo(self):
        for x in self.getAutos():
            print self.getAutos().index(x)+1, x

    def agregarelementoarray(self, elemento):
        self.__autos.append(elemento)
