from Medias import Medias
import pprint
import time


def leerCasosPrueba(filename):
    file = open(filename, "r")
    casos = []

    for line in file:
        linelist = line.split(':')

        caso = {
            'no': linelist[0],
            'metodo': linelist[1],
            'entrada': linelist[2],
            'esperado': linelist[3],
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
                entradasConverted.append(0.0)
            else:
                entradasConverted.append(float(num))

        caso['entrada'] = entradasConverted

        if caso['esperado'] != 'Exception\n':
            caso['esperado'] = float(caso['esperado'])

    return casos


def probarCasos(casos):
    medias = Medias()
    for caso in casos:
        try:
            #validacion del metodo ingresado
            metodo = getattr(Medias, caso['metodo'])
            result = metodo(medias, caso['entrada'])
            esperado = caso['esperado']

            caso['result'] = result

            if esperado == result:
                caso['valido'] = 'Exito'
            else:
                caso['valido'] = 'Falla'

        except:
            print('Exception')
            caso['result'] = 'Exception' 
            caso['valido'] = 'Falla'

    return casos

def pintarResultados(resultados, time):
    print('\u001b[44;1m')
    print(" " * 50)
    print("   PRUEBAS UNITARIAS AUTOMATIZADAS por Fernanda   ")
    print(" " * 50)
    print("   No de casos: {0:10d}".format(len(resultados)) + " " * 24)
    print("   Tiempo de ejecucion: {0:3.9f} sec".format(time) + " " * 11)
    print(" " * 50)
    print('\u001b[0m')
    for resultado in resultados:
        if resultado['valido'] == 'Exito':
            print('\u001b[32m')
        else:
            print('\u001b[31m')
        pprint.pprint(resultado)

def writeResults(results, time):
    pass

def main():
    start = time.time()
    casos = leerCasosPrueba("CasosPrueba.txt")
    casosConverted = conversionTipos(casos)
    resultados = probarCasos(casosConverted)
    executetime = time.time()-start
    pintarResultados(resultados, executetime)


if __name__ == "__main__":
    main()
