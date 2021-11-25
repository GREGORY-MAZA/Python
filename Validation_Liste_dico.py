def main():
    #- Une liste est instanciée
    ma_liste = []
    ma_liste_2 = [1,2,3]


    #- Des éléments sont ajoutés à une liste (append)
    ma_liste.append("salut")
    ma_liste.append("ok")
    ma_liste.append("hello")
    print(ma_liste)

    #- L'existence d'un élément d'une liste est vérifiée (in)
    if "salut" in ma_liste:
        print("Oui oui oui")

    # Des éléments sont retirés d'une liste (del)
    del ma_liste[0]
    print(ma_liste)

    #Un élément est inséré dans une liste (insert)
    ma_liste.insert(100,"TOTO")
    print(ma_liste)

    #Un élément est extrait d'une liste (pop)
    ma_liste.pop(1)
    print(ma_liste)

    #Deux listes sont fusionnées (extend)
    ma_liste_2.extend(ma_liste)
    print(ma_liste_2)


    #Un élément d'une liste précis est affecté à une variable ([n])
    n = ma_liste[0]
    print(n)

    #Une liste d'entiers est triée
    ma_liste_3 = [9, 4, 2, 10, 5, 20]
    ma_liste_3.sort()
    print(ma_liste_3)

    #Une sous liste est créée à partir d'une liste (slice)
    ma_liste_4 = ma_liste_3[2:5]
    print(ma_liste_4)

    #Une liste est créée par copie d'une autre liste
    ma_liste_5 = list(ma_liste)
    print(ma_liste_5)

    #Deux variables font référence à une même liste, la liste est modifié à travers la première variable, et le résultat est affiché à travers la deuxième variable
    one = ma_liste
    two = ma_liste
    two[0] = "Changement"
    print(one[0])

    #La liste est affichée à l'écran au moyen d'une boucle for
    for i in range(len(ma_liste_3)):
        print(ma_liste_3[i])

    #Un dictionnaire est instancié
    dictionnaire = {}

    #Un nouveau couple clé/valeur est ajouté au dictionnaire
    dictionnaire.update({"Greg": "Maza"})
    print(dictionnaire)

    #Une valeur du dictionnaire est affichée à partir de la clé (l[key])
    print(dictionnaire["Greg"])

    #Une valeur du dictionnaire est modifiée à partir de la clé
    dictionnaire["Greg"] = "x"
    print(dictionnaire)

    #Une clé du dictionnaire est supprimée (del)
    dictionnaire2 = {"key1": "Value1", "key2": "Value2", "key3": "Value3"}
    del dictionnaire2["key1"]
    print(dictionnaire2)

    #L'existence d'une clé du dictionnaire est vérifiée (in)
    if "key3" in dictionnaire2:
        print("ok ok ok")

    #Le dictionnaire est affiché au moyen d'une boucle (clé et valeur)
    for key,value in dictionnaire2.items():
        print(key,value)

if __name__ == '__main__':
    main()