from Medias import Medias
import pprint


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

def pintarResultados(resultados):
    for resultado in resultados:
        if resultado['valido'] == 'Exito':
            print('\u001b[32m')
        else:
            print('\u001b[31m')
        pprint.pprint(resultado)


def main():
    casos = leerCasosPrueba("CasosPrueba.txt")
    casosConverted = conversionTipos(casos)
    resultados = probarCasos(casosConverted)
    pintarResultados(resultados)


if __name__ == "__main__":
    main()
