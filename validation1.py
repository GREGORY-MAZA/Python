def calculer_somme_des_3_valeurs(x,y,z):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0
    return x + y + z



def main():
    Saisie_1 = int(input("Merci de choisir votre 1ere Valeur"))
    Saisie_2 = int(input("Merci de choisir votre 2eme Valeur"))
    Saisie_3 = int(input("Merci de choisir votre 3eme Valeur"))
    print (calculer_somme_des_3_valeurs(Saisie_1, Saisie_2, Saisie_3))



if __name__ == '__main__':
    main()