def leerCasosPrueba(filename):
    file = open(filename, "r")
    casos = []

    for line in file:
        linelist = line.split(':')

        caso = {
            'no': linelist[0],
            'metodo': linelist[1],
            'entrada': linelist[2],
            'salida': linelist[3],
        }
        casos.append(caso)

    file.close()
    return casos


def conversionTipos(casos):
    for caso in casos:
        entradasList = caso['entrada'].split(' ')
        entradasConverted = []

        for num in entradasList:
            if num == "NULL":
                entradasConverted.append(None)
            else:
                entradasConverted.append(float(num))

        caso['entrada'] = entradasConverted

        if caso['salida'] != 'Exception\n':
            caso['salida'] = float(caso['salida'])

    return casos


def main():
    casos = leerCasosPrueba("CasosPrueba.txt")
    casosConverted = conversionTipos(casos)
    print(casosConverted)


if __name__ == "__main__":
    main()
