import os.pathPython


def afficher_ligne():
    with open("data.txt", "r") as file:
        lignes = file.readlines()
        for ligne in lignes:
            saisie_ligne_suivante = input("Voici la liste : Taper s pour passer à la ligne suivante ")
            if saisie_ligne_suivante == "s":
                print(ligne)
    main()


def ajouter_une_ligne():
    with open("data.txt", "a") as file:
        saisie_utilisateur = input("Quel message voulez-vous écrire ? ")
        file.write(f"{saisie_utilisateur}\n")


def main():
    path = 'data.txt'

    if os.path.exists(path):  # Vérifie si le chemin existe
        ajouter_ligne = input('Un fichier data.txt est déjà présent. Voulez-vous rajouter une ligne ? y / n ')
        if ajouter_ligne == "y":
            ajouter_une_ligne()
        afficher_ligne()
    else:
        try:
            print("Création du fichier data.txt")
            file = open('data.txt', "w")
            file.close()
            main()
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur d\'ouverture.')


if __name__ == '__main__':
    main()
