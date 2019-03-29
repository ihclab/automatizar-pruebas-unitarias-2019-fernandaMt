import math


class Medias:
    def mediaAritmetica(self, vals):
        return sum(vals) / len(vals)

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
    print(medias.mediaAritmetica([2, 4, 8]))
    print(medias.raizEnesima(8, 3))
    print(medias.mediaGeometrica([1, 2, 4]))
    print(medias.mediaArmonica([2, 4, 8]))


if __name__ == "__main__":
    main()
