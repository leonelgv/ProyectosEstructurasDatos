class convertidor:

    def convertirDecimalABinario(self, numeroAConvertir, residuo, lista):
        if (numeroAConvertir <= 0):
            return lista
        else:
            residuo = numeroAConvertir % 2
            w = (int(numeroAConvertir / 2))
            lista.insert(0, residuo)
            return self.convertirDecimalABinario(w, residuo, lista)


    def decimalABinario(self, numeroAConvertir):
        if (numeroAConvertir <= 1):
            return 1
        else:
            return str(self.decimalABinario(int(numeroAConvertir / 2))) + str(numeroAConvertir % 2)

    def decimalAOctal(self, numeroAConvertir):
        if (numeroAConvertir <= 7):
            return numeroAConvertir
        else:
            return str(self.decimalABinario(int(numeroAConvertir / 8))) + str(numeroAConvertir % 8)

