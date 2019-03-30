import math


class Medias:
    """Metodo que obtiene la media geometrica. params: double vals"""
    def mediaAritmetica(self, vals):
        return sum(vals) / len(vals)

    """Metodo que la raiz enesima. params: double num, int k"""
    def raizEnesima(self, num, k):
        return math.pow(num, (1.0 / k))

    def mediaGeometrica(self, vals):
        prod = 1
        for n in vals:
            prod *= n
        return self.raizEnesima(prod, len(vals))

    def mediaArmonica(self, vals):
        sum = 0
        for n in vals:
            sum += 1 / n
        return len(vals) / sum


def main():
    medias = Medias()
    print(medias.mediaAritmetica([2.0, 4.0, 8.0]))
    print(medias.raizEnesima(8.0, 3.0))
    print(medias.mediaGeometrica([1.0, 2.0, 4.0]))
    print(medias.mediaArmonica([2.0, 4.0, 8.0]))


if __name__ == "__main__":
    main()
