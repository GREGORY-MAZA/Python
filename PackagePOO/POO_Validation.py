class CalculSurListe():
    def __init__(self, liste):
        self.__liste = liste

    def calculer(self):
        return self._calculer(self.__liste)

    def _calculer(self, liste):
        raise Exception("Not implemented")


class CalculSurListeSomme(CalculSurListe):

    def _calculer(self, liste):
        total = 0
        for i in range(len(liste)):
            total += liste[i]
        return total


class CalculSurListeProduit(CalculSurListe):
    def _calculer(self, liste):
        total = 1
        for i in range(len(liste)):
            total *= liste[i]
        return total


if __name__ == '__main__':
    # c = CalculSurListe([1, 2, 3, 4])
    c = CalculSurListeSomme([1, 2, 3, 4])
    print(c.calculer())
    c = CalculSurListeProduit([1, 2, 3, 4])
    print(c.calculer())