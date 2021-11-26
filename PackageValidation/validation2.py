def calculer_la_somme(x, y, z):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0
    return x + y + z


def check_saisie(saisie_utilisateur):
    try:
        return int(saisie_utilisateur)
    except ValueError:
        return check_saisie(input("Merci de choisir un Entier"))


def main():
    saisie1 = check_saisie(input("veuillez saisir votre 1er choix "))
    saisie2 = check_saisie(input("veuillez saisir votre 2eme choix "))
    saisie3 = check_saisie(input("veuillez saisir votre 3eme choix "))
    print(calculer_la_somme(saisie1, saisie2, saisie3))


if __name__ == '__main__':
    main()
