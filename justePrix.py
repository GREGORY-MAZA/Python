import math
import random


def CPU_choix_chiffre():
    return random.randint(0, 100)


def user_input_is_int(saisie_chiffre_utilisateur):
    try:
        saisie_chiffre_utilisateur = int(saisie_chiffre_utilisateur)
    except ValueError:
        saisie_chiffre_utilisateur = input("Réponse non valide, veuillez entrer un  * Entier * ")
        saisie_chiffre_utilisateur = user_input_is_int(saisie_chiffre_utilisateur)
    return saisie_chiffre_utilisateur


def main():

    #  ---------------------------------choix du CPU-------------------------------------------
    choix_du_chiffre_CPU = CPU_choix_chiffre()
    choix_du_chiffre_CPU = int(choix_du_chiffre_CPU)  # convertie en un nombre réel
    #-------------------------------------------------------------------------------------------

    print("Vous avez 10 Tentatives !")

    #  ---------------------------------choix du USER------------------------------------------
    saisie_chiffre_utilisateur = input("Veuillez entrer un entier")
    choix_du_chiffre_user = user_input_is_int(saisie_chiffre_utilisateur)
    # ------------------------------------------------------------------------------------------

    #  ---------------------------------Tentatives User-----------------------------------------
    tentative_user = 0
    # ------------------------------------------------------------------------------------------

    while (choix_du_chiffre_user != choix_du_chiffre_CPU):

        tentative_user = tentative_user + 1
        if (tentative_user == 10):
            print("Vous avez perdu")
            print("GOODBYE !")
            exit()
        if (choix_du_chiffre_user > choix_du_chiffre_CPU):
            print("C'est Moins !")
        if (choix_du_chiffre_user < choix_du_chiffre_CPU):
            print("C'est Plus !")
        saisie_chiffre_utilisateur = input("Essayez à nouveau !")
        choix_du_chiffre_user = user_input_is_int(saisie_chiffre_utilisateur)

    print("BRAVOOOOOO")
    print("Vous avez gagné en ",tentative_user + 1," tentatives")


    # while (le_choix_utilisateur != le_choix_du_CPU):


#
#    print(" Désolé vous n'avez pas trouvé ")
#
#    tentative_utilisateur = tentative_utilisateur + 1
#    print("Nombre de tentative", tentative_utilisateur)
#    if tentative_utilisateur == 10:
#        print(" Désolé, vous avez perdu ")
#        exit()
#
#
#    if (le_choix_utilisateur > le_choix_du_CPU):
#
#        print(" Doucement mon garçon ! ")
#        saisie_chiffre_utilisateur = int(input("Veuillez choisir un chiffre plus petit ! "))  # une chaîne de caractères
#        le_choix_utilisateur = int(saisie_chiffre_utilisateur)
#
#    if (le_choix_utilisateur < le_choix_du_CPU):
#        print(" Encore un effort mon garçon ! ")
#        saisie_chiffre_utilisateur = int(input("Veuillez choisir un chiffre plus grand ! "))  # une chaîne de caractères
#        le_choix_utilisateur = int(saisie_chiffre_utilisateur)
#
#
# print("BRAVOOOOOO")

if __name__ == "__main__":
    main()
