def affiche_dictionnaire(student):
    find = student.find(";") #permet de trouver la premiere position du caractere mis en parametre
    student.split()
    return find


def main():
    chaine_etudiants = """213615200;BESNIER;JEAN
    213565488;DUPOND;MARC
    214665555;DURAND;JULIE"""
    print(affiche_dictionnaire(chaine_etudiants))


if __name__ == '__main__':
    main()

    #TODO check  .split OK
    #TODO décomposer la chaine
    #TODO .find pour trouver le";" OK