import operator


def nb_de_ventes(dict):
    return len(dict)


def nom_vendeur(vendeur):
    return vendeur.keys()


def nom_meilleur_vendeur(best):
    return max(best.items(), key=operator.itemgetter(1))[0]


def main():
    ventes = {"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
    
    print(nb_de_ventes(ventes))
    print(nom_vendeur(ventes))
    print(nom_meilleur_vendeur(ventes))


if __name__ == '__main__':
    main()