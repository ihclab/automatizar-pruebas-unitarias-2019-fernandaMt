def leerCasosPrueba(filename):
    file = open(filename, "r")
    casos = []

    for line in file:
        linelist = line.split(':')
        caso = {
            'no': linelist[0],
            'funcion': linelist[1],
            'entrada': linelist[2],
            'salida': linelist[3],
        }
        casos.append(caso)

    file.close()
    return casos


def main():
    casos = leerCasosPrueba("CasosPrueba.txt")
    for caso in casos:
        if caso['no'] == '0005':
            print(caso)


if __name__ == "__main__":
    main()
