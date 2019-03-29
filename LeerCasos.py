def leerCasosPrueba(filename):
    file = open(filename, "r")

    for line in file:
        print(line)

    file.close()


def main():
    leerCasosPrueba("CasosPrueba.txt")



if __name__ == "__main__":
    main()
